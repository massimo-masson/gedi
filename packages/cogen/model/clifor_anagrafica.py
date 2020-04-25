#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('clifor_anagrafica', pkey='id', 
                    name_long='!![it]Anagrafica clienti e fornitori', 
                    caption_field='ragione_sociale')
                    ###partition_ditta_anagrafica_id='ditta_anagrafica_id')

        self.sysFields(tbl)

        codice = tbl.column('codice', size=':22', name_long='!![it]Codice')
        
        descrizione = tbl.column('ragione_sociale', size=':256', 
                    name_long='!![it]Ragione sociale', 
                    name_short='!![it]Rag.Soc.')

        is_cliente = tbl.column('is_cliente', dtype='B', 
                    name_long='!![it]Cliente', name_short='!![it]Cli')

        is_fornitore = tbl.column('is_fornitore', dtype='B', 
                    name_long='!![it]Fornitore', name_short='!![it]For')

        descrizione = tbl.column('descrizione', size=':256', 
                    name_long='!![it]Descrizione', name_short='!![it]Desc.')   
        
        # anagrafica ditta di riferimento
        ditta_anagrafica = tbl.column('ditta_anagrafica_id', size='22', 
                    name_long='!![it]Ditta', 
                    validate_notnull=True)
        ditta_anagrafica.relation('cogen.ditta_anagrafica.id', 
                    relation_name='clientifornitori', mode='foreignkey', 
                    onDelete='cascade')