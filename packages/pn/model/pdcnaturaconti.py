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
        '''pdcnaturaconti: tabella per definizione della natura dei conti'''

        tbl = pkg.table('pdcnaturaconti', pkey='id', 
                        name_long='!![it]Natura conti',
                        #name_plural='!![it]Tassonomia',
                        caption_field='cod')

        self.sysFields(tbl, hierarchical='cod')

        tbl.column('cod', dtype='A', size=':22', 
                   name_long='!![it]Codice natura',
                   unmodifiable=True,
                   unique=True, validate_notnull=True, indexed=True)

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione tassonomia', 
                   validate_notnull=True)

        tbl.column('epilogo', dtype='A', size=':16', 
                   name_long='!![it]Sezione epilogo chiusura conti', 
                   validate_notnull=True)

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note')
