from datetime import datetime, timedelta

def competenzaAAAAMM(data_da, data_a, importo_dare, importo_avere, includi_giorno_finale=True):
    '''Calcola la competenza in formato AAAAMM

    Se "includi_giorno_finale" True, (default) viene aggiunto il giorno finale al calcolo
    Se "includi_giorno_finale" False, il calcolo e' senza giorno finale
    (excel fa i conteggi differenza date SENZA il giorno finale, ma per tornare ai
    totale importo corretti il giorno finale e' necessario)
    '''

    if includi_giorno_finale:
        giorno_finale = 1
    else:
        giorno_finale = 0
                
    data_da = datetime.strptime(data_da, '%Y-%m-%d')
    data_a = datetime.strptime(data_a, '%Y-%m-%d')

    totale_giorni = (data_a - data_da).days + giorno_finale

    print(f"totale_giorni = {totale_giorni}")

    risultati = []

    data_corrente = data_da
    while data_corrente <= data_a:
        # inizio e fine mese corrente
        inizio_mese = data_corrente.replace(day=1)
        fine_mese = (inizio_mese + timedelta(days=32)).replace(day=1) - timedelta(days=1)

        # se necessario limita fine mese a data_a
        if fine_mese > data_a:
            fine_mese = data_a

        print(f"Periodo da {inizio_mese} a {fine_mese}")
        
        # calcola numero di giorni mese corrente
        giorni_mese = (fine_mese - data_corrente).days + giorno_finale

        # calcolo proporzione importo per mese corrente
        importo_mese_dare = importo_dare * (giorni_mese / totale_giorni)
        importo_mese_avere = importo_avere * (giorni_mese / totale_giorni)

        print(f"giorni mese = {giorni_mese}; importo mese dare = {importo_mese_dare}; importo mese avere = {importo_mese_avere}")

        # aggiunta risultato a lista
        risultati.append((inizio_mese.strftime('%Y%m'), importo_mese_dare, importo_mese_avere))

        # prossimo mese
        data_corrente = fine_mese + timedelta(days=1)

        print('')

    return risultati
