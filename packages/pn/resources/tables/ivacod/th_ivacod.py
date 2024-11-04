#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from datetime import date

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cod')
        r.fieldcell('ftel_iva_naturacodici__id')
        r.fieldcell('desc')
        r.fieldcell('note')

    def th_order(self):
        return 'cod'

    def th_query(self):
        return dict(column='cod', op='contains', val='', runOnStart=True)



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('cod')
        fb.field('ftel_iva_naturacodici__id', hasDownArrow=True,
                 #columns='$cod,$desc',
                 auxColumns='$cod,$desc', 
                 condition = '($valido_al IS NULL) OR ($valido_al >= :data_di_sistema)',
                 condition_data_di_sistema = self.rootenv['workdate']
                 )
        fb.field('desc', colspan=2)
        fb.field('note', colspan=2)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
