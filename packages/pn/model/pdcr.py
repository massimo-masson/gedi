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
        '''pdcr: conto di uno dei piani dei conti
        
        Un conto appartiene ad un piano dei conti, in relazione 1:n.
        il codice e' libero ed esteso, pensato per importare conti da altri sistemi
        senza particolari vincoli.

        Epilogo: serve per determinare la chiusura dei conti, puo' essere:
                CE epilogo a Conto Economico
                SP epilogo a Stato Patrimoniale

        Tipo dettaglio: il conto puo' avere un dettaglio ulteriore, ad esempio
        un codice di anagrafica. Esempio: il conto "clienti" dettaglia il codice
        del cliente nel dettaglio. "Clienti" e' il tipo dettaglio

        Dettaglio conto: una volta definito il "tipo dettaglio", il dettaglio
        rappresenta l'anagrafica di riferimento per dettagliare quello specifico conto.
        '''

        tbl = pkg.table('pdcr', pkey='id', 
                        pkey_columns='pdccod__cod,cod',
                        name_long='!![it]Conto',
                        name_plural='!![it]Conti',
                        caption_field='coddesc')

        self.sysFields(tbl)

        #
        # TO DO: PK COMPOSITA
        #
        # La PK corretta di questa tabella e':
        # pdccod__id
        # cod
        #

        tbl.column('cod', dtype='A', size=':64', 
                   name_long='!![it]Codice conto',
                   unmodifiable=True,
                   validate_notnull=True,
                   #unique=True, 
                   #indexed=True,
                   )

        # pdccod__id: foreign key to pdccod
        tbl_pdccod__cod = tbl.column('pdccod__cod', dtype = 'A', size = ':32',
                                    name_long = '!![it]PDC di riferimento',
                                    unmodifiable=True,
                                    validate_notnull = True
                                    )
        tbl_pdccod__cod.relation('pn.pdccod.cod', mode = 'foreignkey',
                                relation_name = 'conti_pdc', 
                                onDelete = 'raise')

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione conto', 
                   validate_notnull=True)

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note')

        # codice conto epilogo per chiusura e riapertura
        tbl.column('cod_epilogo', dtype='A', size=':16', 
                   name_long='!![it]Epilogo chiusura conto')

        # pdcnaturaconto__id: foreign key to naturaconto
        tbl_pdcnaturaconto__id = tbl.column('pdcnaturaconti__id', dtype = 'A', size = '22',
                                    name_long = '!![it]natura del conto',
                                    #validate_notnull = True
                                    )
        tbl_pdcnaturaconto__id.relation('pn.pdcnaturaconti.id', mode = 'foreignkey',
                                relation_name = 'epilogo_conti', 
                                onDelete = 'raise')
        
        tbl.formulaColumn('coddesc', "$cod||' - '||$desc",
                          name_long='!![it]Codice - Descrizione')