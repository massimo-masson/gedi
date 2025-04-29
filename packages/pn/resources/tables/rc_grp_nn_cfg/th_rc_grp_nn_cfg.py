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

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('rc_grp__id', hasDownArrow=True,
        #             columns='$cod,$desc',
        #             condition='$sog__cod = :SOG',
        #             condition_SOG='=.sog__cod',
        #             )
        r.fieldcell('rc_grp__id')
        r.fieldcell('rc_grp_cfg__id')
        r.fieldcell('@rc_grp__id.desc')
        r.fieldcell('@rc_grp__id.classe_desc')
        #r.fieldcell('__ins_sog__cod')

    def th_order(self):
        return 'rc_grp__id'

    def th_query(self):
        return dict(column='rc_grp__id', op='contains', val='',
                    runOnStart=True,
                    )



class ViewFromGRPCFG(View):
    pass


class ViewFromGRP(View):
    pass


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=1, border_spacing='4px')

        fb.field('rc_grp__id', hasDownArrow=True,
                 columns='$cod,$desc,$sog__cod',
                 auxColumns='$cod,$desc',
                 condition='$sog__cod=:sog',
                 condition_sog='=pn_sog.form.record.cod',
                 #condition_sog='=.__ins_sog__cod', # versione con campo in db
                 #condition_sog='XS', # for testing purposes...
                 )

        fb.field('rc_grp_cfg__id', hasDownArrow=True,
                 columns='$cod,$desc,$sog__cod',
                 auxColumns='$cod,$desc',
                 condition='$sog__cod=:sog',
                 condition_sog='=pn_sog.form.record.cod',
                 #condition_sog='XS', # for testing purposes...
                 )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
