#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count', counter=True, hidden=False,
                    name='!![it]Riga',
                    )
        #r.fieldcell('rc__id', readOnly=True, lbl='!![it]Riga')
        r.fieldcell('desc')
        r.fieldcell('pdccod__cod', readOnly=True)
        r.fieldcell('pdcconto__id', hasDownArrow=True)
        r.fieldcell('cdacod__cod', readOnly=True)
        r.fieldcell('cdacentro__id', hasDownArrow=True)
        r.fieldcell('pdvcod__cod', readOnly=True)
        r.fieldcell('pdvvoce__id', hasDownArrow=True)
        r.fieldcell('dare_udc')
        r.fieldcell('avere_udc')
        r.fieldcell('competenza_am')
        r.fieldcell('divisione__id')
        r.fieldcell('commessa__id')

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
        fb.field('pdccod__cod', readOnly=True)
        fb.field('pdcconto__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$pdccod__cod = :pdc',
                 condition_pdc = '=.@rc__id.@sog__cod.pdccod__cod',
                 )
        fb.field('cdacod__cod', readOnly=True)
        fb.field('cdacentro__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition='$cdacod__cod = :CDACOD',
                 condition_CDACOD='=.cdacod__cod',
                 )
        fb.field('pdvcod__cod', readOnly=True)
        fb.field('pdvvoce__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$pdvcod__cod = :pdv',
                 condition_pdv = '=.@rc__id.@sog__cod.pdvcod__cod',
                 )
        fb.field('dare_udc')
        fb.field('avere_udc')
        fb.field('competenza_am')
        fb.field('divisione__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$sog__cod = :sog',
                 condition_sog = '=.@rc__id.sog__cod',                 
                 )
        fb.field('commessa__id', hasDownArrow=True,
                 columns='$cod,$desc',
                 condition = '$sog__cod = :sog',
                 condition_sog = '=.@rc__id.sog__cod',                 
                 )


    def th_options(self):
        # return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)
