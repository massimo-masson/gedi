#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('descrizione')
        r.fieldcell('ditta_anagrafica_id')
        r.fieldcell('iva_registro_tipo_id')
        r.fieldcell('iva_registro_tipo_descrizione')
        r.fieldcell('iva_registro_segno')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='', runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=3, border_spacing='4px')
        fb.field('codice')
        fb.field('descrizione', colspan=2, width='100%')
        fb.field('ditta_anagrafica_id', hasDownArrow=True)
        fb.field('iva_registro_tipo_id', hasDownArrow=True)
        fb.field('iva_registro_segno', readOnly=True)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')


class ViewFromDitta(View):
    pass

class FormFromDitta(Form):
    def th_options(self):
        return dict(dialog_parentRatio=.8, modal=True)