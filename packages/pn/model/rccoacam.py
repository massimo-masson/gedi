#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# gedi: ge-stionale di-rezionale
# Strumenti per la gestione contabile, amministrativa, finanziaria,
# per il controllo di gestione e direzionale.
# Copyright (C) 2023 Massimo Masson
# 
# This program is dual-licensed.
# 
# Option 1:
# If you respect the terms of GNU GPL license, AND
# you agree to give the copyright for modifications or derivative work
# to the original author Massimo Masson, the GPL license applies.
# In this case:
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# 
# Option 2:
# If you do not agree with any of the statements in option 1, then
# a proprietary license applies. In this case, contact the author
# for a dedicated propietary license.
# 

class Table(object):
    def config_db(self, pkg):
        '''rccoacam: rilevazione contabile - riga contabilita' analitica

        Sviluppo righe rilevazione contabile dati "coa" contabilita' analitica
        dettaglio competenze "cam" competenza anno mese
        '''

        tbl = pkg.table('rccoacam', pkey='id', 
                        #pkey_columns='rc__id',     # 20250103 CANCELLARE
                        name_long="!![it]Riga contabilita' analitica",
                        name_plural="!![it]Righe contabilita' analitica",
                        caption_field='caption')

        self.sysFields(tbl, counter='rc__id')

        # foreign key to rc - testata registrazione
        rc__id = tbl.column('rc__id', dtype = 'A', size = '22',
                            name_long = '!![it]Testata',
                            unmodifiable=True,
                            validate_notnull = True
                            )
        rc__id.relation('pn.rc.id', mode = 'foreignkey',
                        relation_name = 'righe_rccoacam', 
                        onDelete = 'cascade')
        
        # la seguente colonna deve contenere l'id o pk o
        # codice univoco che consenta di riconoscere la riga
        # da parte del programma che la genera automaticamente.
        # lavora insieme alla chiave primaria di rc
        tbl.column('origine', dtype = 'A', size = '32',
                   name_long = '!![it]Origine riga',
                   )

        # la seguente colonna contiene la "firma" del programma
        # automatico che ha generato questa riga, o vuoto se
        # manuale (non metterla nei th_XXX !)
        tbl.column('origine_auto', dtype = 'A', size = '32',
                   name_long = '!![it]Riga automatica',
                   )

        # descrittiva opzionale mnemonica da parte
        # del programma automatico di generazione
        tbl.column('origine_desc', dtype = 'A', size = '256',
                   name_long = '!![it]Descr. da origine',
                   )

        tbl.column('desc', dtype='A', size=':256', 
                   name_long='!![it]Descrizione rilevazione', 
                   )

        # foreign key to pdccod - piano dei conti di riferimento
        pdccod__cod = tbl.column('pdccod__cod', dtype = 'A', size = ':32',
                                 defaultFrom='@rc__id.@sog__cod.pdccod__cod',
                                 name_long = '!![it]PDC',
                                 #unmodifiable=True,
                                 validate_notnull = True
                                 )
        pdccod__cod.relation('pn.pdccod.cod', mode = 'foreignkey',
                             relation_name = 'pdccod_rccoacam', 
                             onDelete = 'raise')
        
        # foreign key to pdcconto - conto
        pdcconto__id = tbl.column('pdcconto__id', dtype = 'A', size = '22',
                                  name_long = '!![it]Conto',
                                  #unmodifiable=True,
                                  validate_notnull = True
                                  )
        pdcconto__id.relation('pn.pdcconto.id', mode = 'foreignkey',
                              relation_name = 'pdcconto_rccoacam', 
                              onDelete = 'raise')

        # foreing key to cdacod - codice piano centri di analisi
        cdacod__cod = tbl.column('cdacod__cod', dtype='A', size=':32',
                                 defaultFrom='@rc__id.@sog__cod.cdacod__cod',
                                 name_long = '!![it]CDA cod.',
                                 #unmodifiable=False,
                                 validate_notnull=True,
                                 )
        cdacod__cod.relation('pn.cdacod.cod', mode='foreignkey',
                             relation_name='cdacod_rccoacam',
                             onDelete='raise'
                             )

        # foreing key to cdacentro - il centro di analisi
        cdacentro__id = tbl.column('cdacentro__id', dtype='A', size='22',
                                   name_long = '!![it]CDA',
                                   #unmodifiable=False,
                                   validate_notnull=True,
                                   )
        cdacentro__id.relation('pn.cdacentro.id', mode='foreignkey',
                               relation_name='cdacentro_rccoacam',
                               #one_one=True,
                               onDelete='raise'
                               )

        # foreing key to pdvcod - codice piano delle voci
        pdvcod__cod = tbl.column('pdvcod__cod', dtype='A', size=':32',
                                 defaultFrom='@rc__id.@sog__cod.pdvcod__cod',
                                 name_long = '!![it]PDV cod.',
                                 #unmodifiable=False,
                                 validate_notnull=True,
                                 )
        pdvcod__cod.relation('pn.pdvcod.cod', mode='foreignkey',
                             relation_name='pdvcod_rccoacam',
                             onDelete='raise'
                             )

        # foreing key to pdvvoce - la voce di analisi
        pdvvoce__id = tbl.column('pdvvoce__id', dtype='A', size='22',
                                 name_long = '!![it]Voce',
                                 #unmodifiable=False,
                                 # validate_notnull=True,
                                 )
        pdvvoce__id.relation('pn.pdvvoce.id', mode='foreignkey',
                               relation_name='pdvvoce_rccoacam',
                               #one_one=True,
                               onDelete='raise'
                               )

        tbl.column('dare_udc', dtype='N', size='12,2',
                   name_long='!![it]Dare', name_short='!![it]D',
                   #validate_notnull=True,
                   )

        tbl.column('avere_udc', dtype='N', size='12,2',
                   name_long='!![it]Avere', name_short='!![it]A',
                   #validate_notnull=True,
                   )

        tbl.formulaColumn('saldo_udc', 'COALESCE($dare_udc, 0) - COALESCE($avere_udc, 0)',
                          dtype='N', size='12,2',
                          name_long='!![it]Saldo', name_short='!![it]S')

        # competenza nella forma anno/mese: AAAAMM
        tbl.column('competenza_am', dtype='A', size = '6',
                   name_long='!![it]Competenza',
                   name_short='!![it]Comp.'
                   )
        
        # foreign key to divisione: default quella della testata registrazione
        divisione__id = tbl.column('divisione__id', dtype = 'A', size = '22',
                                   name_long = '!![it]Divisione', 
                                   name_short='!![it]Div',
                                   defaultFrom='@rc__id.divisione__id',
                                   #unmodifiable=True,
                                   validate_notnull = False
                                   )
        divisione__id.relation('pn.divisione.id', mode = 'foreignkey',
                               relation_name = 'divisione_rccoacam', 
                               onDelete = 'raise')
        
        tbl.aliasColumn('divisione_rc', '@rc__id.divisione__id',
                        name_long='!![it]Divisione testata reg.',
                        name_short='!![it]Div.tes.',
                        )

        # foreign key to commessa: default quella della testata registrazione
        commessa__id = tbl.column('commessa__id', dtype = 'A', size = '22',
                                  name_long = '!![it]Commessa', 
                                  name_short='!![it]Comm',
                                  defaultFrom='@rc__id.commessa__id',
                                  #unmodifiable=True,
                                  validate_notnull = False
                                  )
        commessa__id.relation('anag.commessa.id', mode = 'foreignkey',
                               relation_name = 'commessa_rccoacam', 
                               onDelete = 'raise')

        tbl.aliasColumn('commessa_rc', '@rc__id.commessa__id',
                        name_long='!![it]Commessa testata reg.',
                        name_short='!![it]Comm.tes.',
                        )
        
        tbl.aliasColumn('rcgrp__id', '@rc__id.rcgrp__id',
                        name_long = '!![it]Gruppo reg.',
                        name_short = '!![it]Gr.reg.',
                        )
        
        tbl.formulaColumn('caption', "'rccoacam riga: '||$_row_count",
                          name_long='!![it]Riga')
