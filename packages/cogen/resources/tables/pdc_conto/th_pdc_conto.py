#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('pdc_codice')
        r.fieldcell('descrizione')
        r.fieldcell('note')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')


class ViewFromPDC(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice', edit=True)
        r.fieldcell('pdc_codice', edit=True)
        r.fieldcell('descrizione', edit=True)
        r.fieldcell('note', edit=True)

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('pdc_codice')
        fb.field('descrizione')
        fb.field('note')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

class FormFromPDC(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('@pdc_codice.descrizione', colspan=2, width='100%', readOnly=True)
        fb.field('codice')
        #fb.field('pdc_codice', readOnly='y')
        fb.field('descrizione')
        fb.field('note', colspan=2, width='100%')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

