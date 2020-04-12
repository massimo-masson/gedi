#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('pdc_anagrafica', pkey='id', 
                name_long='!!Anagrafica piano dei conti',
                name_plural='!!Anagrafiche piani dei conti',
                caption_field='codice')

        self.sysFields(tbl)

        codice=tbl.column('codice', dtype='A', size=':15', 
                name_long='!!Codice pdc',
                unique=True, validate_notnull=True, indexed=True)

        descrizione=tbl.column('descrizione', dtype='A', size=':64', 
                name_long='!!Descrizione pdc', 
                validate_notnull=True)

        note=tbl.column('note', dtype='A', size=':255', 
                name_long='!!Note')
