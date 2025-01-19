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


from sottoconto import tipi_sottoconto


class Table(object):
    def config_db(self, pkg):
        '''rcrcg: rilevazione contabile - riga contabilita' generale

        Righe rilevazioni contabili        
        '''

        tbl = pkg.table('rcrcg', pkey='id', 
                        #pkey_columns='rc__id,riga_numero', # 20241226 CANCELLARE
                        #pkey_columns='rc__id', # 20250102 CANCELLARE
                        name_long="!![it]Riga contabilita' generale",
                        name_plural="!![it]Righe contabilita' generale",
                        caption_field='caption')

        self.sysFields(tbl, counter='rc__id')

        # foreign key to rc - testata registrazione
        rc__id = tbl.column('rc__id', dtype = 'A', size = '22',
                            name_long = '!![it]Testata',
                            unmodifiable=True,
                            validate_notnull = True
                            )
        rc__id.relation('pn.rc.id', mode = 'foreignkey',
                        relation_name = 'righe_registrazione', 
                        onDelete = 'cascade')
        
        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione rilevazione', 
                   )

        # foreign key to pdccod - piano dei conti di riferimento
        pdccod__cod = tbl.column('pdccod__cod', dtype = 'A', size = ':32',
                                 defaultFrom='@rc__id.@sog__cod.pdccod__cod',
                                 name_long = '!![it]PDC',
                                 #unmodifiable=True,
                                 validate_notnull = True
                                 )
        pdccod__cod.relation('pn.pdccod.cod', mode = 'foreignkey',
                             relation_name = 'pdc_registrazione', 
                             onDelete = 'raise')
        
        # foreign key to pdcconto - conto
        pdcconto__id = tbl.column('pdcconto__id', dtype = 'A', size = '22',
                                  name_long = '!![it]Conto',
                                  #unmodifiable=True,
                                  validate_notnull = True
                                  )
        pdcconto__id.relation('pn.pdcconto.id', mode = 'foreignkey',
                              relation_name = 'conto_registrazione', 
                              onDelete = 'raise')

        # sottoconto, tipo e specifiche relazioni
        tbl.column('sottoconto_tipo', dtype='A', size=':32',
                   values = tipi_sottoconto(),
                   name_long = '!![it]Tipo sottoconto',
                   name_short = '!![it]Tipo s.c.',
                   )
        # tbl.aliasColumn('sottoconto_tipo', relation_path='@pdcconto__id.sottoconto_tipo',
        #             name_long = '!![it]Tipo sottoconto',
        #             )

        # polimorfico: relazione con anag.cli.id, caso sottoconto_tipo=cli
        sottoconto_cli = tbl.column('anagcli__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Cliente',
                                    )
        sottoconto_cli.relation('anag.cli.id', mode = 'foreignkey',
                                relation_name = 'sottoconti_cli_rcrcg', 
                                onDelete = 'raise')

        # polimorfico: relazione con anag.for.id, caso sottoconto_tipo=for
        sottoconto_for = tbl.column('anagfor__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Fornitore',
                                    )
        sottoconto_for.relation('anag.for.id', mode = 'foreignkey',
                                relation_name = 'sottoconti_for_rcrcg', 
                                onDelete = 'raise')

        # polimorfico: relazione con anag.banche.id, caso sottoconto_tipo=banche
        sottoconto_for = tbl.column('anagbanche__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Banche',
                                    )
        sottoconto_for.relation('anag.banche.id', mode = 'foreignkey',
                                relation_name = 'sottoconti_banche_rcrcg', 
                                onDelete = 'raise')

        # sezione importi
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

        tbl.column('competenza_da', dtype='D',
                   name_long='!![it]Competenza da',
                   name_short='!![it]Comp.da'
                   )

        tbl.column('competenza_a', dtype='D',
                   name_long='!![it]Competenza a',
                   name_short='!![it]Comp.a'
                   )

        # foreing key to pdvcod - codice piano delle voci
        pdvcod__cod = tbl.column('pdvcod__cod', dtype='A', size=':32',
                                 defaultFrom='@rc__id.@sog__cod.pdvcod__cod',
                                 name_long = '!![it]PDV cod.',
                                 #unmodifiable=False,
                                 validate_notnull=True,
                                 )
        pdvcod__cod.relation('pn.pdvcod.cod', mode='foreignkey',
                             relation_name='pdvcod_rcrcg',
                             onDelete='raise'
                             )

        # foreing key to pdvvoce - la voce di analisi
        pdvvoce__id = tbl.column('pdvvoce__id', dtype='A', size='22',
                                 name_long = '!![it]Voce',
                                 #unmodifiable=False,
                                 # validate_notnull=True,
                                 )
        pdvvoce__id.relation('pn.pdvvoce.id', mode='foreignkey',
                               relation_name='pdvvoce_rcrcg',
                               #one_one=True,
                               onDelete='raise'
                               )

        # foreign key to divisione: default quella della testata registrazione
        divisione__id = tbl.column('divisione__id', dtype = 'A', size = '22',
                                   name_long = '!![it]Divisione', 
                                   name_short='!![it]Div',
                                   defaultFrom='@rc__id.divisione__id',
                                   #unmodifiable=True,
                                   validate_notnull = False
                                   )
        divisione__id.relation('pn.divisione.id', mode = 'foreignkey',
                               relation_name = 'divisione_riga', 
                               onDelete = 'raise')
        
        tbl.aliasColumn('divisione_rc', '@rc__id.divisione__id',
                        name_long='!![it]Divisione testata reg.',
                        name_short='!![it]Div.tes.',
                        )

        # foreign key to commessa: default quella della testata registrazione
        commessa__id = tbl.column('commessa__id', dtype = 'A', size = '22',
                                  name_long = '!![it]Commessa', 
                                  name_short='!![it]Comm',
                                  defaultFrom='@rc__id.commessa__id',
                                  #unmodifiable=True,
                                  validate_notnull = False
                                  )
        commessa__id.relation('pn.commessa.id', mode = 'foreignkey',
                               relation_name = 'commessa_riga', 
                               onDelete = 'raise')

        tbl.aliasColumn('commessa_rc', '@rc__id.commessa__id',
                        name_long='!![it]Commessa testata reg.',
                        name_short='!![it]Comm.tes.',
                        )

        tbl.formulaColumn('caption', "$_row_count",
                          name_long='!![it]Riga')


    def coa_update_da_rielaborare(self, record=None, old_record=None):
        '''Restituisce true se la modifica implica ricalcolo'''
        
        modificare = False
        
        #if record[''] != old_record['']: modificare = True
        if record['pdccod__cod'] != old_record['pdccod__cod']: modificare = True
        if record['pdcconto__id'] != old_record['pdcconto__id']: modificare = True
        if record['competenza_da'] != old_record['competenza_da']: modificare = True
        if record['competenza_a'] != old_record['competenza_a']: modificare = True
        if record['pdvcod__cod'] != old_record['pdvcod__cod']: modificare = True
        if record['pdvvoce__id'] != old_record['pdvvoce__id']: modificare = True
        if record['divisione__id'] != old_record['divisione__id']: modificare = True
        if record['commessa__id'] != old_record['commessa__id']: modificare = True

        #if modificare: print("ricalcola analitica:", record)
        
        return modificare
    

    def trigger_onUpdated(self, record=None, old_record=None):
        '''Ad aggiornamento riga, modifica movimenti di analitica
        
        Se la modifica riguarda elementi che impattano sul
        calcolo delle competenze, rigenera le righe analitiche 
        dei cda e comesse
        '''

        if self.coa_update_da_rielaborare(record, old_record):
            self.rielabora_lista_cda(record)
            self.rielabora_lista_com(record)


    def get_lista_cda(self, record):
        '''Restituisce la lista cda della riga contabile'''
        
        query = self.db.table('pn.rcrcgcda').query(
            columns='*',
            where='$rcrcg__id = :id_rcrcg',
            id_rcrcg = record['id']
            ).fetch()
        
        return(query)


    def get_lista_com(self, record):
        '''Restituisce la lista commesse della riga contabile'''
        
        query = self.db.table('pn.rcrcgcom').query(
            columns='*',
            where='$rcrcg__id = :id_rcrcg',
            id_rcrcg = record['id']
            ).fetch()
        
        return(query)
    

    def rielabora_lista_cda(self, record):
        '''Rielabora la lista cda del record rcrcg'''

        lista_cda = self.get_lista_cda(record)

        for cda in lista_cda:
            tbl = self.db.table('pn.rcrcgcda')
            tbl.rccoacam_allinea(cda)


    def rielabora_lista_com(self, record):
        '''Rielabora la lista commesse del record rcrcg'''

        lista_com = self.get_lista_com(record)

        for com in lista_com:
            tbl = self.db.table('pn.rcrcgcom')
            tbl.rccoacam_allinea(com)