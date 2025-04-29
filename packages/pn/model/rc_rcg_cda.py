#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# gedi: ge-stionale di-rezionale
# Strumenti per la gestione contabile, amministrativa, finanziaria,
# per il controllo di gestione e direzionale.
# Copyright (C) 2023 Massimo Masson
# 
# This program is dual-licensed.
# 
# Option 1:
# If you respect the terms of GNU GPL license, AND
# you agree to give the copyright for modifications or derivative work
# to the original author Massimo Masson, the GPL license applies.
# In this case:
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# 
# Option 2:
# If you do not agree with any of the statements in option 1, then
# a proprietary license applies. In this case, contact the author
# for a dedicated propietary license.
# 

from competenze import competenza_AAAAMM

#
# firma automatica del programma di creazione righe in analitca
#
FIRMA_AUTO_rc_rcg_cda = 'pn.rc_rcg_cda'

class Table(object):
    def config_db(self, pkg):
        '''rc_rcg_cda: dettaglio centri di una riga di registrazione contabili

        Questa tabella serve per dettagliare i centri di analisi di ciascuna
        riga contabile di una rilevazione contabile.
        Da questa verranno generati i movimenti di analitica.
        '''

        tbl = pkg.table('rc_rcg_cda', pkey='id', 
                        name_long="!![it]CDA riga",
                        caption_field='caption'
                        )

        self.sysFields(tbl, counter='rc_rcg__id')

        # foreign key to rc_rcg - riga di riferimento
        rc_rcg__id = tbl.column('rc_rcg__id', dtype = 'A', size = '22',
                                name_long = '!![it]Riga contabile',
                                unmodifiable=True,
                                validate_notnull = True
                                )
        rc_rcg__id.relation('pn.rc_rcg.id', mode = 'foreignkey',
                            relation_name = 'cda_rcg', 
                            onDelete = 'cascade'
                            )
        
        # foreing key to cda_cod - codice piano centri di analisi
        cda_cod__cod = tbl.column('cda_cod__cod', dtype='A', size=':32',
                                  defaultFrom='@rc_rcg__id.@rc__id.@sog__cod.cda_cod__cod',
                                  name_long = '!![it]CDA cod.',
                                  #unmodifiable=False,
                                  validate_notnull=True,
                                  )
        cda_cod__cod.relation('pn.cda_cod.cod', mode='foreignkey',
                              relation_name='CDACOD_riga',
                              onDelete='raise'
                              )

        # foreing key to cda_centri - il centro di analisi
        cda_centri__cod = tbl.column('cda_centri__cod', dtype='A', size=':64',
                                     name_long = '!![it]CDA',
                                     #unmodifiable=False,
                                     validate_notnull=True,
                                     )
        # cda_centri__cod.relation('pn.cda_centri.cod', mode='foreignkey',
        #                          relation_name='CDA_riga',
        #                          #one_one=True,
        #                          onDelete='raise'
        #                          )

        #
        # foreign key to cda_centri cpk
        #
        cda_centri__fk = tbl.compositeColumn('cda_centri__fk', 
                                             columns='cda_cod__cod,cda_centri__cod',
                                             name_long = '!![it]Centro',
                                             )
        cda_centri__fk.relation('pn.cda_centri.cpk', mode='foreignkey',
                                relation_name = "CDA_riga",
                                #one_one = True,
                                onDelete = 'raise',
                                )                                            

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione dettaglio CdA', 
                   )

        tbl.column('dare_udc', dtype='N', size='12,2',
                   name_long='!![it]Dare', 
                   name_short='!![it]D',
                   #validate_notnull=True,
                   )

        tbl.column('avere_udc', dtype='N', size='12,2',
                   name_long='!![it]Avere', 
                   name_short='!![it]A',
                   #validate_notnull=True,
                   )

        tbl.formulaColumn('saldo_udc', 'COALESCE($dare_udc, 0) - COALESCE($avere_udc, 0)',
                          dtype='N', size='12,2',
                          name_long='!![it]Saldo', 
                          name_short='!![it]S'
                          )

        # tbl.aliasColumn('sog_cda_cod',
        #                 relation_path='@rcrcg__id.@rc__id.@sog__cod.cdacod__cod',
        #                 # da inspector @rcrcg__id.@rc__id.@sog__cod.cdacod__cod
        #                 name_long='!![it]Piano CDA soggetto'
        #                 )

        tbl.aliasColumn('rc__id', '@rc_rcg__id.rc__id', 
                        name_long='!![it]RC id'
                        )

        tbl.formulaColumn('caption', '$desc',
                          name_long='!![it]Descrizione',
                          name_short='!![it]Desc'
                          )


    def trigger_onInserted(self, record=None):
        '''Ad inserimento riga, creazione movimenti di analitica'''

        self.rc_coa_cam_allinea(record)


    def trigger_onUpdated(self, record=None, old_record=None):
        '''Ad aggiornamento riga, modifica movimenti di analitica'''

        self.rc_coa_cam_allinea(record)


    def trigger_onDeleted(self, record=None):
        '''Ad aggiornamento riga, elimina movimenti di analitica'''

        self.rc_coa_cam_allinea(record)


    def rc_coa_cam_allinea(self, record=None):
        '''Allinea i movimenti di analitica in rccoacam al record rcrcgcda'''
        
        # si cancellano i record eventualmente gia' creati in precedenza
        self.rc_coa_cam_delete(record)

        # poi si creano i record nuovi necessari
        self.rc_coa_cam_insert(record)

    def rc_coa_cam_delete(self, record=None):
        '''Cancella movimenti analitica da rc_coa_cam
        
        Le righe che vengono eliminate sono, se esistenti,
        quelle precedentemente create dalla rc_coa_cam_insert.
        La corrispondenza cercata ha:
        rc__id: riferimento alla testata rc
        origine: id della riga rcrcg
        '''

        # prendo il record della riga contabile rc_rcg per ottenere
        # l'id della testata registrazione rc, nel campo rc_rcg__id
        rcrcg_record = self.db.table('pn.rc_rcg').record(
            record['rc_rcg__id']).output('record')
        
        #print(f'rc_rcg_record={rc_rcg_record}')
        #print(f"cancella righe, $rc__id=({rc_rcg_record['rc__id']}), $origine=({record['id']})")
        self.db.table('pn.rc_coa_cam').deleteSelection(
            where = '$rc__id = :pk_rc AND $origine = :pk_rc_rcg',
            pk_rc = rcrcg_record['rc__id'],
            pk_rc_rcg = record['id'],
            )
        self.db.commit()

    def rc_coa_cam_insert(self, record=None):
        '''Inserisce i movimenti analitica in rc_coa_cam'''

        #print(f"inserisci righe, record: {record}")
        # prendo il record della riga contabile rc_rcg per ottenere
        # l'id della testata registrazione rc, nel campo rc_rcg__id
        rcrcg_record = self.db.table('pn.rc_rcg').record(
            record['rc_rcg__id']
            ).output('record')
        
        # se non c'e' competenza iniziale assumo data documento
        # in subordine data registrazione
        if rcrcg_record['competenza_da']:
            competenza_da = str(rcrcg_record['competenza_da'])
        else:
            # recupero il record di testata
            rc_record = self.db.table('pn.rc').record(
                rcrcg_record['rc__id']
                ).output('record')
            # se c'e' la data documento prendo quella,
            # altrimenti prendo la data registrazione
            if rc_record['rc_docdata']:
                competenza_da = str(rc_record['rc_docdata'])
            else:
                competenza_da = str(rc_record['rc_data'])
        
        # se non c'e' competenza finale assumo uguale a iniziale
        if rcrcg_record['competenza_a']:
            competenza_a = str(rcrcg_record['competenza_a'])
        else:
            competenza_a = competenza_da

        #print(f"da: {competenza_da} a: {competenza_a}; D={record['dare_udc']} A={record['avere_udc']}")
        
        periodi_cam = competenza_AAAAMM(
            competenza_da,
            competenza_a,
            record['dare_udc'],
            record['avere_udc']
            )
        
        # print(periodi_cam)

        for periodo in periodi_cam:
            # record['nome_campo'] -> per accedere al campo di rcrcgcda
            rcrcgcda = dict(
                rc__id = rcrcg_record['rc__id'],  # rif. testata reg.
                origine = record['id'],     # record origine movimento
                origine_auto = FIRMA_AUTO_rc_rcg_cda,
                origine_desc = '',
                desc = record['desc'],
                pdc_cod__cod = rcrcg_record['pdc_cod__cod'],
                pdc_conti__cod = rcrcg_record['pdc_conti__cod'],
                cda_cod__cod = record['cda_cod__cod'],
                cda_centri__cod = record['cda_centri__cod'],
                pdv_cod__cod = rcrcg_record['pdv_cod__cod'],
                pdv_voci__cod = rcrcg_record['pdv_voci__cod'],
                dare_udc = periodo[1], # record['dare_udc'],
                avere_udc = periodo[2], # record['avere_udc'],
                competenza_am = periodo[0],
                divisioni__id = rcrcg_record['divisioni__id'],
                commesse__id = rcrcg_record['commesse__id'],
                )
            #print(f'INSERT: {rc_rcg_cda}')
            self.db.table('pn.rc_coa_cam').insert(rcrcgcda)

        if periodi_cam:
            self.db.commit()


    # def get_lista_cda(self, record):
    #     '''Restituisce la lista dei cda della riga contabile'''
    #
    #     query = self.db.table('pn.rc_rcg_cda').query(
    #         columns='*',
    #         where='$rc_rcg__id = :id_rc_rcg',
    #         id_rc_rcg = record['rc_rcg__id']
    #         ).fetch()
    #
    #     return(query)
