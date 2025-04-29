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
        '''rc_grp_nn_cfg: tabella appoggio relazione n:n rc_grp e rc_grp_cfg
        
        '''

        tbl = pkg.table('rc_grp_nn_cfg', pkey='id', 
                        name_long='!![it]Configurazione gruppo registrazioni',
                        name_plural='!![it]Configurazioni gruppi registrazioni',
                        name_short='!![it]Conf.grp.reg.',
                        caption_field='rc_grp_cfg__id',
                        )

        self.sysFields(tbl)

        #
        # Relazione con i gruppi di registrazione
        #
        rc_grp__id = tbl.column('rc_grp__id', dtype = 'A', size = '22',
                                name_long = '!![it]Gruppo',
                                name_plural = '!![it]Gruppi',
                                )
        rc_grp__id.relation('pn.rc_grp.id', mode = 'foreignkey',
                            relation_name = 'configurazioni_rcgrpcfg',
                            onDelete = 'cascade',
                            )

        #
        # Relazione con le configurazioni contabili
        #
        rc_grp_cfg__id = tbl.column('rc_grp_cfg__id', dtype = 'A', size = '22',
                                    name_long = '!![it]Configurazione',
                                    name_plural = '!![it]Configurazioni',
                                    )
        rc_grp_cfg__id.relation('pn.rc_grp_cfg.id', mode = 'foreignkey',
                                relation_name = 'gruppi_rcgrp',
                                onDelete = 'cascade',
                                )
        