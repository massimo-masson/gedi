#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('pdc_tassonomia', pkey='id', 
            caption_field='hierarchical_descrizione',
            name_long='Tassonomia conti')

        self.sysFields(tbl, hierarchical='descrizione')

        tbl_descrizione = tbl.column('descrizione', size=':64',
            name_long='Descrizione', name_short='Desc')

        tbl_epilogo_id = tbl.column('pdc_epilogo_codice', size='22',
            validate_notnull=True, name_long='Epilogo')
        tbl_epilogo_id.relation('cogen.pdc_epilogo.id', mode='foreignkey',
            relation_name='epiloghi',
            onDelete='raise')
        
        tbl_note = tbl.column('note', size=':256', name_long='Note')