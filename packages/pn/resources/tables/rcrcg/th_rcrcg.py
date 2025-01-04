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
        r.fieldcell('rc__id')
        r.fieldcell('_row_count', counter=True, hidden=False,
                    name='!![it]Riga',
                    )
        #r.fieldcell('riga_numero') # cancellare con counter del 20241226
        r.fieldcell('desc')
        r.fieldcell('pdccod__cod')
        r.fieldcell('pdcconto__id')
        r.fieldcell('dare_udc')
        r.fieldcell('avere_udc')
        r.fieldcell('pdvcod__cod')
        r.fieldcell('pdvvoce__id')
        r.fieldcell('divisione__id')
        r.fieldcell('divisione_rc')
        r.fieldcell('commessa__id')

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='rc__id', op='contains', val='')
    
    def th_options(self):
        return dict(grid_selfDragRows=True)

class ViewFromRC(View):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count', counter=True, hidden=False,
                    name='!![it]Riga',
                    )
        #r.fieldcell('riga_numero') # cancellare con counter del 20241226
        r.fieldcell('desc')
        r.fieldcell('pdccod__cod')
        r.fieldcell('pdcconto__id')
        r.fieldcell('dare_udc', totalize=True)
        r.fieldcell('avere_udc', totalize=True)
        r.fieldcell('saldo_udc', totalize=True)
        r.fieldcell('pdvcod__cod', readOnly=True)
        r.fieldcell('pdvvoce__id', hasDownArrow=True)
        r.fieldcell('commessa__id')
        r.fieldcell('divisione__id')
        r.fieldcell('divisione_rc')


class Form(BaseComponent):

    def th_form(self, form):
        #pane = form.record

        bc = form.center.BorderContainer()
        self.FHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.FBody(bc.contentPane(region = 'center'))


    def FHeader(self, pane):
        fb = pane.formbuilder(cols=3, border_spacing='4px')

        #fb.field('rc__id')
        fb.field('_row_count', readOnly=True, lbl='!![it]Riga')
        #fb.field('riga_numero') # cancellare con counter del 20241226
        fb.field('commessa_rc', readOnly=True)
        fb.field('divisione_rc', readOnly=True)

        fb.field('pdcconto__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$pdccod__cod = :pdc',
                 #condition_pdc = '=#FORM.record.pdccod__cod', # funziona
                 condition_pdc = '=.@rc__id.@sog__cod.pdccod__cod',
                 colspan=2, width='100%',
                 )
        fb.field('pdccod__cod', readOnly=True, hasDownArrow=False)

        fb.field('dare_udc')
        fb.field('avere_udc')
        fb.field('saldo_udc')
        
        fb.field('desc', colspan=3, width='100%', name_long='!![it]Descrizione')

        fb.field('competenza_da')
        fb.field('competenza_a')
        fb.div('')

        fb.field('pdvvoce__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$pdvcod__cod = :pdv',
                 condition_pdv = '=.@rc__id.@sog__cod.pdvcod__cod',
                 colspan=2, width='100%',
                 )
        fb.field('pdvcod__cod', readOnly=True)

        fb.field('commessa__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$sog__cod = :sog',
                 condition_sog = '=.@rc__id.sog__cod',
                 )
        fb.field('divisione__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$sog__cod = :sog',
                 condition_sog = '=.@rc__id.sog__cod',
                 )
        fb.div('')


    def FBody(self, pane):
        tc = pane.tabContainer()

        # tab ANALITICA
        analitica = tc.contentPane(title = "!![it]Analitica")
        aa = analitica.tabContainer(tabPosition='bottom') # top bottom right-h, left-h

        # tab CDA
        tab_rcrcg = aa.contentPane(title = "!![it]Centri")
        tab_rcrcg.dialogTableHandler(relation = '@cda_rcg',
                                     title = '!![it]Dettaglio centri di analisi (analitica)',
                                     pbl_classes = True,
                                     viewResource = 'ViewFromRCRCG',
                                     #  formResource = 'FormFromCategory',
                                     grid_selfDragRows = True,
                                     margin = '2px',
                                     searchOn = False,
                                     )

        # tab COMMESSE
        tab_commesse = aa.contentPane(title = '!![it]Commesse')
        tab_commesse.dialogTableHandler(relation = '@commesse_rcg',
                                        title = '!![it]Dettaglio commesse (analitica)',
                                        pbl_classes = True,
                                        viewResource = 'ViewFromRCRCG',
                                        #  formResource = 'FormFromCategory',
                                        grid_selfDragRows = True,
                                        margin = '2px',
                                        searchOn = False,
                                        )

        # tab FLUSSI FINANZIARI
        tab_flussifi = tc.contentPane(title = '!![it]Flussi Finanziari')
        tab_flussifi.dialogTableHandler(relation = '@flussifin_rcg',
                                        title = '!![it]Scadenze per riga',
                                        pbl_classes = True,
                                        viewResource = 'ViewFromRCRCG',
                                        #  formResource = 'FormFromCategory',
                                        grid_selfDragRows = True,
                                        margin = '2px',
                                        searchOn = False,
                                        )

        # # tab note
        # tab_note = tc.contentPane(title = "!![it]Note", datapath = '.record',
        #                           width='100%', height='100%',
        #                           minwidth='90%', minheight='90%',
        #                           )
        # tab_note.field('note', width='100%', height='10em', 
        #          tag='simpleTextArea', editor=True,
        #          )

        # 20241226 Esperimento: progressivo riga numero da dataRpc
        # fb.dataRpc('.riga_numero', self.getProssimoNumeroRiga, 
        #            pk='^.rc__id',
        #            _onStart=True)
        # 20241226 END Esperimento


    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.9)

    # 20241226 Esperimento: metodo per contatore con dataRpc
    # @public_method
    # def getProssimoNumeroRiga(self, pk):
    #     '''Restituisce il numero progressivo successivo per la riga'''
    #
    #     if not pk:
    #         return
    #   
    #     qry = self.db.table('pn.rcrcg').query(
    #         columns="MAX($riga_numero) AS ultima_riga",
    #         limit=1,
    #         #columns="""COALESCE(MAX($riga_numero), 0) AS ultima_riga""",
    #         where="$rc__id=:registrazione",
    #         registrazione=pk
    #         ).fetch()
    #
    #     # print("ultima_riga =", ultima_riga)
    #     # ultima_riga = [[ultima_riga=2,pkey=KcWbs1O4PxGDpjTCOfg_HQ_2]]
    #     # ultima_riga[0][0] ultima_riga valore 2
    #     # ultima_riga[0][1] pkey valore ...
    #     ultima_riga = qry[0][0] or 0    # if Null start form 0
    #     prossima_riga = ultima_riga + 1
    #
    #     return  prossima_riga
    # 20241226 END Esperimento