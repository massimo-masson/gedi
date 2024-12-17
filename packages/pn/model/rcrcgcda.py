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
        '''rcrcgcda: dettaglio centri di una riga di registrazione contabili

        Questa tabella serve per dettagliare i centri di analisi di ciascuna
        riga contabile di una rilevazione contabile.
        Da questa verranno generati i movimenti di analitica.
        '''

        tbl = pkg.table('rcrcgcda', pkey='id', 
                        name_long="!![it]CDA riga",
                        caption_field='caption')

        self.sysFields(tbl)

        # foreign key to rcrcg - riga di riferimento
        rcrcg__id = tbl.column('rcrcg__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Riga contabile',
                                    unmodifiable=True,
                                    validate_notnull = True
                                    )
        rcrcg__id.relation('pn.rcrcg.id', mode = 'foreignkey',
                                relation_name = 'cda_rcg', 
                                onDelete = 'cascade'
                                )
        
        # foreing key to cdacod - codice piano centri di analisi
        cdacod__cod = tbl.column('cdacod__cod', dtype='A', size=':32',
                                 defaultFrom='@rcrcg__id.@rc__id.@sog__cod.cdacod__cod',
                                 name_long = '!![it]CDA cod.',
                                 #unmodifiable=False,
                                 validate_notnull=True,
                                 )
        cdacod__cod.relation('pn.cdacod.cod', mode='foreignkey',
                             relation_name='CDACOD_riga',
                             onDelete='raise'
                             )

        # foreing key to cdacentro - il centro di analisi
        cdacentro__id = tbl.column('cdacentro__id', dtype='A', size='22',
                                   name_long = '!![it]CDA',
                                   #unmodifiable=False,
                                   validate_notnull=True,
                                   )
        cdacentro__id.relation('pn.cdacentro.id', mode='foreignkey',
                               relation_name='CDA_riga',
                               #one_one=True,
                               onDelete='raise'
                               )

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione dettaglio CdA', 
                   )

        tbl.column('dare_udc', dtype='N', size='12,2',
                   name_long='!![it]Dare', name_short='!![it]D',
                   #validate_notnull=True,
                   )

        tbl.column('avere_udc', dtype='N', size='12,2',
                   name_long='!![it]Avere', name_short='!![it]A',
                   #validate_notnull=True,
                   )

        tbl.formulaColumn('saldo_udc', 'COALESCE($dare_udc, 0) - COALESCE($avere_udc, 0)',
                          dtype='N', size='12,2',
                          name_long='!![it]Saldo', name_short='!![it]S')

        # tbl.aliasColumn('sog_cdacod',
        #                 relation_path='@rcrcg__id.@rc__id.@sog__cod.cdacod__cod',
        #                 # da inspector @rcrcg__id.@rc__id.@sog__cod.cdacod__cod
        #                 name_long='!![it]Piano CDA soggetto'
        #                 )

        tbl.formulaColumn('caption', '$desc',
                          name_long='!![it]Descrizione',
                          name_short='!![it]Desc')
