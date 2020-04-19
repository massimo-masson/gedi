#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('iva_registro_tipo', pkey='id',
                        caption_field='codice',
                        name_long='!![it]Tipo registro IVA')
        
        self.sysFields(tbl)

        tbl_codice = tbl.column('codice', size=':22', 
                        name_long='!![it]Codice', name_short='!![it]Cod.', 
                        unique=True, validate_notnull=True)

        tbl_descrizione = tbl.column('descrizione', size=':64',
                        name_long='!![it]Descrizione', name_short='!![it]Desc.')

        # segno versamento IVA: a credito o a debito
        # campo numerico da usare per moltiplicare il valore iva
        # +1 = a debito (ciclo attivo)
        # -1 = a credito (ciclo passivo)
        tbl_segno = tbl.column('segno', dtype='L', default=1,
                        name_long='!![it]Segno a credito (-1) o debito (+1)', 
                        name_short='!![it]+/-')