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

def config(root,application=None):
    gedi = root.branch('GeDi')

    # menu CONTABILE
    contab = gedi.branch('!![it]CONTABILE')

    contab.thpage('!![it]Gruppi di registrazione', table = 'pn.rcgrp')

    # menu PDC
    pdc = gedi.branch('!![it]PDC')

    pdc.thpage('!![it]Piani dei conti', table = 'pn.pdccod')
    #pdc.thpage('!![it]...singoli conti', table = 'pn.pdcr')

    pdc.thpage('!![it]Natura dei conti', table = 'pn.pdcnaturaconti')

    # menu IVA
    iva = gedi.branch('!![it]IVA')

    iva.thpage('!![it]Codici IVA', table = 'pn.ivacod')
    iva.thpage('!![it]natura codici IVa per Fattura Elettronica', table = 'pn.ftel_iva_naturacodici')

    # menu CONFIGURAZIONE
    conf = gedi.branch('!![it]CONFIGURAZIONE')
    conf.thpage('!![it]Soggetti operativi', table = 'pn.sog')
