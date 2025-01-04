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

from datetime import datetime, timedelta

def competenza_AAAAMM(data_da, data_a, importo_dare, importo_avere, includi_giorno_finale=True):
    '''Calcola la competenza in formato AAAAMM

    Restituisce una lista di periodi in formato AAAAMM, ciascuno dei quali
    con la proporzione calcolata in giorni di importo dare ed importo avere

    Se "includi_giorno_finale" True, (default) viene aggiunto il giorno finale al calcolo
    Se "includi_giorno_finale" False, il calcolo e' senza giorno finale
    (excel fa i conteggi differenza date SENZA il giorno finale, ma per tornare ai
    totale importo corretti il giorno finale e' necessario)
    '''

    #
    # controllo validita' parametri
    #
    if includi_giorno_finale:
        giorno_finale = 1
    else:
        giorno_finale = 0
    
    if importo_dare is None:
        importo_dare = 0
    else:
        importo_dare = float(importo_dare)

    if importo_avere is None:
        importo_avere = 0
    else:
        importo_avere = float(importo_avere)
    
    #
    # inizio procedura
    #
    data_da = datetime.strptime(data_da, '%Y-%m-%d')
    data_a = datetime.strptime(data_a, '%Y-%m-%d')

    totale_giorni = (data_a - data_da).days + giorno_finale

    risultati = []

    data_corrente = data_da
    while data_corrente <= data_a:
        # inizio e fine mese corrente
        inizio_mese = data_corrente.replace(day=1)
        fine_mese = (inizio_mese + timedelta(days=32)).replace(day=1) - timedelta(days=1)

        # se necessario limita fine mese a data_a
        if fine_mese > data_a:
            fine_mese = data_a

        # calcola numero di giorni mese corrente
        giorni_mese = (fine_mese - data_corrente).days + giorno_finale

        # calcolo proporzione importo per mese corrente
        importo_mese_dare = importo_dare * (giorni_mese / totale_giorni)
        importo_mese_avere = importo_avere * (giorni_mese / totale_giorni)

        # aggiunta risultato a lista
        risultati.append((inizio_mese.strftime('%Y%m'), 
                        importo_mese_dare, 
                        importo_mese_avere)
                        )

        # prossimo mese
        data_corrente = fine_mese + timedelta(days=1)

    return risultati
