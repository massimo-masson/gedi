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

class Table(object):
    def config_db(self, pkg):
        '''rc: rilevazione contabile (accounting journal) testata

        Testata delle rilevazioni contabili, cui tutte le tabelle
        di movimento contabile e relativo dettaglio faranno riferimento.        
        '''

        tbl = pkg.table('rc', pkey='id', 
                        #pkey_columns='sog__cod,rc_rif',
                        #pkey_columns='sog__cod,rc_rif,id',
                        #pkey_columns='id,sog__cod',
                        partition_sog__cod='sog__cod',
                        name_long='!![it]Rilevazione contabile',
                        name_plural='!![it]Rilevazioni contabili',
                        caption_field='caption')

        self.sysFields(tbl)

        #
        # TO DO: PK COMPOSITA
        #
        # La PK corretta di questa tabella e':
        # sog__cod
        # rc_rif
        #

        # foreign key to sog.cod - soggetto cui questo gruppo di riferimento appartiene
        sog__cod = tbl.column('sog__cod', dtype = 'A', size = ':32',
                              name_long = '!![it]Soggetto di riferimento',
                              unmodifiable=True,
                              validate_notnull = True
                              )
        sog__cod.relation('pn.sog.cod', mode = 'foreignkey',
                          relation_name = 'rilevazioni_contabili', 
                          onDelete = 'raise')
        
        # foreign key to esercizio
        esercizio__id = tbl.column('esercizio__id', dtype = 'A', size = '22',
                                     name_long = '!![it]Esercizio',
                                     validate_notnull = True
                                     )
        esercizio__id.relation('pn.sogesercizi.id', mode = 'foreignkey',
                                relation_name = 'registrazioni_esercizio', 
                                onDelete = 'raise')

        # foreign key to rcgrp - gruppo di registrazione di questa rilevazione
        rcgrp__id = tbl.column('rcgrp__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Gruppo registrazioni',
                                    validate_notnull = True,
                                    )
        rcgrp__id.relation('pn.rcgrp.id', mode = 'foreignkey',
                                relation_name = 'registrazioni_gruppo', 
                                onDelete = 'raise')

        # foreign key to ivaregistro - eventuale registro iva
        ivaregistro__id = tbl.column('ivaregistro__id', dtype = 'A', size = '22',
                                     name_long = '!![it]Registro IVA',
                                     #validate_notnull = True
                                     )
        ivaregistro__id.relation('pn.ivaregistro.id', mode = 'foreignkey',
                                relation_name = 'registrazioni_ivaregistro', 
                                onDelete = 'raise')

        # foreign key to divisione - eventuale divisione
        divisione__id = tbl.column('divisione__id', dtype = 'A', size = '22',
                                     name_long = '!![it]Divisione',
                                     #validate_notnull = True
                                     )
        divisione__id.relation('pn.divisione.id', mode = 'foreignkey',
                                relation_name = 'registrazioni_divisione', 
                                onDelete = 'raise')

        # foreign key to commessa - eventuale commessa di testata
        commessa__id = tbl.column('commessa__id', dtype = 'A', size = '22',
                                     name_long = '!![it]Commessa',
                                     #validate_notnull = True
                                     )
        commessa__id.relation('pn.commessa.id', mode = 'foreignkey',
                                relation_name = 'registrazioni_commesse', 
                                onDelete = 'raise')

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione rilevazione', 
                   #validate_notnull=True
                   )

        tbl.column('rc_data', dtype='D',
                   name_long='!![it]Data registrazione',
                   validate_notnull=True
                   )

        #
        # TO DO: rimettere validate_notnull=True
        # magari con un default autoincrementante
        #
        tbl.column('rc_rif', dtype='A', size=':128',
                   name_long='!![it]Riferimento registrazione',
                   name_short='!![it]Rif.reg.',
                   #validate_notnull=True
                   )
        
        tbl.column('rc_docdata', dtype='D',
                   name_long='!![it]Data documento',
                   name_short='!![it]Data doc.',
                   )

        tbl.column('rc_docnum', dtype='A', size=':64', 
                   name_long='!![it]Numero documento',
                   name_short='!![it]Num.doc.',
                   )

        tbl.column('iva_protocollo', dtype='N',
                   name_long='!![it]Protocollo',
                   name_short='!![it]Prot.')
        
        tbl.column('iva_protocollo_appendice', dtype='A', size=':32',
                   name_long='!![it]Appendice',
                   name_short='!![it]Pr.app.')
        
        # tbl.column('note', dtype='A', size=':1024', 
        #            name_long='!![it]Note')

        tbl.formulaColumn('caption', "$rc_data||' - '||$rc_rif",
                          name_long='!![it]data-num')
        
        # formule riepilogo COGE
        tbl.formulaColumn('tot_dare_udc', dtype='N', 
                          name_long='!![it]Totale Dare',
                          select=dict(table='pn.rcrcg',
                                      columns='SUM($dare_udc)',
                                      where='$rc__id=#THIS.id'
                                      )
                          )

        tbl.formulaColumn('tot_avere_udc', dtype='N', 
                          name_long='!![it]Totale Avere',
                          select=dict(table='pn.rcrcg',
                                      columns='SUM($avere_udc)',
                                      where='$rc__id=#THIS.id'
                                      )
                          )

        tbl.formulaColumn('numero_righe_coge', dtype='N', 
                          name_long='!![it]Numero righe',
                          select=dict(table='pn.rcrcg',
                                      columns='COUNT($rc__id)',
                                      where='$rc__id=#THIS.id'
                                      )
                          )

        # formule riepilogo CDA
        tbl.formulaColumn('tot_cda_dare_udc', dtype='N', 
                          name_long='!![it]Totale Dare CDA',
                          select=dict(table='pn.rcrcgcda',
                                      columns='COALESCE(SUM($dare_udc), 0)',
                                      where='@rcrcg__id.rc__id=#THIS.id'
                                      )
                          )

        tbl.formulaColumn('tot_cda_avere_udc', dtype='N', 
                          name_long='!![it]Totale Avere CDA',
                          select=dict(table='pn.rcrcgcda',
                                      columns='COALESCE(SUM($avere_udc), 0)',
                                      where='@rcrcg__id.rc__id=#THIS.id'
                                      )
                          )

        tbl.formulaColumn('numero_cda_movimentati', dtype='N', 
                          name_long='!![it]Numero CDA movimentati',
                          select=dict(table='pn.rcrcgcda',
                                      columns='COUNT(DISTINCT $cdacentro__id)',
                                      where='@rcrcg__id.rc__id=#THIS.id'
                                      )
                          )
        
        tbl.formulaColumn('diff_coge_cda_dare', '$tot_dare_udc - $tot_cda_dare_udc',
                          dtype='N',
                          name_long='!![it]Squadratura centri Dare'
                          )

        tbl.formulaColumn('diff_coge_cda_avere', '$tot_avere_udc - $tot_cda_avere_udc',
                          dtype='N',
                          name_long='!![it]Squadratura centri Avere'
                          )

        # formule riepilogo commesse
        tbl.formulaColumn('tot_com_dare_udc', dtype='N', 
                          name_long='!![it]Totale Dare commesse',
                          select=dict(table='pn.rcrcgcom',
                                      columns='COALESCE(SUM($dare_udc), 0)',
                                      where='@rcrcg__id.rc__id=#THIS.id'
                                      )
                          )

        tbl.formulaColumn('tot_com_avere_udc', dtype='N', 
                          name_long='!![it]Totale Avere commesse',
                          select=dict(table='pn.rcrcgcom',
                                      columns='COALESCE(SUM($avere_udc), 0)',
                                      where='@rcrcg__id.rc__id=#THIS.id'
                                      )
                          )

        tbl.formulaColumn('numero_com_movimentate', dtype='N', 
                          name_long='!![it]Numero commesse movimentate',
                          select=dict(table='pn.rcrcgcom',
                                      columns='COUNT(DISTINCT $commessa__id)',
                                      where='@rcrcg__id.rc__id=#THIS.id'
                                      )
                          )
        
        tbl.formulaColumn('diff_coge_com_dare', '$tot_dare_udc - $tot_com_dare_udc',
                          dtype='N',
                          name_long='!![it]Squadratura Commesse Dare'
                          )

        tbl.formulaColumn('diff_coge_com_avere', '$tot_avere_udc - $tot_com_avere_udc',
                          dtype='N',
                          name_long='!![it]Squadratura Commesse Avere'
                          )


    def defaultValues(self):
        '''Valore di default per nuovi inserimenti in partizione attiva'''

        return dict(sog__cod = self.db.currentEnv.get('current_sog__cod'),
                    rc_data  = self.db.workdate,
                    )
    

    def protect_validate(self, record, old_record, **kwargs):
        '''Validazione salvataggio registrazione contabile
        
        1) controllo totale DARE = totale AVERE
        '''

        query = self.db.table('pn.rcrcg').query(
            columns='COALESCE(SUM($dare_udc), 0) AS DARE, COALESCE(SUM($avere_udc), 0) AS AVERE',
            where='$rc__id = :id_corrente',
            id_corrente = record['id']
            ).fetch()
        #print(query)

        if not (query[0]['DARE'] == query[0]['AVERE']):
            raise self.exception('protect_update', record=record,
                msg='!![it]totali DARE e AVERE diversi!'
                )


    def counter_rc_rif(self, record=None):
        '''contatore progressivo RC'''
        
        return dict(format='$K-$NNNNNNN', #format='$K$YYYY$MM$DD/$NNNNNNN',
                    code=record['sog__cod'],
                    date_field='rc_data',
                    showOnLoad=True,
                    recycle=False
                    )

    
    # def protect_validate(self, record):
    #     '''Simula la protezione da chiave composta duplicata'''

    #     #
    #     # pk composta di questa tabella:
    #     # sog__cod
    #     # rc_rif
    #     #
    #     print('sog__cod', record['sog__cod'])
    #     print('rc_rif', record['rc_rif'])

    #     t = self.db.table('pn.rc')
    #     q = t.query(#columns='$sog__cod, $rc_rif',
    #                 where='$sog__cod=:soggetto,$rc_rif=:riferimento',
    #                 soggetto=record['sog__cod'],
    #                 riferimento='RC20241208/0000001' #record['rc_rif']
    #                 )
    #     f = q.fetch()

    #     if f:
    #         raise self.exception('protect_update', record=record,
    #                              msg='Chiave duplicata in rc')
