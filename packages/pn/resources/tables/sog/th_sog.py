#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# gedi: ge-stionale di-rezionale
# Strumenti per la gestione contabile, amministrativa, finanziaria,
# per il controllo di gestione e direzionale.
# Copyright (C) 2023 Massimo Masson
# 
# This program is dual-licensed.
# 
# Option 1:
# If you respect the terms of GNU GPL license, AND
# you agree to give the copyright for modifications or derivative work
# to the original author Massimo Masson, the GPL license applies.
# In this case:
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# 
# Option 2:
# If you do not agree with any of the statements in option 1, then
# a proprietary license applies. In this case, contact the author
# for a dedicated propietary license.
# 

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cod')
        r.fieldcell('desc')
        r.fieldcell('pdccod__cod')
        r.fieldcell('pdvcod__cod')
        r.fieldcell('cdacod__cod')
        #r.fieldcell('note')

    def th_order(self):
        return 'cod'

    def th_query(self):
        return dict(column='cod', op='contains', val='',
                    runOnStart=True)


class ViewOperaPNC(View):
    '''Form per gestire le Operazioni di Prima Nota Contabile
    
    '''
    pass 


class ViewAnagSOG(View):
    '''Form per la visualizzazione delle anagrafiche soggetto
    
    '''
    pass


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        
        fb.field('cod')
        fb.div('---')

        fb.field('desc', colspan=2, width='100%')

        fb.field('note', colspan=2, width='100%',
                 height='5em',
                 tag='simpleTextArea', editor=True
                 )

    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)


class FormCFG(Form):
    '''Form per gestire gli elementi di configurazione dei soggetti
    
    '''

    def th_form(self, form):

        bc = form.center.BorderContainer()
        self.FHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.FBody(bc.contentPane(region = 'center'))

    def FHeader(self, pane):
        fb = pane.formbuilder(cols=3, border_spacing='4px')
        
        fb.field('cod')
        fb.field('desc', colspan=2, width='100%')

        fb.field('pdccod__cod', hasDownArrow=True)
        fb.field('pdvcod__cod', hasDownArrow=True)
        fb.field('cdacod__cod', hasDownArrow=True)


    def FBody(self, pane):
        tc = pane.tabContainer()

        # tab esercizi
        tab_esercizi = tc.contentPane(title = "!![it]Esercizi")
        tab_esercizi.dialogTableHandler(relation = '@esercizi',
                                        pbl_classes = True,
                                        viewResource = 'ViewFromSOG',
                                        #formResource = 'FormFromSOG',
                                        grid_selfDragRows = True,
                                        margin = '2px',
                                        searchOn = True
                                        )

        # tab attivita IVA
        tab_iva_attivita = tc.contentPane(title = "!![it]Attività IVA")
        tab_iva_attivita.dialogTableHandler(relation = '@attivita_iva',
                                            pbl_classes = True,
                                            viewResource = 'ViewFromSOG',
                                            #formResource = 'FormFromSOG',
                                            grid_selfDragRows = True,
                                            margin = '2px',
                                            searchOn = True
                                            )

        # tab registri IVA
        tab_iva_registri = tc.contentPane(title = "!![it]Registri IVA")
        tab_iva_registri.dialogTableHandler(relation = '@registri_iva',
                                            pbl_classes = True,
                                            viewResource = 'ViewFromSOG',
                                            #formResource = 'FormFromSOG',
                                            grid_selfDragRows = True,
                                            margin = '2px',
                                            searchOn = True
                                            )

        # tab configurazioni contabili
        tab_gruppiregist = tc.contentPane(title = "!![it]Configurazioni contabili")
        tab_gruppiregist.dialogTableHandler(relation = '@rcgrpcfg_sog',
                                            pbl_classes = True,
                                            viewResource = 'ViewFromSOG',
                                            #formResource = 'FormFromSOG',
                                            grid_selfDragRows = True,
                                            margin = '2px',
                                            searchOn = True
                                            )

        # tab divisioni
        tab_iva_registri = tc.contentPane(title = "!![it]Divisioni")
        tab_iva_registri.dialogTableHandler(relation = '@divisioni',
                                            pbl_classes = True,
                                            viewResource = 'ViewFromSOG',
                                            #formResource = 'FormFromSOG',
                                            grid_selfDragRows = True,
                                            margin = '2px',
                                            searchOn = True
                                            )

        # tab commesse
        tab_commesse = tc.contentPane(title = "!![it]Commesse")
        tab_commesse.dialogTableHandler(relation = '@commesse',
                                        pbl_classes = True,
                                        viewResource = 'ViewFromSOG',
                                        #formResource = 'FormFromSOG',
                                        grid_selfDragRows = True,
                                        margin = '2px',
                                        searchOn = True
                                        )

        # tab NOTE
        tab_note = tc.contentPane(title = "!![it]NOTE", datapath = '.record',
                                  width='100%', height='100%',
                                  #td_width='100%', td_height='100%'
                                  #colswidth='100%',
                                  minwidth='90%', minheight='90%',
                                  )
        #fb = tab_note.formbuilder(cols=1, border_spacing='4px')    
        tab_note.field('note', width='100%', height='10em', 
                       #td_width='100%', td_height='100%',
                       # #minwidth='90%', minheight='90%',
                       tag='simpleTextArea', editor=True
                       )


class FormOperaPNC(Form):
    '''Form per gestire le Operazioni di Prima Nota Contabile
    
    '''

    def th_form(self, form):
        bc = form.center.BorderContainer()
        self.FHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.FBody(bc.contentPane(region = 'center'))

    def FHeader(self, pane):
        fb = pane.formbuilder(cols=3, border_spacing='4px')
        
        fb.field('cod')
        fb.field('desc', colspan=2, width='100%')

    def FBody(self, pane):
        tc = pane.tabContainer()

        # tab rilevazioni
        tab_rilevazioni = tc.contentPane(title = "!![it]Rilevazioni")
        tab_rilevazioni.dialogTableHandler(relation = '@rilevazioni_contabili',
                                           pbl_classes = True,
                                           viewResource = 'ViewFromSOG',
                                           #formResource = 'FormFromSOG',
                                           grid_selfDragRows = True,
                                           margin = '2px',
                                           searchOn = True
                                           )

        # tab gruppi registrazione
        tab_gruppiregist = tc.contentPane(title = "!![it]Gruppi di registrazione")
        tab_gruppiregist.dialogTableHandler(relation = '@gruppi_registrazione',
                                            pbl_classes = True,
                                            viewResource = 'ViewFromSOG',
                                            #formResource = 'FormFromSOG',
                                            grid_selfDragRows = True,
                                            margin = '2px',
                                            searchOn = True
                                            )

        # tab commesse
        tab_commesse = tc.contentPane(title = "!![it]Commesse")
        tab_commesse.dialogTableHandler(relation = '@commesse',
                                        pbl_classes = True,
                                        viewResource = 'ViewFromSOG',
                                        #formResource = 'FormFromSOG',
                                        grid_selfDragRows = True,
                                        margin = '2px',
                                        searchOn = True
                                        )

        # tab NOTE
        tab_note = tc.contentPane(title = "!![it]NOTE", datapath = '.record',
                                  width='100%', height='100%',
                                  #td_width='100%', td_height='100%'
                                  #colswidth='100%',
                                  minwidth='90%', minheight='90%',
                                  )
        #fb = tab_note.formbuilder(cols=1, border_spacing='4px')    
        tab_note.field('note', width='100%', height='10em', 
                       tag='simpleTextArea', editor=True
                       )

class FormAnagSOG(Form):
    '''Form per la visualizzazione delle anagrafiche soggetto
    
    '''

    def th_form(self, form):
        bc = form.center.BorderContainer()
        self.FHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.FBody(bc.contentPane(region = 'center'))

    def FHeader(self, pane):
        fb = pane.formbuilder(cols=3, border_spacing='4px')
        
        fb.field('cod')
        fb.field('desc', colspan=2, width='100%')

    def FBody(self, pane):
        tc = pane.tabContainer()

        # tab clienti
        tab_clienti = tc.contentPane(title = "!![it]Clienti")
        tab_clienti.dialogTableHandler(relation = '@clienti_cli',
                                       pbl_classes = True,
                                       viewResource = 'ViewFromSOG',
                                       #formResource = 'FormFromSOG',
                                       grid_selfDragRows = True,
                                       margin = '2px',
                                       searchOn = True
                                       )

        # tab fornitori
        tab_fornitori = tc.contentPane(title = "!![it]Fornitori")
        tab_fornitori.h1('Fornitori: TO DO')

        # tab banche
        tab_banche = tc.contentPane(title = "!![it]Banche")
        tab_banche.h1('banche: TO DO')

        # tab gruppi registrazione
        tab_gruppiregist = tc.contentPane(title = "!![it]Gruppi di registrazione")
        tab_gruppiregist.dialogTableHandler(relation = '@gruppi_registrazione',
                                            pbl_classes = True,
                                            viewResource = 'ViewFromSOG',
                                            #formResource = 'FormFromSOG',
                                            grid_selfDragRows = True,
                                            margin = '2px',
                                            searchOn = True
                                            )

        # tab commesse
        tab_commesse = tc.contentPane(title = "!![it]Commesse")
        tab_commesse.dialogTableHandler(relation = '@commesse',
                                        pbl_classes = True,
                                        viewResource = 'ViewFromSOG',
                                        #formResource = 'FormFromSOG',
                                        grid_selfDragRows = True,
                                        margin = '2px',
                                        searchOn = True
                                        )

        # tab NOTE
        tab_note = tc.contentPane(title = "!![it]NOTE", datapath = '.record',
                                  width='100%', height='100%',
                                  #td_width='100%', td_height='100%'
                                  #colswidth='100%',
                                  minwidth='90%', minheight='90%',
                                  )
        tab_note.field('note', width='100%', height='10em', 
                       tag='simpleTextArea', editor=True
                       )

    def th_options(self):
        return dict(dialog_parentRatio=0.95)
