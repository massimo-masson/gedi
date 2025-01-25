GeDi: il Gestionale Direzionale
===============================

GeDi = Ge(stionale) Di(rezionale)
Il suo scopo e' quello di supportare ed agevolare la consulenza
direzionale ed il controllo di gestione aziendale.

La funzione primaria e' la gestione di un sistema contabile con la
possibilita di gestire configurazioni contabili.

Le configurazioni contabili sono degli insiemi di registrazioni
contabili che, raggruppate in certi modi, offrono visioni dei risultati
e degli aggregati contabili differenti, ed eventualmente comparabili.

Ad esempio, un *gruppo di registrazioni* potrebbe rappresentare la 
contabilita' consuntiva.
Un ulteriore *gruppo di registrazioni* potrebbe rappresentare i movimenti
di forecast previsionale a fine anno.
Una **configurazione contabile** potrebbe consistere nel consuntivo effettivo
ad una certa data, sommato alle previsioni di forecast.

Uno scenario diverso potrebbe essere quello in cui al *gruppo di regisrazioni*
della contabilita' consuntiva viene sommato un primo "scenario", dato
dalle risultanze dell'impatto di una *simulazione di investimento* (gruppo 
di registrazione), o eventualmente di piu' simulazioni di investimenti, 
magari appoggiati su piu' *gruppi di registrazione*.
Le diverse **configurazioni contabili** consentono di ottenere diverse
risultanze, successivamente utilizzabili ai fini di analisi.

In modo "minimalista", uno scenario contabile potrebbe essere la
tradizionale contabilita' generale consuntiva.

Il programma puo' avere senso utilizzato in autonomia, per la gestione
contabile, così come puo' avere senso in simbiosi con altro erp
o software contabile, da cui viene alimentato periodicamente con appositi
**connettori** (da sviluppare specificamente per l'esigenza) per i
movimenti consuntivi effettivi, ed a cui vengono poi effettuate operazioni
quali:

- fast closing di periodo
- previsioni di forecast
- eventuali scenari
- budget e rolling budget
- ...altro...

Sottosistemi contabili
----------------------

E' previsto il sottosistema contabile in partita doppia metodo reddituale,
al quale viene aggiunto un sottosistema di gestione IVA.
E' immediatamente disponibile anche la possibilita' di gestire il 
sottosistema di contabilita' analitica con sviluppo per centri di analisi
e per commesse, sia sui conti di natura economica che su quelli di 
natura patrimoniale.

BI Friendly
-----------

Gli archivi sono strutturati su tabelle di db relazionale in modo da
risultare "Business Intelligence Friendly" per ampliare le possibilita'
di analisi.