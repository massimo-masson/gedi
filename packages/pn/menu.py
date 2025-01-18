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

    contab.thpage('!![it]Anagrafiche', 
                  table = 'pn.sog',
                  viewResource = 'ViewAnagSOG',
                  formResource = 'FormAnagSOG'
                  )

    contab.thpage('!![it]Operazioni', 
                  table = 'pn.sog',
                  viewResource = 'ViewOperaPNC',
                  formResource = 'FormOperaPNC'
                  )
    
    # i due seguenti menu' sono utili per vedere le registrazioni
    # senza il soggetto di riferimento della relazione, utilizzando
    # in parte le funzioni di partizionamento tabella, potendo scegliere
    # e filtrare quale soggetto vedere.
    # La funzionalita' piu' comoda resta quella collegata alla relazione
    # con il soggetto.
    # contab.thpage('!![it]Gruppi di registrazione', table = 'pn.rcgrp')
    # contab.thpage('!![it]Rilevazioni contabili', table = 'pn.rc')

    # menu CONFIGURAZIONE
    conf = gedi.branch('!![it]CONFIGURAZIONE')

    conf.thpage('!![it]Configurazione soggetto', 
                table = 'pn.sog',
                #viewResource = 'View',
                formResource = 'FormCFG'
                )

    conf.thpage('!![it]Classi dei gruppi di registrazione', table = 'pn.rcgrpcls')


    # menu CONFIGURAZIONE - PDC / PDV / CDA
    conf_pdc = conf.branch('!![it]Piani: PDC - PDV - CDA')

    conf_pdc.thpage('!![it]Natura dei conti', table = 'pn.pdcnaturaconti')

    conf_pdc.thpage('!![it]Piani dei conti', table = 'pn.pdccod')
    #conf_pdc.thpage('!![it]...singoli conti', table = 'pn.pdcconto')

    conf_pdc.thpage('!![it]Piani delle voci', table = 'pn.pdvcod')
    conf_pdc.thpage('!![it]Piani dei centri', table = 'pn.cdacod')


    # menu CONFIGURAZIONE - IVA
    conf_iva = conf.branch('!![it]IVA')

    conf_iva.thpage('!![it]Codici IVA', table = 'pn.ivacod')


    # menu CONFIGURAZIONE - FATTURA ELETTRONICA
    conf_ftel = conf.branch('!![it]FATTURA ELETTRONICA')
    conf_ftel.thpage('!![it]natura codici IVa per Fattura Elettronica', 
                    table = 'ftel.iva_naturacodici')


    # menu CONFIGURAZIONE - ATECO
    conf_ateco = conf.branch('!![it]ATECO')
    conf_ateco.thpage('!![it]Codici ATECO', 
                    table = 'pn.atecocodice')
