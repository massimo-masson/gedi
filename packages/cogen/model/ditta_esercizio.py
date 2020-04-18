#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('ditta_esercizio', pkey='id', 
                    name_long='!![it]Esercizio contabile', 
                    name_plural='!![it]Esercizi contabili',
                    caption_field='descrizione')
        self.sysFields(tbl)

        codice = tbl.column('codice', size=':22', name_long='!![it]Codice')
        
        descrizione = tbl.column('descrizione', size=':128', 
                    name_long='!![it]Descrizione', name_short='!![it]Desc.')   
        
        anno = tbl.column('anno', size=':22', name_long='!![it]Anno')

        # anagrafica ditta di riferimento
        ditta_anagrafica = tbl.column('ditta_anagrafica_id', size='22', 
                    name_long='!![it]Ditta', 
                    validate_notnull=True)
        ditta_anagrafica.relation('cogen.ditta_anagrafica.id', 
                    relation_name='esercizi', mode='foreignkey', 
                    onDelete='raise')
        
        # piano dei conti di riferimento
        pdc_anagrafica = tbl.column('pdc_anagrafica_id', size='22', 
                    name_long='!![it]Piano dei conti', name_short='!![it]PDC',
                    validate_notnull=True)
        pdc_anagrafica.relation('cogen.pdc_anagrafica.id', 
                    relation_name='esercizi', mode='foreignkey', 
                    onDelete='raise')