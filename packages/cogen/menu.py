#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    gedi = root.branch('GeDi')

    # menu anagrafiche
    anagr = gedi.branch('!![it]Anagrafiche')

    # menu configurazione
    config = gedi.branch('!![it]Configurazione')
    config.thpage('!![it]Piani dei conti',table='cogen.pdc_anagrafica')
    #config.thpage('!!__Conti', table='cogen.pdc_conto')
    #config.lookups('!![it]Tabelle lookup', lookup_manager='cogen')
    config.thpage('!![it]Codici IVA', table='cogen.IVA_codice')

    # menu configurazione - sistema
    config_sistema = config.branch('!![it]Sistema')
    config_sistema.thpage(u'!![it]Tabella epilogo conti', 
                table='cogen.pdc_epilogo')
    config_sistema.thpage(u'!![it]Tabella tassonomia conti',
                table='cogen.pdc_tassonomia')
