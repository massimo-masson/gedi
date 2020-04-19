#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('ditta_iva_registro', pkey='id', 
                    name_long='!![it]Registro IVA', 
                    name_plural='!![it]Registri IVA',
                    caption_field='descrizione')
        self.sysFields(tbl)

        codice = tbl.column('codice', size=':22', name_long='!![it]Codice')
        
        descrizione = tbl.column('descrizione', size=':128', 
                    name_long='!![it]Descrizione', name_short='!![it]Desc.')   
        
        # anagrafica ditta di riferimento
        ditta_anagrafica = tbl.column('ditta_anagrafica_id', size='22', 
                    name_long='!![it]Ditta', 
                    validate_notnull=True)
        ditta_anagrafica.relation('cogen.ditta_anagrafica.id', 
                    relation_name='registri_iva', mode='foreignkey', 
                    onDelete='cascade')
        
        # tipologia di registro IVA (a credito o a debito)
        registro_tipo = tbl.column('iva_registro_tipo_id', size='22', 
                    name_long='!![it]Tipo registro IVA', name_short='!![it]Tipo',
                    validate_notnull=True)
        registro_tipo.relation('cogen.iva_registro_tipo.id', 
                    relation_name='registri_iva', mode='foreignkey', 
                    onDelete='raise')
        registro_tipo_descrizione = tbl.aliasColumn('iva_registro_tipo_descrizione',
                    relation_path='@iva_registro_tipo_id.descrizione',
                    name_long='!![it]Descrizione registro')
        
        # segno del registro
        registro_segno = tbl.aliasColumn('iva_registro_segno',
                    relation_path='@iva_registro_tipo_id.segno',
                    name_long='!![it]IVA credito/debito')
