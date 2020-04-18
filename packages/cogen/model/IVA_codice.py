#!/usr/bin/python3
# -*- coding: utf-8 -*-

# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('IVA_codice', pkey='id', name_long='!![it]Codice IVA', 
                    name_plural='!![it]Codici IVA',caption_field='descrizione')
        self.sysFields(tbl)

        # sigla sintetica e descrizione
        sigla = tbl.column('sigla', size=':22', name_long='!![it]Sigla')
        descrizione = tbl.column('descrizione', size=':128', 
                    name_long='!![it]Descrizione', name_short='!![it]Desc.')   
        
        aliquota = tbl.column('aliquota', dtype='N',
                    name_long='!![it]Aliquota', name_short='%')