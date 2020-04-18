#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('pdc_anagrafica', pkey='id', 
                        name_long='!![it]Anagrafica piano dei conti',
                        name_plural='!![it]Anagrafiche piani dei conti',
                        caption_field='codice')

        self.sysFields(tbl)

        tbl_codice=tbl.column('codice', dtype='A', size=':15', 
                        name_long='!![it]Codice pdc',
                        unique=True, validate_notnull=True, indexed=True)

        tbl_descrizione=tbl.column('descrizione', dtype='A', size=':64', 
                        name_long='!![it]Descrizione pdc', 
                        validate_notnull=True)

        tbl_note=tbl.column('note', dtype='A', size=':255', 
                        name_long='!![it]Note')
