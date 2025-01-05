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
FIRMA_AUTO_rcrcgcom = 'pn.rcrcgcom'


class Table(object):
    def config_db(self, pkg):
        '''rcrcgcom: dettaglio commesse di una riga di registrazione contabile

        Questa tabella serve per dettagliare eventuali commesse di dettaglio
        di ciascuna riga contabile di una rilevazione contabile.
        Da questa verranno generati i movimenti di analitica.
        '''

        tbl = pkg.table('rcrcgcom', pkey='id', 
                        name_long="!![it]Comm. riga",
                        caption_field='caption')

        self.sysFields(tbl, counter='rcrcg__id')

        # foreign key to rcrcg - riga di riferimento
        rcrcg__id = tbl.column('rcrcg__id', dtype = 'A', size = '22',
                               name_long = '!![it]Riga contabile',
                               unmodifiable=True,
                               validate_notnull = True
                               )
        rcrcg__id.relation('pn.rcrcg.id', mode = 'foreignkey',
                           relation_name = 'commesse_rcg', 
                           onDelete = 'cascade'
                           )
        
        # foreing key to commessa - la commessa
        commessa__id = tbl.column('commessa__id', dtype='A', size='22',
                                  name_long = '!![it]Commessa',
                                  name_short = '!![it]Comm.',
                                  #unmodifiable=False,
                                  validate_notnull=True,
                                  )
        commessa__id.relation('pn.commessa.id', mode='foreignkey',
                               relation_name='commesse_riga',
                               #one_one=True,
                               onDelete='raise',
                               )

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione dettaglio commessa', 
                   )

        tbl.column('dare_udc', dtype='N', size='12,2',
                   name_long='!![it]Dare', name_short='!![it]D',
                   #validate_notnull=True,
                   )

        tbl.column('avere_udc', dtype='N', size='12,2',
                   name_long='!![it]Avere', name_short='!![it]A',
                   #validate_notnull=True,
                   )

        tbl.formulaColumn('saldo_udc', 'COALESCE($dare_udc, 0) - COALESCE($avere_udc, 0)',
                          dtype='N', size='12,2',
                          name_long='!![it]Saldo', name_short='!![it]S')

        tbl.formulaColumn('caption', '$desc',
                          name_long='!![it]Descrizione',
                          name_short='!![it]Desc')


    def trigger_onInserted(self, record=None):
        '''Ad inserimento riga, creazione movimenti di analitica'''

        self.rccoacam_allinea(record)


    def trigger_onUpdated(self, record=None, old_record=None):
        '''Ad aggiornamento riga, modifica movimenti di analitica'''

        self.rccoacam_allinea(record)


    def trigger_onDeleted(self, record=None):
        '''Ad aggiornamento riga, elimina movimenti di analitica'''

        self.rccoacam_allinea(record)


    def rccoacam_allinea(self, record=None):
        '''Allinea i movimenti di analitica in rccoacam al record rcrcgcom'''
        
        # si cancellano i record eventualmente gia' creati in precedenza
        self.rccoacam_delete(record)

        # poi si creano i record nuovi necessari
        self.rccoacam_insert(record)

    def rccoacam_delete(self, record=None):
        '''Cancella movimenti analitica da rccoacam
        
        Le righe che vengono eliminate sono, se esistenti,
        quelle precedentemente create dalla rccoacam_insert.
        La corrispondenza cercata ha:
        rc__id: riferimento alla testata rc
        origine: id della riga rcrcg
        '''

        # prendo il record della riga contabile rcrcg per ottenere
        # l'id della testata registrazione rc, nel campo rcrcg__id
        rcrcg_record = self.db.table('pn.rcrcg').record(
            record['rcrcg__id']).output('record')
        
        #print(f'rcrcg_record={rcrcg_record}')
        #print(f"cancella righe, $rc__id=({rcrcg_record['rc__id']}), $origine=({record['id']})")
        self.db.table('pn.rccoacam').deleteSelection(
            where = '$rc__id = :pk_rc AND $origine = :pk_rcrcg',
            pk_rc = rcrcg_record['rc__id'],
            pk_rcrcg = record['id'],
            )
        self.db.commit()

    def rccoacam_insert(self, record=None):
        '''Inserisce i movimenti analitica in rccoacam'''

        #print(f"inserisci righe, record: {record}")
        # prendo il record della riga contabile rcrcg per ottenere
        # l'id della testata registrazione rc, nel campo rcrcg__id
        rcrcg_record = self.db.table('pn.rcrcg').record(
            record['rcrcg__id']
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
            rcrcgcom = dict(
                rc__id = rcrcg_record['rc__id'],  # rif. testata reg.
                origine = record['id'],     # record origine movimento
                origine_auto = FIRMA_AUTO_rcrcgcom,
                origine_desc = '',
                desc = record['desc'],
                pdccod__cod = rcrcg_record['pdccod__cod'],
                pdcconto__id = rcrcg_record['pdcconto__id'],
                # questa parte varia tra centri e commesse
                #cdacod__cod = record['cdacod__cod'],
                #cdacentro__id = record['cdacentro__id'],
                commessa__id = record['commessa__id'],
                #
                pdvcod__cod = rcrcg_record['pdvcod__cod'],
                pdvvoce__id = rcrcg_record['pdvvoce__id'],
                dare_udc = periodo[1], # record['dare_udc'],
                avere_udc = periodo[2], # record['avere_udc'],
                competenza_am = periodo[0],
                divisione__id = rcrcg_record['divisione__id'],
                # attenzione, questa e' commessa di riga...
                #commessa__id = rcrcg_record['commessa__id'],
                )
            #print(f'INSERT: {rcrcgcda}')
            self.db.table('pn.rccoacam').insert(rcrcgcom)

        if periodi_cam:
            self.db.commit()
