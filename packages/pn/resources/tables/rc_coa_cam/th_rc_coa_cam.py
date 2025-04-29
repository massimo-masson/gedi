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
        colore_automatico = 'DarkSlateGray'
        colore_automatico_sfondo = 'Khaki'

        r = struct.view().rows()
        r.fieldcell('origine_auto', hidden=True)
        r.fieldcell('_row_count', counter=True, hidden=False,
                    name='!![it]Riga',
                    range_autogen="origine_auto>''",
                    range_autogen_color = colore_automatico,
                    range_autogen_background_color = colore_automatico_sfondo,
                    )
        #r.fieldcell('rc__id', readOnly=True, lbl='!![it]Riga')
        r.fieldcell('competenza_am',
                    range_autogen="origine_auto>''",
                    range_autogen_color = colore_automatico,
                    range_autogen_background_color = colore_automatico_sfondo
                    )
        r.fieldcell('dare_udc', format='#,###.00',
                    range_autogen="origine_auto>''",
                    range_autogen_color = colore_automatico,
                    range_autogen_background_color = colore_automatico_sfondo
                    )
        r.fieldcell('avere_udc', format='#,###.00',
                    range_autogen="origine_auto>''",
                    range_autogen_color = colore_automatico,
                    range_autogen_background_color = colore_automatico_sfondo
                    )
        r.fieldcell('cda_centri__cod', hasDownArrow=True,
                    range_autogen="origine_auto>''",
                    range_autogen_color = colore_automatico,
                    range_autogen_background_color = colore_automatico_sfondo,
                    range_autogencda="origine_auto=='pn.rcrcgcda'",
                    range_autogencda_color = 'DarkBlue',
                    )
        r.fieldcell('commesse__id', hasDownArrow=True,
                    range_autogen="origine_auto>''",
                    range_autogen_color = colore_automatico,
                    range_autogen_background_color = colore_automatico_sfondo,
                    range_autogencom="origine_auto=='pn.rcrcgcom'",
                    range_autogencom_color = 'DarkGreen',
                    )
        r.fieldcell('desc')
#        r.fieldcell('pdv_voci__id', hasDownArrow=True)
#        r.fieldcell('pdc_conti__cod', hasDownArrow=True)
        r.fieldcell('pdc_conti__fk')
        r.fieldcell('pdv_voci__fk')
        r.fieldcell('divisioni__id')
        r.fieldcell('cda_cod__cod', readOnly=True)
        r.fieldcell('pdv_cod__cod', readOnly=True)
        r.fieldcell('pdc_cod__cod', readOnly=True)
        r.fieldcell('rc_grp__id')

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='_row_count', op='contains', val='')


class ViewFromRC(View):
    pass


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('_row_count', readOnly=True, lbl='!![it]Riga')
        #fb.field('rc__id')
        fb.field('origine')
        fb.field('desc')
        fb.field('pdc_cod__cod', readOnly=True)
        fb.field('pdc_conti__fk', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$pdc_cod__cod = :pdc',
                 condition_pdc = '=.@rc__id.@sog__cod.pdc_cod__cod',
                 )
        fb.field('cda_cod__cod', readOnly=True)
        fb.field('cda_centri__cod', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition='$cda_cod__cod = :CDACOD',
                 condition_CDACOD='=.cda_cod__cod',
                 )
        fb.field('pdv_cod__cod', readOnly=True)
        fb.dbSelect('^.pdv_voci__cod', dbtable='pn.pdv_voci',
                    lbl='!![it]Voce',
                    hasDownArrow=True,
                    columns='$cod,$desc',
                    auxColumns='$cod,$desc',
                    condition = '$pdv_cod__cod = :pdv',
                    condition_pdv = '=.@rc__id.@sog__cod.pdv_cod__cod',
                    )
        # fb.field('pdv_voci__fk', hasDownArrow=True,
        #          columns='$cod,$desc',
        #          condition = '$pdv_cod__cod = :pdv',
        #          condition_pdv = '=.@rc__id.@sog__cod.pdv_cod__cod',
        #          )
        fb.field('dare_udc')
        fb.field('avere_udc')
        fb.field('competenza_am')
        fb.field('divisioni__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$sog__cod = :sog',
                 condition_sog = '=.@rc__id.sog__cod',                 
                 )
        fb.field('commesse__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$sog__cod = :sog',
                 condition_sog = '=.@rc__id.sog__cod',                 
                 )
        fb.field('rc_grp__id')


    def th_options(self):
        # return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)
