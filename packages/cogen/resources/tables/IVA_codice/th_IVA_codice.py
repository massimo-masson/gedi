#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('sigla')
        r.fieldcell('descrizione')
        r.fieldcell('aliquota')

    def th_order(self):
        return 'sigla'

    def th_query(self):
        return dict(column='sigla', op='contains', val='', runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('sigla')
        fb.field('descrizione')
        fb.field('aliquota')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
