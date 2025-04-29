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
        '''rc_rcg_flf: dettaglio flusso finanziario.
        
        Si riferisce ad una riga di registrazione contabile, serve per
        dettagliare i flussi finanziari (scadenze)
        di ciascuna riga contabile di una rilevazione contabile.
        '''

        tbl = pkg.table('rc_rcg_flf', pkey='id', 
                        name_long="!![it]Flussi finanziari",
                        caption_field='caption'
                        )

        self.sysFields(tbl, counter='rc_rcg__id')

        # foreign key to rc_rcg - riga di riferimento
        rc_rcg__id = tbl.column('rc_rcg__id', dtype = 'A', size = '22',
                                name_long = '!![it]Riga contabile',
                                unmodifiable=True,
                                validate_notnull = True
                                )
        rc_rcg__id.relation('pn.rc_rcg.id', mode = 'foreignkey',
                            relation_name = 'flussifin_rcg', 
                            onDelete = 'cascade'
                            )
        
        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione flusso', 
                   )

        tbl.column('data_operazione', dtype='D',
                   name_long='!![it]Data operazione',
                   )
        
        tbl.column('data_valuta', dtype='D',
                   name_long='!![it]Data valuta',
                   )
        
        tbl.column('data_scadenza', dtype='D',
                   name_long='!![it]Data scadenza',
                   )
        
        tbl.column('data_scadenza_prev', dtype='D',
                   name_long='!![it]Data scadenza previsionale',
                   )

        tbl.column('data_scadenza_negoz', dtype='D',
                   name_long='!![it]Data scadenza negoziata',
                   )

        tbl.column('dare_udc', dtype='N', size='12,2',
                   name_long='!![it]Dare', 
                   name_short='!![it]D',
                   #validate_notnull=True,
                   )

        tbl.column('avere_udc', dtype='N', size='12,2',
                   name_long='!![it]Avere', 
                   name_short='!![it]A',
                   #validate_notnull=True,
                   )

        tbl.formulaColumn('saldo_udc', 'COALESCE($dare_udc, 0) - COALESCE($avere_udc, 0)',
                          dtype='N', size='12,2',
                          name_long='!![it]Saldo', 
                          name_short='!![it]S'
                          )

        tbl.formulaColumn('caption', '$desc',
                          name_long='!![it]Descrizione',
                          name_short='!![it]Desc'
                          )
