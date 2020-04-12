#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('pdc_conto', pkey='id', 
                name_long='!!Conto',
                name_plural='!!Conti',
                caption_field='codice')

        self.sysFields(tbl)

        codice=tbl.column('codice', dtype='A', size=':15', 
                name_long='!!Codice conto',
                unique=True, validate_notnull=True, indexed=True)

        # pdc_codice: chiave esterna per la relazione con pdc_anagrafica
        # di riferimento
        codice_pdc=tbl.column('pdc_codice', dtype='A', size=':15',
                name_long='!!Piano dei conti',
                validate_notnull=True)
        codice_pdc.relation('cogen.pdc_anagrafica.codice', mode='foreignkey',
                relation_name='conti',
                onDelete='raise')

        descrizione=tbl.column('descrizione', dtype='A', size=':64', 
                name_long='!!Descrizione conto', 
                validate_notnull=True)

        note=tbl.column('note', dtype='A', size=':255', 
                name_long='!!Note')
