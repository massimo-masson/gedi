#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice', sort='d')

        # set colonne 
        #esercizio = r.columnset('colset_esercizio', name='!![it]Esercizio')
        r.fieldcell('descrizione')
        r.fieldcell('anno')
        r.fieldcell('chiuso', 
                range_chiuso='value==true', range_chiuso_color='dark red')
        r.fieldcell('corrente')

        # set specifiche
        #specifiche = r.columnset('colset_specifiche', name='!![it]Specifiche',
        #        background='green')
        r.fieldcell('ditta_anagrafica_id')
        r.fieldcell('pdc_anagrafica_id')
        r.fieldcell('pdc_anagrafica_descrizione')

    def th_order(self):
        return 'codice:d'

    def th_query(self):
        return dict(column='codice', op='contains', val='', runOnStart=True)

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=4, border_spacing='4px')
        
        fb.field('codice')
        fb.field('descrizione')
        fb.field('corrente', width='3em')
        fb.field('chiuso', width='3em')

        fb.field('anno')
        fb.field('ditta_anagrafica_id', hasDownArrow=True)
        fb.field('pdc_anagrafica_id', hasDownArrow=True)
        #fb.field('pdc_anagrafica_descrizione')
        fb.field('@pdc_anagrafica_id.descrizione', readOnly=True)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
        

class ViewFromDitta(View):
    pass

class FormFromDitta(Form):

    def th_options(self):
        return dict(dialog_parentRatio=.8, modal=True)