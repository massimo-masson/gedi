Package pn: "prima nota"
========================

Funzioni e struttura
--------------------

Il package pn e' il package principale.

Ha il compito di gestire le rilevazioni contabili e le configurazioni
di valori contabili degli scenari di simulazione.

Il concetto di simulazione contabile
------------------------------------

La simulazione contabile e' basata sul fatto che le righe di rilevazione
contabile sono caratterizzate da un codice di gruppo specifico, definibile
dall'utente.

Significa che l'utente puo' arbitrariamente creare un "gruppo di registrazioni"
che saranno successivamente visibili insieme ad altri gruppi, o singolarmente.

La possibilita' di aggregare piu' gruppi di registrazione viene definita 
"configurazione contabile". 
Una configurazione contabile quindi ha lo scopo di visualizzare piu' gruppi di
registrazione.

In questo modo si possono gestire piu' righe contabili, caratterizzate da
diversi gruppi di registrazione, ciascuno dei quali puo' rappresentare un diverso
scenario.

Esempio:
si sta predisponendo un budget, le cui rilevazioni potrebbero essere nel gruppo "bdg"
(esempio totalmente arbitrario).

Si vuole poi fare una ipotesi tipo what-if sull'impatto di un certo investimento, che 
viene definito in termini di rilevazione contabile con delle registrazioni appartenenti
al gruppo "bdg-inv01".

Una configurazione di valore con le sole rilevazioni "bdg" consentira' di ottenere i dati
del budget.
Una configurazione di valore con le rilevazioni "bdg" e le rilevazioni "bdg-inv01" invece
consentira' di ottenere i dati di budget con l'impatto contabile dello scenario con 
l'investimento 01.
Ovviamente, qualora ci fosse un investimento ulteriore, ad esempio "bdg-inv02", si potrebbero
predisporre diverse configurazioni contabili per tenere in considerazione uno solo o 
entrambi gli investimenti.

L'analisi comparativa di diversi scenari consentira' di sviluppare analisi WHAT-IF.

Suggerimento: le rilevazioni per i diversi scenari potrebbero essere singole (o poche)
rilevazioni "complesse", sviluppate su piu' righe.

Suggerimento: la classica contabilita' generale, consuntiva, metodo reddituale, non e' altro
che un caso particolare di uno scenario con un gruppo di rilevazioni singolo riferito al
consuntivo.

Funzioni contabili
------------------

Il sistema gestisce rilevazioni contabili con il metodo della partita doppia, sistema del reddito.
In verita' non ci sono specifici vingoli sul sistema del reddito.

La registrazione ha delle informazioni di "testata", cui si possono correlare:

- righe di contabilita' (dare avere), basate sul piano dei conti;
- informazioni su divisione e commessa. Queste possono poi essere specificate nei
dettagli di riga in modo piu' puntuale
- informazioni IVA (registri e codici)
- informazioni di contabilita' analitica:
    - per natura, con un dettaglio specifico di "voce". Questa correlazione e' di tipo 1:1 tra conto e voce
    - per destinazione, con un dettaglio specifico di "centro" e di "commessa". Questa relazione e'
    di tipo 1:n tra conto e centro/commessa
- informazioni sulle scadenze finanziarie
- indicazione del gruppo di registrazione (simulatore)


Struttura delle tabelle
-----------------------

Le tabelle sono organizzate per sigle, quelle che iniziano con la stessa radice si riferiscono
ad entita' correlate.

Ci sono tabelle di "impostazione e configurazione", ci sono tabelle "operative".

**rc**
La radice delle tabelle operative per le rilevazioni contabili e' *rc*, 
che sta per *rilevazione contabile*.
Questa tabella e' la testata di una serie di relazioni in cascata, tutte con prefisso rc

**rcrcg**
La prima relazione, di tipo 1:n, con la rilevazione contabile consiste nelle righe che
compongono la registrazione. rc **rcg** sta per **r** iga **c** ontabilita' **g** enerale.
