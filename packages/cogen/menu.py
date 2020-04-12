#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    gedi = root.branch(u'GeDi')

    # menu anagrafiche
    anagr = gedi.branch(u'!![it]Anagrafiche')

    # menu configurazione
    config = gedi.branch(u'!![it]Configurazione')
    config.thpage(u'!![it]Piani dei conti',table='cogen.pdc_anagrafica')
    config.thpage(u'!!__Conti', table='cogen.pdc_conto')
    config.lookups(u'!![it]Tabelle lookup', lookup_manager='cogen')
