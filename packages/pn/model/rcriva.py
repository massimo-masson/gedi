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
        '''rcriva: rilevazione contabile - riga IVA

        Righe movimenti IVA        
        '''

        tbl = pkg.table('rcriva', pkey='id', 
                        # pkey_columns='rc__id,riga_numero', # 20241227 CANCELLARE
                        pkey_columns='rc__id',
                        name_long="!![it]Riga movimento IVA",
                        name_plural="!![it]Righe movimenti IVA",
                        caption_field='caption')

        self.sysFields(tbl, counter='rc__id')

        #
        # TO DO: PK COMPOSITA
        #
        # La PK corretta di questa tabella e':
        # rc__id
        #

        # foreign key to rc - testata registrazione
        rc__id = tbl.column('rc__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Testata',
                                    unmodifiable=True,
                                    validate_notnull = True
                                    )
        rc__id.relation('pn.rc.id', mode = 'foreignkey',
                                relation_name = 'righe_iva_registrazione', 
                                onDelete = 'cascade')
        
        # 20241227 CANCELLA: il campo 'riga_numero' e' diventato ridondante 
        # dopo aver utilizzato il counter='rc__id'. Si puo' cancellare
        #
        # tbl.column('riga_numero', dtype='N',
        #            unmodifiable=True,
        #            name_long='!![it]Progressivo riga',
        #            validate_notnull=True
        #            )
        # 20241226 END CANCELLA

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione movimento IVA', 
                   )

        # foreign key to ivacodice: codice IVA del movimento
        ivacod__id = tbl.column('ivacod__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Codice IVA',
                                    #unmodifiable=True,
                                    validate_notnull = True
                                    )
        ivacod__id.relation('pn.ivacod.id', mode = 'foreignkey',
                                relation_name = 'codice_iva_registrazione', 
                                onDelete = 'raise')

        tbl.column('indetr', dtype='N', size='3,2',
                   name_long='!![it]Perc. indetraibilità',
                   name_short='!![it]Perc.indet.',
                   format='###.00',
                   #validate_notnull=True,
                   )

        tbl.column('importo', dtype='N', size='12,2',
                   name_long='!![it]Importo/imponibile',
                   #validate_notnull=True,
                   )

        tbl.column('iva', dtype='N', size='12,2',
                   default='$iva * $iva_aliquota / 100',
                   name_long='!![it]IVA',
                   #validate_notnull=True,
                   )

        tbl.aliasColumn('iva_aliquota', dtype='N',
                        name_long='!![it]Aliquota IVA',
                        name_short='!![it]% IVA',
                        relation_path='@ivacod__id.aliquota',
                        )
        
        tbl.formulaColumn('iva_indetr', '$iva * $indetr',
                          dtype='N', size='12,2',
                          name_long='!![it]IVA Indetraibile',
                          name_short='!![it]IVA Ind.',
                          )
        
        tbl.formulaColumn('totale_riga', '$importo + $iva',
                          name_long='!![it]Totale Riga',
                          name_short='!![it]Tot.r.',
                          )

        tbl.formulaColumn('caption', "$_row_count",
                          name_long='!![it]Riga')
