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
        r.fieldcell('sog__cod', readOnly=True)
        r.fieldcell('cod', readOnly=True)
        #r.fieldcell('cpk')
        r.fieldcell('iva_attivita__cod')
        #r.fieldcell('iva_attivita__fk')
        r.fieldcell('desc')
        r.fieldcell('note')

    def th_order(self):
        return 'sog__cod,cod'

    def th_query(self):
        return dict(column='cod', op='contains', val='', runOnStart=True)


class ViewFromSOG(View):
    pass

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=3, border_spacing='4px')
        fb.field('sog__cod', hasDownArrow=True)
        fb.field('cod')
        fb.dbSelect('^.iva_attivita__cod', dbtable='pn.iva_attivita',
                    lbl='!![it]attività IVA',
                    hasDownArrow=True,
                    columns='$cod,$desc',
                    auxColumns='$cod,$desc',
                    condition='$sog__cod=:sog',
                    condition_sog='=.sog__cod',
                    alternatePkey="cod",    # il campo della tabella dbtable
                    )
        # Questa non funziona, la chiave recuperata e' tutta la compositeColumn,
        # invece qui serve solo il campo iva_attivita__cod
        # fb.field('iva_attivita__fk', 
        #          hasDownArrow=True, readOnly = False,
        #          columns='$cod,$desc',
        #          condition='$sog__cod=:sog',
        #          condition_sog='=.sog__cod',
        #          alternatePkey="cod",    # il campo della tabella dbtable
        #          )
        ###
        # VERSIONE VECCHIA: prima di pk composte
        # fb.field('iva_attivita__cod', hasDownArrow=True,
        #          columns='$cod,$desc',
        #          condition='$sog__cod=:sog',
        #          condition_sog='=.sog__cod',
        #          )

        fb.field('desc', colspan=3, width='100%')
        fb.field('note', colspan=3, width='100%')


    def th_options(self):
        #return dict(dialog_height='400px', dialog_width='600px')
        return dict(dialog_parentRatio=0.8)
