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
        '''iva_naturacodici: natura dei codici IVA in fattura elettronica
        
        Ai fini della fatturazione elettronica i codici IVA su cui non 
        si applica l'IVA devono avere un codice che rappresenta la nautra IVA.
        Ad esempio:
            N1   "escluse ex art. 15"
            N2.1 "non soggette ex artt. 7 - 7-septies DPR 633/72"
            N2.2 "non soggette - altri casi"
            ...
        '''

        tbl = pkg.table('iva_naturacodici', pkey='cod', 
                        name_long='!![it]Natura codice IVA',
                        name_plural='!![it]Natura codici IVA',
                        caption_field='coddesc')

        self.sysFields(tbl, id=False)

        tbl.column('cod', dtype='A', size=':16', 
                   name_long='!![it]Codice natura IVA',
                   unmodifiable=True,
                   unique=True, validate_notnull=True, indexed=True)

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione codice', 
                   validate_notnull=True)

        tbl.column('valido_dal', dtype='D',
                   name_long = "!![it]Data inizio validita'")

        tbl.column('valido_al', dtype='D',
                   name_long = "!![it]Data fine validita'")

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note')
        
        tbl.formulaColumn('coddesc', "$cod||' - '||$desc",
                          name_long='!![it]Codice - Descrizione')
