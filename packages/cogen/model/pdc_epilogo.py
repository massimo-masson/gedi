#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('pdc_epilogo', pkey='id',
            caption_field='codice',
            name_long='Chiusura')
        
        self.sysFields(tbl)

        tbl_codice = tbl.column('codice', size='2', 
            name_long='Codice', name_short='Cod', 
            unique=True, validate_notnull=True)

        tbl_descrizione = tbl.column('descrizione', size=':64',
            name_long='Descrizione', name_short='Desc')
