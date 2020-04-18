#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('pdc_conto', pkey='id', 
                        name_long='!![it]Conto',
                        name_plural='!![it]Conti',
                        caption_field='codice')

        self.sysFields(tbl)

        # colonna codice
        tbl_codice=tbl.column('codice', dtype='A', size=':15', 
                        name_long='!![it]Codice conto',
                        unique=True, validate_notnull=True, indexed=True)

        # colonna pdc_codice: chiave esterna per la relazione con pdc_anagrafica
        # di riferimento
        tbl_codice_pdc=tbl.column('pdc_codice', dtype='A', size=':15',
                        name_long='!![it]Piano dei conti',
                        validate_notnull=True)
        tbl_codice_pdc.relation('cogen.pdc_anagrafica.codice', mode='foreignkey',
                        relation_name='conti',
                        onDelete='raise')

        # colonna descrizione
        tbl_descrizione=tbl.column('descrizione', dtype='A', size=':64', 
                        name_long='!![it]Descrizione conto', 
                        validate_notnull=True)

        # colonna note
        tbl_note=tbl.column('note', dtype='A', size=':255', 
                        name_long='!![it]Note')

        # colonna tassonomia: FK
        tbl_pdc_tassonomia_id=tbl.column('pdc_tassonomia_id', size='22',
                        name_long='!![it]Tassonomia',
                        validate_notnull=True)
        tbl_pdc_tassonomia_id.relation('cogen.pdc_tassonomia.id', mode='foreignkey',
                        relation_name='tassonomia_conti',
                        onDelete='raise')

        # colonna imputabile: se vero rappresenta un livello di imputazione
        tbl_imputabile=tbl.column('imputabile', dtype='B',
                        name_long='!![it]Livello di input',
                        validate_notnull=True, default=False)