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
        bc = form.center.borderContainer()
        self.pdcInfo(bc.contentPane(region='top', datapath='.record'))
        self.pdcConti(bc.contentPane(region='center'))
    
    def pdcInfo(self, pane):
        div1 = pane.div(margin='2px', 
                border='1px solid silver',
                rounded=5,
                shadow='4px 4px 8px #666')

        fb = div1.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('descrizione')
        fb.field('note', colspan=2, width='100%', 
            tag='simpleTextArea', height='5em')

    def pdcConti(self, pane):
        tc = pane.tabContainer()

        # TAB Conti
        conti = tc.contentPane(title='!![it]Elenco conti')
        #conti.inlineTableHandler(relation='@conti',
        #        pbl_classes=True,
        #        viewResource='ViewFromPDC',
        #        grid_selfDragRows=True,
        #        margin='2px',
        #        searchOn=True)
        conti.dialogTableHandler(relation='@conti',
                viewResource='ViewFromPDC',
                formResource='FormFromPDC',
                margin='2px')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
