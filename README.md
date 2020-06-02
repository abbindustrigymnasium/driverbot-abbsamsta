# driverbot-abbsamsta

## Plan

- Styrning:
  - HTML
    - Range sliders
    - Mätare
    - Reverse knapp
    - Reset knapp
  - MQTT
    - Publisher på hemsidan
    - Subscriber i arduino
- Konstrukton
  - CADa och printa
    - Servo hållare
    - NodeMCU hållare
    - Batteri hållare
    - TT-motor hållare
    - 90 Graders kugghjul
    - TT-motor kugghjul

## Hemsidan

För att styra RC-bilen så har jag gjort en [hemsida](https://github.com/abbindustrigymnasium/driverbot-abbsamsta/blob/master/index.html) som använder sig av MQTT för att kommunicera med bilen. Styrningen består främst av två "range sliders". Den vänstra styr bilen riktining då vänster på slidern betyder att bilen kommer åka vänster o.s.v. Den högra är hastigheten där längst ner är stillastående och längst upp är maxfarten. 
I koden finns det en funktion för varje slider som uppdatera värdet som syns på mätarens i realtid och det värde som senare ska skickas iväg till bilen. En annan funktion märker när man släpper själva slider som då skickar iväg en de uppdaterade värdena till bilen.
Den stora röda knappen är för att omedelbart stoppa bilen och återställa hemsidan. 

![RC-image](https://github.com/abbindustrigymnasium/driverbot-abbsamsta/blob/master/assets/hemsidan.PNG?raw=true)

För att skicka iväg värden till bilen har hemsidan en publisher som skickar ut värden till en topic jag satt upp till just detta projekt. I bilens arduinokod finns då en subscriber som tar emot dess värden. Värdet som skickas iväg består av 7 siffror. Den första siffran är 0  eller 1 där 0=framåt och 1=bakåt. Den andra till 5e siffran är hastigheten. Eftersom TT-motorn jobbar med siffron mellan 0 och 1023 så kommer siffrorna som skickas iväg vara mellan 0000 till 1023. Slutligen så är de tre sista siffrorna graderna på hur mycke servon ska vridas.

## Konstruktionen
[Lista på alla delar gjorda i CAD. (Går att visas i github)](https://github.com/abbindustrigymnasium/driverbot-abbsamsta/tree/master/CAD)

Jag ville att min RC-bil skulle vara så modulär som möjligt. Därför består bilen främst av två balkar med 5 pluppars mellanrum där man kan sätta på vilken komponent som helst. NodeMCU kortets hållare, batterihållaren och servo-hållarens fästa består av 5 pluppars mellanrum för att matcha balken. Hela framdelen som styr framhjulens rikting är som en komponent som går att ta av och sätta på genom ett fästa som återigen består av 5 pluppars mellanrum. Bakdelen som styr bakhjulens hastighet fungerar på samma sätt.

Något som också är modulärbart är själva hållarna. Enheterna är lätta att ta ut ur och sätta i hållaren om det skulle behövas.

Som man ser på bilden längst till höger så fungerar servon som en ratt genom kugghjulet som endast är 90 grader brett. Det är för att inte ta onödigt plats och inte slösa på plast. Legobiten som går i sidled behöver inte röras så mycke och därför behövs inte ett helt 360 graders hjul. Kugghjulet till TT-motorn består dock 360 grader eftersom den ska kunna rulla så länge som möjligt.

<img src="https://github.com/abbindustrigymnasium/driverbot-abbsamsta/blob/master/assets/IMG_3803.jpg" width="24%"></img> <img src="https://github.com/abbindustrigymnasium/driverbot-abbsamsta/blob/master/assets/IMG_3805.jpg" width="24%"></img> <img src="https://github.com/abbindustrigymnasium/driverbot-abbsamsta/blob/master/assets/IMG_3837.GIF" width="26%"></img> <img src="https://github.com/abbindustrigymnasium/driverbot-abbsamsta/blob/master/assets/IMG_3851.GIF" width="22%"></img>

## Förbättringar

#### Gjorda 
- Valet att göra den så modulär som möjligt kom efter att jag märkt att jag hade väldigt begränsat antal legobitar hemma. Bilen skulle då vara så enkelt att bygga på som möjligt och enkel att printa delar till
- Kugghjulen är printade. Av samma anledning som tidigare så behövde jag printa för att göra ha ett kugghjul som passade bra till de andra delarna jag hade.

#### Möjliga
- Ett mindre batteri hade gjort den mycket mer kompakt.
- Något form av chassi så den slipper se ut som en naken RC bil.
- Möjliggöra för live uppdatering av slider så att man inte behöver släppa slider för att bilens rörelse ska ändras.
- Testa och möjligtvis förbättra sytrnig via mobil.

