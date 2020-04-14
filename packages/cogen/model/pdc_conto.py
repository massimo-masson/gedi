#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('pdc_conto', pkey='id', 
                name_long=u'!![it]Conto',
                name_plural=u'!![it]Conti',
                caption_field='codice')

        self.sysFields(tbl)

        # colonna codice
        tbl_codice=tbl.column('codice', dtype='A', size=':15', 
                name_long=u'!![it]Codice conto',
                unique=True, validate_notnull=True, indexed=True)

        # colonna pdc_codice: chiave esterna per la relazione con pdc_anagrafica
        # di riferimento
        tbl_codice_pdc=tbl.column('pdc_codice', dtype='A', size=':15',
                name_long=u'!![it]Piano dei conti',
                validate_notnull=True)
        tbl_codice_pdc.relation('cogen.pdc_anagrafica.codice', mode='foreignkey',
                relation_name='conti',
                onDelete='raise')

        # colonna descrizione
        tbl_descrizione=tbl.column('descrizione', dtype='A', size=':64', 
                name_long=u'!![it]Descrizione conto', 
                validate_notnull=True)

        # colonna note
        tbl_note=tbl.column('note', dtype='A', size=':255', 
                name_long=u'!![it]Note')
