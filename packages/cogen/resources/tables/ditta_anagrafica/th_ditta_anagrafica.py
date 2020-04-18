#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('descrizione')
        r.fieldcell('partita_iva')
        r.fieldcell('codice_fiscale')

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
        #fb.field('partita_iva')
        #fb.field('codice_fiscale')
        bc = form.center.borderContainer()
        self.dittaInfo(bc.contentPane(region='top', datapath='.record'))
        self.dittaCorpo(bc.contentPane(region='center'))

    def dittaInfo(self, pane):
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        # riga 1
        fb.field('codice')
        fb.field('descrizione')
        # riga 2
        fb.field('partita_iva')
        fb.field('codice_fiscale')

    def dittaCorpo(self, pane):
        tc = pane.tabContainer()
        # esercizi
        esercizi = tc.contentPane(title='!![it]Esercizi')
        esercizi.dialogTableHandler(relation='@esercizi',
                viewResource='ViewFromDitta',
                formResource='FormFromDitta',
                margin='2px')
        
        # altro
        altro = tc.contentPane(title='AlTrO')
        altro.div('...to do...')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
