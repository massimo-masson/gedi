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

import math

class Table(object):
    def config_db(self, pkg):
        '''cli: anagrafica clienti'''

        tbl = pkg.table('cli', pkey='id',
                        pkey_columns='sog__cod,cod',
                        name_long='!![it]Cliente',
                        name_plural='!![it]Clienti',
                        caption_field='caption')

        self.sysFields(tbl)

        #
        # TO DO: PK COMPOSITA
        #
        # La PK corretta di questa tabella e':
        # sog__cod
        # cod
        #

        # foreign key to sog.cod - soggetto cui questo gruppo di riferimento appartiene
        sog__cod = tbl.column('sog__cod', dtype = 'A', size = ':32',
                              name_long = '!![it]Soggetto di riferimento',
                              unmodifiable=True,
                              validate_notnull = True,
                              )
        sog__cod.relation('pn.sog.cod', mode = 'foreignkey',
                          relation_name = 'clienti_cli', 
                          onDelete = 'raise')
        
        #
        # se utente inserisce un codice, usa quello
        # in combinazione con sog__cod.
        # Altrimenti calcola un progressivo.
        # unmodifiable=True: e' PK, non si puo' cambiare poi
        # validate_notnull=False: a mano puo' restare vuoto
        #
        tbl.column('cod', dtype='A', size=':32', 
                   name_long='!![it]Codice',
                   unmodifiable=True, #unique=True, 
                   #validate_notnull=True,
                   #indexed=True,
                   )

        tbl.column('codesterno', dtype='A', size=':32', 
                   name_long='!![it]Codice esterno',
                   )

        tbl.column('denominazione', dtype='A', size=':256', 
                   name_long='!![it]denominazione', 
                   )

        tbl.column('codicefiscale', dtype='A', size=':16', 
                   name_long='!![it]Codice Fiscale',
                   name_short='!![it]CF',
                   #validate_notnull=True,
                   )

        tbl.column('partitaiva', dtype='A', size=':13', 
                   name_long='!![it]Partita IVA',
                   name_short='!![it]PIVA',
                   #validate_notnull=True,
                   )

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note')

        tbl.formulaColumn('caption', "'C-'||$cod||' - '||$denominazione",
                          name_long='!![it]Titolo')


    def pkeyValue(self, record):
        '''Restituisce la pk "composta": sog__cod + cod
        
        Il valore di sog__cod viene preso dalla relazione, non modificato.
        Il valore di cod viene:
            - se e' stato inserito dall'utente, MANTENUTO
            - se vuoto, viene calcolato il progressivo successivo
              guardando i campi di tipo numerico.

        ### TODO ###
        da rivedere al passaggio a chiavi composte
        '''

        # se non viene indicato un codice esplicito, progressivo + 1
        if not record['cod']:
            q = self.db.table('anag.cli').query(
                # conversone in numero
                columns = 'MAX(CAST($cod AS REAL)) AS cod',
                # delle righe che contengono solo numeri (regex)
                where = "($sog__cod=:SOG) AND ($cod NOT LIKE '%[^0-9.]%')",
                SOG = record['sog__cod']
                )
            f = q.fetch()

            try:
                # arrotonda per eccesso
                progr = math.ceil(float(f[0]['cod']))
            except (ValueError, TypeError):
                # o parti da 0
                progr = 0
            # componente cod della pk e' il numero successivo
            record['cod'] = str(progr + 1)

            #print(f"record cod aggiornato a {record['cod']}")
        #print(record)

        # restituzione PK formata da sog__cod + cod
        return(record['sog__cod'] + record['cod'])