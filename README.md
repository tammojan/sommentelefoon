# Sommentelefoon
*T65-telefoon + raspberry pi = sommentelefoon*

## Idee
Het idee is simpel: iets leuks en leerzaams doen met een oude draaischijftelefoon. De hardware hiervan is zo simpel dat ik het zelfs begrijp.

De telefoon geeft (door de hoorn) een sommetje, en je moet het antwoord geven door het te draaien met de draaischijf. De telefoon zegt 'goed' of 'fout', en geeft de volgende som.

Dit project heeft mij twee avonden gekost, en m'n dochter van 5 is er erg blij mee.

## Hoe maak je dit?

### Hardware
* Een oude draaischijftelefoon, type T65
* Een raspberry pi
* Stukjes kabel
* Een 3,5 inch audio-plug

Haal voor de zekerheid de kabel met de telefoonstekker van de telefoon af, hij hoeft niet meer aan het net. Dit voorkomt schade aan de raspberry.

De connectors van de speaker van de hoorn (blauw en rood) kun je verbinden aan twee aders die naar de 3,5  inch audio-plug gaan. Deze gaat vervolgens in de audio-uitgang van de raspberry pi.

Voor de pulsteller zitten binnen voor in de telefoon contactpunten. Bij elke puls wordt er contact gemaakt tussen blauw en geel. Verbind deze met twee GPIO-pinnen in de raspberry, pinnen 3 en aarde (of in een andere nummering, pin 5 en 6; het is het derde pinnetje boven en onder).

### Software
Installeer de software bijvoorbeeld in `/home/pi/sommentelefoon` op de raspberry.

Om het programma automatisch te starten, voeg je de volgende regel toe aan `/etc/rc.local` (voor de regel met `exit 0`):

```
sudo amixer sset PCM,0 90% && python /home/pi/sommentelefoon/quiz.py &
```

Het eerste stuk van dit commando zet het volume op 90%.

### Starten
Zet de raspberry aan (hij moest dus tot dit punt uit staan). Na ongeveer een minuut moet er nu een som door de hoorn klinken.

## To-do
* Software mooier maken
* Aansluitingen voor het hoorncontact maken
* Meer sommen toevoegen (ook vermenigvuldigingen en delingen)
* Meer spelletjes bedenken die je met de draaischijf kunt bedienen
