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
        r.fieldcell('sog__cod')
        r.fieldcell('esercizi__cod')
        #r.fieldcell('rc_grp_cls__cod')
        r.fieldcell('desc')
        r.fieldcell('rc_data')
        r.fieldcell('rc_rif')
        r.fieldcell('rc_docdata')
        r.fieldcell('rc_docnum')
        r.fieldcell('iva_registri__cod')
        r.fieldcell('divisioni__id')
        r.fieldcell('commesse__id')
        r.fieldcell('rc_grp__id')

    def th_order(self):
        return 'sog__cod, esercizi__cod, rc_data'

    def th_query(self):
        return dict(column='sog__cod', op='contains', val='')

    def th_options(self):
        return dict(partitioned=True)



class ViewFromSOG(View):
    pass 



class Form(BaseComponent):

    def th_form(self, form):
        # pane = form.record
        # fb = pane.formbuilder(cols=2, border_spacing='4px')
        # fb.field('sog__cod')
        # fb.field('rc_grp_cls__cod')
        # fb.field('desc')
        # fb.field('rc_data')
        # fb.field('rc_rif')
        # fb.field('rc_docdata')
        # fb.field('rc_docnum')

        bc = form.center.BorderContainer()
        self.FHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.FBody(bc.contentPane(region = 'center'))

    def FHeader(self, pane):
        fb = pane.formbuilder(cols = 3, border_spacing = '4px')

        #fb.field('sog__cod', readOnly=True)
        
        fb.field('rc_grp__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 #auxColumns='$cod,$desc',
                 condition='$sog__cod=:sog',
                 condition_sog='=.sog__cod',
                 )
        fb.field('@rc_grp__id.classe_desc', readOnly=True)
        fb.div('')

        fb.dbSelect('^.esercizi__cod', dbtable='pn.sog_esercizi',
                    lbl='!![it]Esercizio', 
                    hasDownArrow=True,
                    columns='$cod,$desc',
                    auxColumns='$cod,$desc',
                    condition='$sog__cod=:sog',
                    condition_sog='=.sog__cod',
                    alternatePkey='cod',
                    )

        fb.field('rc_data')
        fb.field('rc_rif')

        fb.field('desc', colspan=3, width='90%')

        fb.field('rc_docdata')
        fb.field('rc_docnum')
        fb.div('')

        fb.field('commesse__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 #auxColumns='$cod,$desc',
                 condition='$sog__cod=:sog',
                 condition_sog='=.sog__cod',
                 )
        fb.field('divisioni__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 #auxColumns='$cod,$desc',
                 condition='$sog__cod=:sog',
                 #condition_sog='=#FORM.record.sog__cod', # anche questa funziona
                 condition_sog='=.sog__cod',
                 )
        fb.div('')

#        fb.field('iva_registri__id', hasDownArrow=True,
        fb.dbSelect('^.iva_registri__cod', dbtable='pn.iva_registri',
                    lbl='!![it]Registro IVA',
                    hasDownArrow=True,
                    columns='$cod,$desc',
                    auxColumns='$cod,$desc',
                    condition='$sog__cod=:sog',
                    #condition_sog='=#FORM.record.sog__cod', # alternativa
                    condition_sog='=.sog__cod',
                    alternatePkey='cod'
                    )
        fb.field('iva_protocollo')
        fb.field('iva_protocollo_appendice')


    def FBody(self, pane):
        tc = pane.tabContainer()

        # tab rcrcg righe contabilita' generale
        tab_rcrcg = tc.contentPane(title = "!![it]Contabilita' Generale")
        tab_rcrcg.dialogTableHandler(relation = '@righe_registrazione',
                 pbl_classes = True,
                 viewResource = 'ViewFromRC',
                 #  formResource = 'FormFromCategory',
                 grid_selfDragRows = True,
                 margin = '2px',
                 searchOn = True
                 )

        # tab rciva righe IVA
        tab_rcriva = tc.contentPane(title = '!![it]Movimenti IVA')
        tab_rcriva.dialogTableHandler(relation = '@righe_iva_registrazione',
                 pbl_classes = True,
                 viewResource = 'ViewFromRC',
                 # formResource = 'FormFromCategory',
                 grid_selfDragRows = True,
                 margin = '2px',
                 searchOn = True
                 )

        # tab movimenti analitica
        tab_movana = tc.contentPane(title = '!![it]Movimenti analitica')
        tab_movana.dialogTableHandler(relation = '@righe_rccoacam',
                 pbl_classes = True,
                 viewResource = 'ViewFromRC',
                 # formResource = 'FormFromCategory',
                 grid_selfDragRows = True,
                 margin = '2px',
                 searchOn = True
                 )

        # tab riepilogo rilevazione
        tab_riepil = tc.contentPane(title = '!![it]Riepilogo rilevazione',
                                    datapath = '.record'
                                    )

        # riepilogo coge
        tab_riepil.h3('!![it]Contabilità generale:')
        boxcoge = tab_riepil.div('', 
                                 border='1px solid black',
                                 border_radius='10px',
                                 padding='20px',
                                 )
        fbcoge = boxcoge.formbuilder(cols = 3, border_spacing = '4px')
        fbcoge.field('tot_dare_udc')
        fbcoge.field('tot_avere_udc')
        fbcoge.field('numero_righe_coge')

        # riepilogo CDA
        tab_riepil.h3('!![it]Centri di analisi:')
        box_cda = tab_riepil.div('', 
                                 border='1px solid black',
                                 border_radius='10px',
                                 padding='20px',
                                 )
        fbcda = box_cda.formbuilder(cols = 3, border_spacing = '4px')
        fbcda.field('tot_cda_dare_udc')
        fbcda.field('tot_cda_avere_udc')
        fbcda.field('numero_cda_movimentati')

        fbcda.field('diff_coge_cda_dare')
        fbcda.field('diff_coge_cda_avere')
        fbcda.div('')

        # riepilogo commesse
        tab_riepil.h3('!![it]Commesse:')
        box_com = tab_riepil.div('', 
                                 border='1px solid black',
                                 border_radius='10px',
                                 padding='20px',
                                 )
        fbcom = box_com.formbuilder(cols = 3, border_spacing = '4px')
        fbcom.field('tot_com_dare_udc')
        fbcom.field('tot_com_avere_udc')
        fbcom.field('numero_com_movimentate')

        fbcom.field('diff_coge_com_dare')
        fbcom.field('diff_coge_com_avere')
        fbcom.div('')



    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.95)
