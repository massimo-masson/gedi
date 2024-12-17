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
        r.fieldcell('riga_numero')
        r.fieldcell('desc')
        r.fieldcell('pdccod__cod')
        r.fieldcell('pdcconto__id')
        r.fieldcell('dare_udc')
        r.fieldcell('avere_udc')
        r.fieldcell('divisione__id')
        r.fieldcell('divisione_rc')

    def th_order(self):
        return 'rc__id, riga_numero'

    def th_query(self):
        return dict(column='rc__id', op='contains', val='')

class ViewFromRC(View):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('riga_numero')
        r.fieldcell('desc')
        r.fieldcell('pdccod__cod')
        r.fieldcell('pdcconto__id')
        r.fieldcell('dare_udc', totalize=True)
        r.fieldcell('avere_udc', totalize=True)
        r.fieldcell('saldo_udc', totalize=True)
        r.fieldcell('divisione__id')
        r.fieldcell('divisione_rc')


class Form(BaseComponent):

    def th_form(self, form):
        #pane = form.record

        bc = form.center.BorderContainer()
        self.FRMHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.FRMBody(bc.contentPane(region = 'center'))


    def FRMHeader(self, pane):
        fb = pane.formbuilder(cols=5, border_spacing='4px')

        fb.field('rc__id')
        fb.field('riga_numero')
        fb.field('divisione__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$sog__cod = :sog',
                 condition_sog = '=.@rc__id.sog__cod',                 
                 )
        fb.field('divisione_rc', readOnly=True)
        fb.field('pdccod__cod', readOnly=True, hasDownArrow=False)

        fb.field('pdcconto__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$pdccod__cod = :pdc',
                 #condition_pdc = '=#FORM.record.pdccod__cod', # funziona
                 condition_pdc = '=.@rc__id.@sog__cod.pdccod__cod',
                 )
        fb.field('dare_udc')
        fb.field('avere_udc')
        fb.field('saldo_udc')
        fb.div('')
        
        fb.field('desc', colspan=4, width='100%', name_long='!![it]Descrizione')
        fb.div('')

        fb.field('competenza_da')
        fb.field('competenza_a')
        fb.div('')
        fb.div('')
        fb.div('')


    def FRMBody(self, pane):
        tc = pane.tabContainer()

        # tab CDA
        tab_rcrcg = tc.contentPane(title = "!![it]CDA (Centri Di Analisi)")
        tab_rcrcg.dialogTableHandler(relation = '@cda_rcg',
                 pbl_classes = True,
                 viewResource = 'ViewFromRCRCG',
                 #  formResource = 'FormFromCategory',
                 grid_selfDragRows = True,
                 margin = '2px',
                 searchOn = False,
                 )

        # tab commesse
        tab_commesse = tc.contentPane(title = '!![it]Commesse')
        tab_commesse.H1('... to do ....')

        # tab note
        tab_note = tc.contentPane(title = '!![it]Note')



    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)
