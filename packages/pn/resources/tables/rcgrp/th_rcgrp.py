#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codkey')
        r.fieldcell('cod')
        r.fieldcell('sog__cod')
        r.fieldcell('desc')
        r.fieldcell('note')

    def th_order(self):
        return 'codkey'

    def th_query(self):
        return dict(column='codkey', op='contains', val='', runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        #fb.field('codkey')

        fb.field('cod')
        fb.field('sog__cod', hasDownArrow=True)
        #fb.field('@sog__cod.desc', readOnly=True)

        fb.field('desc', colspan=2, width='100%')

        fb.field('note', colspan=2, width='100%')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
