#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('rc__id')
        r.fieldcell('riga_numero')
        r.fieldcell('desc')
        r.fieldcell('pdccod__cod')
        r.fieldcell('pdcr__id')
        r.fieldcell('dare_udc')
        r.fieldcell('avere_udc')

    def th_order(self):
        return 'rc__id, riga_numero'

    def th_query(self):
        return dict(column='rc__id', op='contains', val='')

class ViewFromRC(View):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('riga_numero')
        r.fieldcell('desc')
        r.fieldcell('pdccod__cod')
        r.fieldcell('pdcr__id')
        r.fieldcell('dare_udc')
        r.fieldcell('avere_udc')

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('rc__id')
        fb.field('riga_numero')

        fb.field('pdccod__cod', hasDownArrow=True)
        fb.field('pdcr__id', hasDownArrow=True)
        
        fb.field('dare_udc')
        fb.field('avere_udc')

        fb.field('desc', colspan=2, width='100%')


    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)
