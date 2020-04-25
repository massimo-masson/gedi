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
        div1 = pane.div(margin='2px', 
                border='1px solid silver',
                rounded=5,
                shadow='4px 4px 8px #666')

        fb = div1.formbuilder(cols=2, border_spacing='4px')
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
        
        # registri IVA
        registri_IVA = tc.contentPane(title='!![it]Registri IVA')
        registri_IVA.dialogTableHandler(relation='@registri_iva',
                viewResource='ViewFromDitta',
                formResource='FormFromDitta',
                margin='2px')

        # Clienti
        clienti = tc.contentPane(title='!![it]Clienti')
        clienti.dialogTableHandler(relation='@clientifornitori',
                viewResource='ViewCliForFromDitta',
                formResource='FormFromDitta',
                condition='$is_cliente=1',
                margin='2px')

        # Fornitori
        fornitori = tc.contentPane(title='!![it]Fornitori')
        fornitori.dialogTableHandler(relation='@clientifornitori',
                viewResource='ViewCliForFromDitta',
                formResource='FormFromDitta',
                condition='$is_fornitore=1',
                margin='2px')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')