#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    gedi = root.branch('GeDi')

    #gedi.webpage('Hello, gedi!', filepath='hello_gedi.py')

    # menu anagrafiche
    anagr = gedi.branch('!![it]Anagrafiche')

    # menu anagrafiche - ditte
    #anagr_ditte = anagr.branch('!![it]Ditte')
    anagr.thpage('!![it]Ditte',table='cogen.ditta_anagrafica')
    #anagr.thpage('!![it]clienti e fornitori',table='cogen.clifor_anagrafica')
    anagr.thpage('!![it]Clienti e fornitori',table='cogen.clifor_anagrafica')

    # menu configurazione
    config = gedi.branch('!![it]Configurazione')
    #config.thpage('!!__Conti', table='cogen.pdc_conto')
    #config.lookups('!![it]Tabelle lookup', lookup_manager='cogen')

    # configurazione globale, tabelle valide per tutte le ditte
    config_globale = config.branch('!![it]Globale')
    config_globale.thpage('!![it]Piani dei conti',table='cogen.pdc_anagrafica')
    config_globale.thpage('!![it]Codici IVA', table='cogen.iva_codice')

    # configurazione tabelle specifiche per ditta
    config_perditta = config.branch('!![it]Per ditta')
    config_perditta.thpage('!![it]Esercizi contabili', table='cogen.ditta_esercizio')
    config_perditta.thpage('!![it]Registri IVA', table='cogen.ditta_iva_registro')

    # menu configurazione - tabelle di sistema
    config_sistema = config.branch('!![it]Tabelle di sistema')
    config_sistema.thpage('!![it]Epilogo conti', 
                table='cogen.pdc_epilogo')
    config_sistema.thpage('!![it]Tassonomia conti',
                table='cogen.pdc_tassonomia')
    config_sistema.thpage('!![it]Tipi di registro IVA',
                table='cogen.iva_registro_tipo')
