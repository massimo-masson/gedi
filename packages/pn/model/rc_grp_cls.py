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
        '''rc_grp_cls: registrazione contabile - classi per gruppi registrazione
        
        E' possibile definire una classe di appartenenza per un
        gruppo di registrazione.
        Il gruppo di registrazione in tal modo potra' acquisire i parametri
        caratterizzanti la classe
        '''

        tbl = pkg.table('rc_grp_cls', pkey='cod', 
                        name_long='!![it]Classe gruppo registrazione',
                        name_plural='!![it]Classe gruppi registrazione',
                        caption_field='desc'
                        )

        self.sysFields(tbl, id=False)

        tbl.column('cod', dtype='A', size=':32', 
                   name_long='!![it]Codice classe gruppo registrazione',
                   unmodifiable=True,
                   unique=True, 
                   validate_notnull=True, 
                   indexed=True
                   )

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione classe', 
                   validate_notnull=True
                   )

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note'
                   )
