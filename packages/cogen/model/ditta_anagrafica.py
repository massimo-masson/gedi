#!/usr/bin/python3
# -*- coding: utf-8 -*-

# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('ditta_anagrafica', pkey='id', 
                    name_long='!![it]Anagrafica ditta', 
                    name_plural='!![it]Anagrafiche ditte',
                    caption_field='descrizione')
        self.sysFields(tbl)

        codice = tbl.column('codice', size=':22', name_long='!![it]Codice')
        
        descrizione = tbl.column('descrizione', size=':128', 
                    name_long='!![it]Descrizione', name_short='!![it]Desc.')   
        
        partita_iva = tbl.column('partita_iva', size=':22', 
                    name_long='!![it]Partita IVA', name_short='!![it]P.IVA')

        codice_fiscale = tbl.column('codice_fiscale', size=':22', 
                    name_long='!![it]Codice Fiscale', name_short='!![it]Cod.Fisc.')