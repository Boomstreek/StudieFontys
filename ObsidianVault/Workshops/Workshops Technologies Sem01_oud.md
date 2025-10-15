# Les 1 
Deze les heb ik gemist, daar ging iets mis met de opname en ik was niet live aanwezig bij de les.
[[Workshops Technologies Sem01]]
# Les 2
Les 2 vond ik vrij saai. Ging volgens mij over de delay inbouwen bij een button. 

# Les 3
Hier begon het bij mij te klikken. Wat doet Void setup (initaliseren / opstarten van de hardware / programma) en wat doet Void loop (Dat wat de hardware continu doet, vandaar loop)

We zijn een lampje gaan laten branden, we hebben het gehad over millis() en nog meer praktische dingen

dit zijn mijn aantekeningen, zonder inhoud te verliezen maak dit een beetje mooi chatgpt
Arduino Les 3

Vorige keer delays voor button ingebouwt, maar dat wil je liever niet
  - tijdens delay doet programme nisk nuttigs, wacht gewoon

  Tinkercad, autocad waar je via computer kan schetsen met arduino onderdelen.

  void setup() is de setup

  void loop() hier komt de daadwerkelijk code. setup is dus alleen de voorbereiding hiervoor.

  Functie, tijd sinds arduino aanstaat
    - arduino millis gegoogled
        - krijg je millis() docs
        - unsigned is alleen positieve getallen. bijv. unsigned long is een 32 bit getal, int is 16 bit bij arduino. verschilt per chip

millis is hudiige tijd en zet daar 1000ms bij

bool buttonispressed -= false;

const int LED_PIN< output = 8;
const int BTN_PIN = 6;

unsigned long

hoe weet je waar welke code je moet neerzetten? Variable boven, wat in voud setup en wat in loop, is daar een ezelsbrugetje voor?

setup is code die alleen aan het begint wilt runnen, loop is continu. Varable die in loop en setup wil gebruiken, moeten erbuiten staan

static; de eerste keer dat compiler het tegen komt, dan voort die hem uit. 2de keer doet die het niet.

arduino aangeven dat het input of output is
serial .begin moet zelfde bitrate hebben

input_pullup, als hij ingedrukt is die low en bij niet high, high is 5v

hoe wordt millis() berekend? sinds applicatie aan staat

milis() huidige tijd, toevoegen anders werk je in het verleden.

hoe voeg je libray toe:
tools manage librays
anologe pin uitlezen

Koop arduino in china, goedkoper. Let op dat het wel een compatible chip is Atmega86 of zo iets
einde

# Les 4
Les 4 State Diagram
bounce liefst oplossen via condencator
en als dat niet kan, dan via software

Opnieuw beginnen, we gaan naar de tekentafel. draw.io
  - blank diagram

State diagram, wacht echt op bepaalde gebeurtenissen. Events willkeurig
  - legt verschil uit tussen flow chart en statediagram

  booleans geeft chaos en daardoor bugs, wordt een drama
  - zie je wel veel in de praktijk
  - dit nog eens nazoeken

begin toestand, zwart cirkeltje
Achter / in de tekst komt water gedaan moet wordne

Rest van de diagram heeft waar het op wacht en wat het doet. 

De acties gaat hij nu met [] doen, bijvoorbeeld [millis() > GreenOnTime] / (/ zijn de acties als de [] transitie plaats vindt) GreenLed(on)

[milis90 > GreenOnTime && ButtonReleaser]/ 
GreenLed(on);


ButtonPressed/
calculateReactieTime();
greenLedOff();

Dan wachten totdat knopje los laat

ButtonReleaser/
GreenOnTime = millis() + random(2000);

invarianten? wat zijn dit opzoeken

Moeilijk vershil qua denken , flowchart en state diagram

VSCode vult beter aan,proffesioneler

void setup()

enum STATE

{
  WAIT_ON_GREEN_LED,
  WAIT_ON_BTN_PRESSED,
  WAIT_ON_BTN_RELEASED
};

void loop()

static STATE currentState = WAIT_ON_GREEN_LED;

switch (currentState) // slimmer if else statment
{
  case WAIT_ON_GREEN_LED:
  if digitaleRead(BTN_PIN == LOW
  {
    currentState = WAIT BTN RELASEED
  }
    else if (millis() > greenOnTime)
    {
      digitalWrite(GREEN_LED_PIN, HIGH);
      currentState = WAIT_ON_BTN_PRESSED;
    }
    break;
  case WAIT_ON_BTN_PRESSED:
      if (digitalRead(BTN_PIN) == LOW)
      {
          serial print
          led uitzetten
          currentState = WAIT_ON_BRN_RELEASED;
      }
    break; 
  case WAIT_ON_BTN_RELEASED:
      if digitalread btn pin == high // pull up , knop uit is high
      {
          greenontime = milis random
          currentState + WAIT_ON_GREEN_LEDl
      }
    break;
}

Wat je heel vaak ziet, vaak denk je dat je het wel kan doen met een boolean, maar case werkt overzichtelijker

communicatie tussen divces $bericht:argument:# bijv. Hiervoor toestanden, case, gebruikenplaatje helpt, diagram, met code te lezen
  - geen booleans. Nu bij wijziging terug naar tekening , stae diagram, en dan weer nieuwe states maken

# Les 5
vragen solderen? Edwin vragen snel cursus solderen
defecte arduino

#class Button

class is een blauwdruk van een object, wordt pas een object als een constructor oproept. Zelfde naam als class

Breadbord weerstand pulldown maken, opzoeken

Constructor, class blue print

class heeft x aantal methodes(functies) en data(attributen) alles bij elkaar zijn members. 
Welke methodes zijn publiek en welke private.

Constructor wat je initialiseeert, meer van opzoeken

Object maken 
static Button btn(BTN_PIN);

btn.IsPressed()
of
!btn.IsPressed()

#Bit manipulatie
registers manipulatie, dat zit in de microcontroller
Wat kunnen we ermee doen:
- bitjes lezen, bitjes zetten en togglen

<<
??
&
|
^
nog iets

Bitwise left shit (<<)
alle bitjes in een byte schrijft 2 plekken naar link, wat eruit schrijft is weg en rechts komen nuller erbij.

vermedigvuldige met 2, 4, 8, 16 per 1, 2, 3, 4 stappen

Bitwise right sift (>>)
zelf als left shift maar andersom

hier dan delen

Bitwise AND (&)
Beide 1 dan pas een 1

Bitwise OR (|)
als 1 vna beide 1, dan is resultaat 1

Bitwise XOR (^)
exlusive or, als 1 van beide is 1, dan 1, beide 1 dan 0 ,beide 0 dan 0

Bitwise complement (~)
alles omklappen 1= 0 0 = 1

Dit om geheugen te besparen, want soms gebruiken meerdere functies dezelfde bits

0b1000; = 0b00001000, alles links wordt aaangeveuld met nulletjes

Bitjes wil j lezen, schrijven en omzetten, dat wil je ermee doen

read voorbeeld gehad

scrhijven, eerst wat je wilt schrijven 0 maken en dan schrijven wat je er wilt hebben
nul maken, wat wil je hebben, op jusit plek zetten en dan erin zetten

omklappen, mask en dan xor

1 regel code in de praktijk, nu uitgelegd via vee lstpappen

## Arduino
Arduino heeft een aantal registers

voor Port B, heeeft een aantal registor, voor I&O 3

DDRB 1 = output en 0 is input
dus zet pitjes voor data direction

pinntjes hoog of laag voltage 0 of 1

op bit niveau werken maakt het programme sneller ipv librarys

zowel compiler als applicatie wordt een stuk sneller

pb0 

DDRB = DDRB & 0b11111110;
(via and blijft een 1 een 1 maar laatste bit is sowieso 0 nu)
PORTB = PORTB & | 0b00000001;

lastReading = PINB $ 0b1; (dit pakt het meeste rechtste bitje)

Cryptografie doen ze dit veel 

ppt, nieuwe code erin
