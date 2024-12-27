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
        #r.fieldcell('rcrcg__id')
        r.fieldcell('_row_count', counter=True, hidden=False,
                    name='!![it]Riga',
                    )
        r.fieldcell('data_scadenza')
        r.fieldcell('data_operazione')
        r.fieldcell('data_valuta')
        r.fieldcell('data_scadenza_prev')
        r.fieldcell('data_scadenza_negoz')
        r.fieldcell('dare_udc', totalize=True)
        r.fieldcell('avere_udc', totalize=True)
        r.fieldcell('saldo_udc', totalize=True)
        r.fieldcell('desc')

    def th_order(self):
        return 'data_scadenza'

    def th_query(self):
        return dict(column='rcrcg__id', op='contains', val='')


class ViewFromRCRCG(View):
    pass



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=5, border_spacing='4px')

        fb.field('_row_count', readOnly=True, lbl='!![it]Riga')
        fb.div('')
        fb.div('')
        fb.div('')
        fb.div('')

        fb.field('data_scadenza')
        fb.field('data_operazione')
        fb.field('data_valuta')
        fb.field('data_scadenza_prev')
        fb.field('data_scadenza_negoz')

        fb.field('dare_udc')
        fb.field('avere_udc')
        fb.field('saldo_udc', readOnly=True)
        fb.div('')
        fb.div('')

        fb.field('desc', colspan=5, width='100%')
        



    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.98)
