# Agente predittivo nell’ecosistema competitivo di Pokémon

Progetto per esame di Ingegneria della Conoscenza presso l'Università di Bari, anno 2023/2024.
La documentazione prodotta è presente in `doc/Documentazione.pdf`.

Per poter eseguire gli esperimenti di apprendimento supervisionato, eseguire il seguente comando a partire dalla root directory del progetto:

```
python ./supervised_learning.py
```

**ATTENZIONE**: L'esecuzione di `supervised_learning.py` andrà a sovrascivere i plot nella cartella `./plots`. Sono disabilitati (commentati), inoltre, l'esecuzione degli esperimenti del regressore logistico e dell'applicazione dell'oversampling. Per abilitare anche quelli basta decommentare dalla riga 218 alla riga 226. In generale l'esecuzione di `supervised_learning.py` richiede molto tempo.

Per poter eseguire gli esperimenti sulla rete bayesiana, eseguire il seguente comando a partire dalla root directory del progetto:

```
python ./bayesian_network.py
```