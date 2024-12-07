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
        '''pdvvoce: voce di uno dei piani delle voci
        
        Una voce appartiene ad un piano delle voci, in relazione 1:n.
        il codice e' libero ed esteso, pensato per importare voci da altri sistemi
        senza particolari vincoli.
        '''

        tbl = pkg.table('pdvvoce', pkey='id', 
                        pkey_columns='pdvcod__cod,cod',
                        name_long='!![it]Voce',
                        name_plural='!![it]Voci',
                        caption_field='caption')

        self.sysFields(tbl)

        #
        # TO DO: PK COMPOSITA
        #
        # La PK corretta di questa tabella e':
        # pdvcod__cod
        # cod
        #

        tbl.column('cod', dtype='A', size=':64', 
                   name_long='!![it]Codice voce',
                   unmodifiable=True,
                   validate_notnull=True,
                   #unique=True, 
                   #indexed=True,
                   )

        # pdvcod__id: foreign key to pdvcod
        tbl_pdvcod__cod = tbl.column('pdvcod__cod', dtype = 'A', size = ':32',
                                    name_long = '!![it]PDV di riferimento',
                                    unmodifiable=True,
                                    validate_notnull = True
                                    )
        tbl_pdvcod__cod.relation('pn.pdvcod.cod', mode = 'foreignkey',
                                relation_name = 'voci_pdv', 
                                onDelete = 'raise')

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione voce', 
                   validate_notnull=True)

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note')

        tbl.formulaColumn('caption', "$cod||' - '||$desc",
                          name_long='!![it]Codice - Descrizione')
        