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
        '''rcrcg: rilevazione contabile - riga contabilita' generale

        Righe rilevazioni contabili        
        '''

        tbl = pkg.table('rcrcg', pkey='id', 
                        pkey_columns='rc__id,riga_numero',
                        name_long="!![it]Riga contabilita' generale",
                        name_plural="!![it]Righe contabilita' generale",
                        caption_field='caption')

        self.sysFields(tbl)

        #
        # TO DO: PK COMPOSITA
        #
        # La PK corretta di questa tabella e':
        # rc__id
        # riga_numero
        #

        # foreign key to rc - testata registrazione
        rc__id = tbl.column('rc__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Testata',
                                    unmodifiable=True,
                                    validate_notnull = True
                                    )
        rc__id.relation('pn.rc.id', mode = 'foreignkey',
                                relation_name = 'righe_registrazione', 
                                onDelete = 'cascade')
        
        tbl.column('riga_numero', dtype='N',
                   unmodifiable=True,
                   name_long='!![it]Progressivo riga',
                   validate_notnull=True
                   )

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione rilevazione', 
                   )

        tbl.column('dare_udc', dtype='N', size='12,2',
                   name_long='!![it]Dare',
                   #validate_notnull=True,
                   )

        tbl.column('avere_udc', dtype='N', size='12,2',
                   name_long='!![it]Avere',
                   #validate_notnull=True,
                   )

        tbl.formulaColumn('caption', "$riga_numero",
                          name_long='!![it]Rif. reg.')

