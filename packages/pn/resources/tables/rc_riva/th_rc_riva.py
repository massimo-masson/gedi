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
        r.fieldcell('rc__id')
        r.fieldcell('_row_count', counter=True, hidden=False,
                    name='!![it]Riga',
                    )
        r.fieldcell('desc')
        r.fieldcell('iva_cod__cod')
        r.fieldcell('iva_aliquota')
        r.fieldcell('indetr')
        r.fieldcell('importo')
        r.fieldcell('iva')
        r.fieldcell('iva_indetr')
        r.fieldcell('totale_riga')

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='rc__id', op='contains', val='')



class ViewFromRC(View):
    pass



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=4, border_spacing='4px')
        #
        fb.field('rc__id')
        fb.field('_row_count', readOnly=True, lbl='!![it]Riga')
        #fb.field('riga_numero') # cancellare con counter del 20241227
        fb.div()
        fb.div()

        fb.field('desc', colspan=4, width='100%')
        #
        fb.field('iva_cod__cod', hasDownArrow=True)
        fb.field('iva_aliquota', readOnly=True, width='5em')
        fb.field('indetr')
        fb.div()
        #
        fb.field('importo')
        fb.field('iva')
        fb.field('iva_indetr')
        fb.div()
        #
        fb.field('totale_riga')
        fb.div()
        fb.div()
        fb.div()


    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.9)
