Package ftel: "fattura elettronica"
===================================

Funzioni e struttura
--------------------

Il package **ftel** raccoglie tabelle e funzioni
collegate alla gestione della fatturazione elettronica.

Tabella: iva_naturacodici
-------------------------

Contiene l'elenco dei codici ministeriali in caso di
non applicabilita' dell'IVA.

Ai fini della fatturazione elettronica i codici IVA su cui non 
si applica l'IVA devono avere un codice che rappresenta la nautra IVA.
Ad esempio:
- N1   "escluse ex art. 15"
- N2.1 "non soggette ex artt. 7 - 7-septies DPR 633/72"
- N2.2 "non soggette - altri casi"
- [...]
