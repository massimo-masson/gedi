#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('descrizione')
        r.fieldcell('note')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='', runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        #pane = form.record
        #fb = pane.formbuilder(cols=2, border_spacing='4px')
        #fb.field('codice')
        #fb.field('descrizione')
        #fb.field('note', colspan=2, width='100%')
        bc = form.center.borderContainer()
        self.pdcInfo(bc.contentPane(region='top', datapath='.record'))
        self.pdcConti(bc.contentPane(region='center'))
    
    def pdcInfo(self, pane):
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('descrizione')
        fb.field('note', colspan=2, width='100%', 
            tag='simpleTextArea', height='10ex')

    def pdcConti(self, pane):
        #pane.inlineTableHandler(relation='@conti',
        #        pbl_classes=True,
        #        viewResource='ViewFromPDC',
        #        grid_selfDragRows=True,
        #        margin='2px',
        #        searchOn=True)
        pane.dialogTableHandler(relation='@conti',
                viewResource='ViewFromPDC',
                formResource='FormFromPDC',
                margin='2px')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
