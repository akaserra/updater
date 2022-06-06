### UPDATER

**Come funziona l'updater.py**

L'updater è uno script molto utile, che ha come principale utilizzo, quello di far installare automaticamente agli utenti gli aggiornamenti dei vostri progetti.

**Le dipendenze**

L'updater funziona solo se è stato collegato ad una vostra repository e funziona tramite delle raw:
![image](https://user-images.githubusercontent.com/105589680/172217284-f8a5bef2-8345-4e1a-a638-10c23eeaaba2.png)

**Cosa potete modificare**

Nel file **Version.txt** dovete solo mettere la versione e ogni volta che modificate quel valore lo dovete modificare anche qui:
![image](https://user-images.githubusercontent.com/105589680/172217749-60222056-7f49-4eb5-a57d-c8c1f2b696a2.png)

Nel file **Changelogs.txt** dovete semplicemente mettere i cambiamenti del vostro progetto.

Nel file **updater.py** potete cambiare i messaggi e i link nelle variabili che iniziano con `FILE_`

_Non modificate il resto almeno che non sappiate ciò che fate!_

```
P.S. i vostri progetti possono essere con qualsiasi linguaggio, quindi non devono essere per forza in Pyhton. 
L'importate è che non modifichiate il nome dei file che installerete da questa Repository!
```

Per maggiori informazioni entrate qui: https://discord.gg/kUvd982grX e aprite un Ticket per ricevere supporto
