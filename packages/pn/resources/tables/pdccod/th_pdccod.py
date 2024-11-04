#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cod')
        r.fieldcell('desc')
        r.fieldcell('note')

    def th_order(self):
        return 'cod'

    def th_query(self):
        return dict(column='cod', op='contains', val='',
                    runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        # pane = form.record
        # fb = pane.formbuilder(cols=2, border_spacing='4px')
        # fb.field('cod')
        # fb.field('desc')
        # fb.field('note')

        bc = form.center.BorderContainer()
        self.PDCHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.PDCBody(bc.contentPane(region = 'center'))

    def PDCHeader(self, pane):
        fb = pane.formbuilder(cols = 3, border_spacing = '4px')

        fb.field('cod')
        fb.field('desc', colspan=2, width='100%')
        fb.field('note', colspan=2, width='100%', height = '100%')

    def PDCBody(self, pane):
        tc = pane.tabContainer()

        # tab pdc records
        tab_pdcr = tc.contentPane(title = '!![it]Conti')
        tab_pdcr.dialogTableHandler(relation = '@conti',
                 pbl_classes = True,
                 viewResource = 'ViewFromPDCCOD',
        #         formResource = 'FormFromCategory',
                 grid_selfDragRows = True,
                 margin = '2px',
                 searchOn = True)
        

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
