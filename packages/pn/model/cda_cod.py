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
        '''cda_cod: codici degli schemi dei piani dei centri di analisi
        
        Il centro di analisi e' l'entita' deputata alla rilevazione delle
        componenti economico/finanziarie per destinazione.

        In relazione 1:n con la tabella cdacentri, che contiene i record
        dello specifico piano dei centri di analisi.

        Questa tabella e' generale: non collegata ad uno specifico SOG
        Di conseguenza, diversi SOG possono usare (condividere) i medesimi
        piani dei centri di analisi.
        '''

        tbl = pkg.table('cda_cod', pkey='cod', 
                        name_long='!![it]Piano dei centri',
                        name_plural='!![it]Piani dei centri',
                        caption_field='caption')

        self.sysFields(tbl, id=False)

        tbl.column('cod', dtype='A', size=':32', 
                   name_long='!![it]Codice piano dei centri',
                   unmodifiable=True,
                   unique=True,
                   validate_notnull=True,
                   indexed=True
                   )

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione centro', 
                   validate_notnull=False
                   )

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note'
                   )

        tbl.formulaColumn('caption', "$cod||' - '||$desc",
                          name_long='!![it]Codice - Descrizione'
                          )
