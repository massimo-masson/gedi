#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('sog__cod')
        r.fieldcell('cod')
        r.fieldcell('desc')
        r.fieldcell('note')

    def th_order(self):
        return 'sog__cod'

    def th_query(self):
        return dict(column='sog__cod', op='contains', val='')

class ViewFromSOG(View):
    pass


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('sog__cod', hasDownArrow=True)
        fb.field('cod')
        fb.field('desc', colspan=2, width='100%')
        fb.field('note', colspan=2, width='100%', height='5em')


    def th_options(self):
        # return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)
