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
        '''sog: soggetti operativi nel db (multiditta)'''

        tbl = pkg.table('sog', pkey='cod', 
                        name_long='!![it]Soggetto operativo',
                        name_plural='!![it]Soggetti operativi',
                        caption_field='desc'
                        )

        self.sysFields(tbl, id=False)

        tbl.column('cod', dtype='A', size=':32', 
                   name_long='!![it]Soggetto operativo',
                   unmodifiable=True,
                   unique=True,
                   validate_notnull=True,
                   indexed=True
                   )

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione', 
                   validate_notnull=True
                   )

        tbl.column('note', dtype='A', size=':1024', 
                   name_long='!![it]Note'
                   )
        
        # pdc_cod__id: foreign key to pdc_cod
        pdc_cod__cod = tbl.column('pdc_cod__cod', dtype = 'A', size = ':32',
                                  name_long = '!![it]PDC',
                                  #unmodifiable=True,
                                  validate_notnull = True
                                  )
        pdc_cod__cod.relation('pn.pdc_cod.cod', mode = 'foreignkey',
                              relation_name = 'pdccod', 
                              one_one=True,
                              onDelete = 'raise'
                              )

        # pdv_cod__cod: foreign key to pdv_cod
        pdv_cod__cod = tbl.column('pdv_cod__cod', dtype = 'A', size = ':32',
                                  name_long = '!![it]PDV',
                                  #unmodifiable=True,
                                  validate_notnull = False
                                  )
        pdv_cod__cod.relation('pn.pdv_cod.cod', mode = 'foreignkey',
                              relation_name = 'pdvcod', 
                              one_one=True,
                              onDelete = 'raise'
                              )

        # cda_cod__cod: foreign key to cdacod
        cda_cod__cod = tbl.column('cda_cod__cod', dtype = 'A', size = ':32',
                                  name_long = '!![it]CDA',
                                  #unmodifiable=True,
                                  validate_notnull = False
                                  )
        cda_cod__cod.relation('pn.cda_cod.cod', mode = 'foreignkey',
                              relation_name = 'cdacod', 
                              one_one=True,
                              onDelete = 'raise'
                              )


    def partitioning_pkeys(self):
        '''Lista dei soggetti per il partizionamento'''
        where = None

        soggetti = [r['pkey'] for r in self.query(where=where).fetch()]
        return soggetti
