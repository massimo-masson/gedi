#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('pdc_tassonomia', pkey='id', 
            caption_field='descrizione',
            name_long=u'!![it]Tassonomia conti')

        self.sysFields(tbl, hierarchical='descrizione')

        tbl_descrizione = tbl.column('descrizione', size=':64',
            name_long=u'!![it]Descrizione', name_short=u'!![it]Desc')

        tbl_epilogo_id = tbl.column('pdc_epilogo_codice', size='22',
            validate_notnull=True, name_long=u'!![it]Epilogo')
        tbl_epilogo_id.relation('cogen.pdc_epilogo.id', mode='foreignkey',
            relation_name='epiloghi',
            onDelete='raise')
        
        tbl_note = tbl.column('note', size=':256', name_long=u'!![it]Note')