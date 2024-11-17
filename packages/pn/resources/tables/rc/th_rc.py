#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('sog__cod')
        r.fieldcell('rcgrpcls__cod')
        r.fieldcell('desc')
        r.fieldcell('rc_data')
        r.fieldcell('rc_docdata')
        r.fieldcell('rc_docnum')

    def th_order(self):
        return 'sog__cod'

    def th_query(self):
        return dict(column='sog__cod', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('sog__cod')
        fb.field('rcgrpcls__cod')
        fb.field('desc')
        fb.field('rc_data')
        fb.field('rc_docdata')
        fb.field('rc_docnum')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
