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
        '''for: anagrafica fornitori
        
        '''

        tbl = pkg.table('for', pkey='id', 
                        name_long='!![it]Fornitore',
                        name_plural='!![it]Fornitori',
                        caption_field='caption')

        self.sysFields(tbl)

        tbl.column('cod', dtype='A', size=':32',
                   name_long='!![it]Codice',
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

        tbl.formulaColumn('caption', "$cod||' - '||$denominazione",
                          name_long='!![it]Titolo')
