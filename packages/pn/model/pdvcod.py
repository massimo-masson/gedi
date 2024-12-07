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
        '''pdvcod: codice dello schema del piano delle voci analitico
        
        Conto si riferisce al conto del piano dei conti di contabilita' generale.
        Voce si riferisce alla voce del piano delle voci di contabilita' analitica.
        E' possibile avere piu' di un piano delle voci.
        Il raggruppamento delle voci fa riferimento al codice definito in pdvcod

        In relazione 1:n con la tabella pdvvoce, che contiene i record dello 
        specifico piano delle voci
        '''

        tbl = pkg.table('pdvcod', pkey='cod', 
                        name_long='!![it]Piano delle voci',
                        name_plural='!![it]Piani delle voci',
                        caption_field='caption')

        self.sysFields(tbl, id=False)

        tbl.column('cod', dtype='A', size=':32', 
                   name_long='!![it]Codice piano delle voci',
                   unmodifiable=True,
                   unique=True, validate_notnull=True, indexed=True)

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione pdv', 
                   validate_notnull=True)

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note')

        tbl.formulaColumn('caption', "$cod||' - '||$desc",
                          name_long='!![it]Codice - Descrizione')
