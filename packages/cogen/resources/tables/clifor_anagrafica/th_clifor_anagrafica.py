#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('ragione_sociale')
        #r.fieldcell('is_cliente')
        #r.fieldcell('is_fornitore')
        r.fieldcell('descrizione')
        r.fieldcell('ditta_anagrafica_id')

    def th_order(self):
        return 'codice'

    def th_query(self):
        #return dict(column='is_cliente', op='istrue')
        return dict(column='codice', op='contains', val='')

    ###def th_options(self):
    ###    return dict(partitioned=True)

class ViewClienti(View):

    def th_query(self):
        return dict(column='is_clienti', op='value', val=1)

class ViewFornitori(View):
    
    def th_query(self):
        return dict(column='is_fornitori', op='istrue')

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('ragione_sociale')
        fb.field('is_cliente')
        fb.field('is_fornitore')
        fb.field('descrizione')
        fb.field('ditta_anagrafica_id', hasDownArrow=True)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

class FormFromDitta(Form):
    pass