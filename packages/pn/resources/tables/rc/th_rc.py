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
        r.fieldcell('rcgrpcls__cod')
        r.fieldcell('desc')
        r.fieldcell('rc_data')
        r.fieldcell('rc_rif')
        r.fieldcell('rc_docdata')
        r.fieldcell('rc_docnum')
        r.fieldcell('ivaregistro__id')
        r.fieldcell('divisione__id')

    def th_order(self):
        return 'sog__cod'

    def th_query(self):
        return dict(column='sog__cod', op='contains', val='')

    def th_options(self):
        return dict(partitioned=True)


class Form(BaseComponent):

    def th_form(self, form):
        # pane = form.record
        # fb = pane.formbuilder(cols=2, border_spacing='4px')
        # fb.field('sog__cod')
        # fb.field('rcgrpcls__cod')
        # fb.field('desc')
        # fb.field('rc_data')
        # fb.field('rc_rif')
        # fb.field('rc_docdata')
        # fb.field('rc_docnum')

        bc = form.center.BorderContainer()
        self.PDCHeader(bc.contentPane(region = 'top', datapath = '.record'))
        self.PDCBody(bc.contentPane(region = 'center'))

    def PDCHeader(self, pane):
        fb = pane.formbuilder(cols = 4, border_spacing = '4px')

        fb.field('rc_data')
        fb.field('rc_rif')
        fb.field('rcgrpcls__cod')
        fb.field('sog__cod', readOnly=True)

        fb.field('desc', colspan=4, width='90%')

        fb.field('rc_docdata')
        fb.field('rc_docnum')
        fb.field('divisione__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 #auxColumns='$cod,$desc',
                 condition='$sog__cod=:sog',
                 #condition_sog='=#FORM.record.sog__cod', # anche questa funziona
                 condition_sog='=.sog__cod',
                 )
        fb.div('')

        fb.field('ivaregistro__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 #auxColumns='$cod,$desc',
                 condition='$sog__cod=:ws',
                 #condition_ws='=#FORM.record.sog__cod', # anche questa funziona
                 condition_ws='=.sog__cod'
                 )
        fb.field('iva_protocollo')
        fb.field('iva_protocollo_appendice')
        fb.div('')


    def PDCBody(self, pane):
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

        # tab allegati
        tab_allegati = tc.contentPane(title = '!![it]Allegati')

        # tab note
        tab_note = tc.contentPane(title = '!![it]Note')


    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)
