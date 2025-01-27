.. GeDi documentation master file, created by
   sphinx-quickstart on Mon Jan 13 11:59:25 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GeDi - il Gestionale Direzionale
================================

Ha lo scopo di supportare ed agevolare la consulenza
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
- [...]

Sottosistemi contabili
----------------------

- Contabilita' generale in partita doppia
	- metodo reddituale
	- gestione IVA
- Contabilita' analitica
	- per natura (conti / voci)
	- per destinazione (centri di analisi / commesse)
	- su tutte le tipologie di conto (economici / patrimoniali)

INDICE
======

.. toctree::
   :maxdepth: 2
   :caption: Contenuti:

   manuale_utente
   pkg_pn
   pkg_anag
   pkg_ftel
