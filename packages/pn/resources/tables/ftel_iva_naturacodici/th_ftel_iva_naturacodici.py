#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cod')
        r.fieldcell('desc')
        r.fieldcell('valido_dal')
        r.fieldcell('valido_al')
        r.fieldcell('note')

    def th_order(self):
        return 'cod'

    def th_query(self):
        return dict(column='cod', op='contains', val='', runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('cod')
        fb.field('desc')
        fb.field('valido_dal')
        fb.field('valido_al')
        fb.field('note')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
