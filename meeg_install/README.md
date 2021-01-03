# portable-meeg
portable version of MEEG system

# Installazione della versione pubblica 6.0 del sistema MEEG (fixata)
1. Scaricare e installare la versione 3.8 del software `ampps` scaricando il file da [qui](https://macdownload.informer.com/ampps/)
2. Scaricare e scompattare il sistema `meeg` pre-configurato da [qui](https://u.pcloud.link/publink/show?code=XZYXTQXZQMRG370Ls6S0p9oU6Y8HWbjpeb5V)
3. Copiare la sottocartella `meeg` che si trova nella cartella appena scompattata e posizionarlo in `/Applicazioni/AMPPS/www`
4. Aprire l'applicazione `Ampps.app` che si trova in `/Applicazioni/AMPPS`; comparirà una finestra con 3 componenti attive (*running*): `Apache`, `PHP` e `MyAQL`. Tutte e 3 le componenti **devono** essere attive, se non lo sono andare al punto 1 della sezione Troubleshooting.
5. Verificare la versione di PHP, che dovrebbe essere la 7.1 (o qualcosa del genere). A noi serve la versione 5.4, quindi bisogna installarla e attivarla. Per fare ciò andare, in `ampps`, su `option`, cioè l'icona più a sinistra fra le 4 disponibili nella finestra. Da lì andare su `change php version`; si aprirà una nuova finestra con alcune versioni di PHP disponibili. La versione 5.4 è `disattiva`, significa che va installata. Fare click su `PHP 5.4` e seguire i passaggi dell'installazione. Dopo l'installazione attivare PHP 5.4.
6. A questo punto dovremmo avere Apache, PHP 5.4 e MySQL attivi e con le versioni giuste. Fare click sulla finestra `HOME` (la terza icona) in modo da aprire nel browser il `pannello di controllo` del server, in cui compaiono una serie di applicazioni identificate da relative icone.
7. Aprire l'applicazione `phpMyAdmin`, che permette di gestire il database.
8. Nella finestra di `phpMyAdmin` andare su `Utenti` (mi riferisco alla versione italiana, ma è tutto facilmente intuibile anche in inglese). Premere su `aggiungi utente`.
9.  Nella nuova finestra inserire il nome utente: `antonio` e la password `francesco`. Poi nella sezione in basso, su `Privilegi globali` premere su `seleziona tutti`. Infine premere, in basso a sinistra, su `Esegui`.
10. Tornare alla finestra del `pannello di controllo`, quello che avevamo aperto al punto (7) e aprire l'applicazione `add Domain`
11. In corrispondenza della voce `Domain` scrivere `my.meeg`, mentre in `Domain Path` scrivere: `/Applications/AMPPS/www/`, quindi premere `Add Domain`
12. A questo punto la configurazione è terminata. Andare sull'icona di `ampps` in alto (vicino all'orologio) e dal menu a tendina che si apre al click del mouse andare su `Restart`. Attendere qualche secondo.
13. Aprire una nuova finestra del browser e scrivere nella barra degli indirizzi: `my.meeg`, se tutto funziona dovrebbe aprirsi l'interfaccia del sistema MEEG perfettamente funzionante.

## Troubleshooting
1. Se una o piu componenti del server di `ampps` non dovessero essere in *running* (e quindi trovarsi in stato di *stopping*) la causa più comune risiede nella possibilità che ci siano delle istanze attive di uno dei servizi di interesse. Procedere come segue:
   * Dall'icona di `ampps` vicino all'orologio premere su `Stop`
   * Aprire `Monitoraggio Attività` del Mac e cercare eventuali servizi attivi attinenti a: php, apache, httpd e mysql(d). Se ci sono, ucciderli (uno ad uno) selezionandoli e andando sulla `x` in alto a sinistra.
   * Riaprire `Ampps.app` e verificare che tutto funzioni.  
