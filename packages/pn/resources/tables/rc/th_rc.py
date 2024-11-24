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
        r.fieldcell('rc_rif')
        r.fieldcell('rc_docdata')
        r.fieldcell('rc_docnum')

    def th_order(self):
        return 'sog__cod'

    def th_query(self):
        return dict(column='sog__cod', op='contains', val='')

    def th_options(self):
        return dict(partitioned=True)


class Form(BaseComponent):

    def th_form(self, form):
        # pane = form.record
        # fb = pane.formbuilder(cols=2, border_spacing='4px')
        # fb.field('sog__cod')
        # fb.field('rcgrpcls__cod')
        # fb.field('desc')
        # fb.field('rc_data')
        # fb.field('rc_rif')
        # fb.field('rc_docdata')
        # fb.field('rc_docnum')

        bc = form.center.BorderContainer()
        self.PDCHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.PDCBody(bc.contentPane(region = 'center'))

    def PDCHeader(self, pane):
        fb = pane.formbuilder(cols = 4, border_spacing = '4px')

        fb.field('rc_data')
        fb.field('rc_rif')
        fb.field('rcgrpcls__cod')
        fb.field('sog__cod', readOnly=True)

        fb.field('desc', colspan=4, width='90%')

        fb.field('rc_docdata')
        fb.field('rc_docnum')
        fb.div('')
        fb.div('')

    def PDCBody(self, pane):
        tc = pane.tabContainer()

        # tab rcrcg righe contabilita' generale
        tab_rcrcg = tc.contentPane(title = "!![it]Contabilita' Generale")
        tab_rcrcg.dialogTableHandler(relation = '@righe_registrazione',
                 pbl_classes = True,
                 viewResource = 'ViewFromRC',
        #         formResource = 'FormFromCategory',
                 grid_selfDragRows = True,
                 margin = '2px',
                 searchOn = True
                 )

        # tab rciva righe IVA
        tab_rciva = tc.contentPane(title = '!![it]Movimenti IVA')

        # tab allegati
        tab_allegati = tc.contentPane(title = '!![it]Allegati')

        # tab note
        tab_rciva = tc.contentPane(title = '!![it]Note')


    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)
