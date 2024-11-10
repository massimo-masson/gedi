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
        #r.fieldcell('parent_id')
        r.fieldcell('cod')
        #r.fieldcell('hierarchical_cod')
        #r.fieldcell('_parent_h_cod')
        #r.fieldcell('hierarchical_pkey')
        #r.fieldcell('_parent_h_pkey')
        r.fieldcell('desc')
        r.fieldcell('epilogo')
        #r.fieldcell('note')

    def th_order(self):
        return 'parent_id'

    def th_query(self):
        return dict(column='parent_id', op='contains', val='', 
                    runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        #fb.field('parent_id')
        fb.field('cod')
        fb.field('hierarchical_cod')
        fb.field('epilogo')
        fb.div()
        #fb.field('_parent_h_cod')
        #fb.field('hierarchical_pkey')
        #fb.field('_parent_h_pkey')
        fb.field('desc', colspan=2, width='100%')
        fb.field('note', colspan=2, width='100%',
                 height='5em',
                 tag='simpleTextArea', editor=True
                 )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
