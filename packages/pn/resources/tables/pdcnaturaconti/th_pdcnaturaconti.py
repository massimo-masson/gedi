#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
        fb.field('note', colspan=2, width='100%')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
