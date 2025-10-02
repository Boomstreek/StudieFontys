#include <DHT.h> // nieuwe library

const int DHT11_PIN = 7;

int RED_LED = 10;
const int GREEN_LED = 9;
const int BUTTON_PIN = 2;

bool greenIsOn = false;
unsigned long greenOnTime = 0;
unsigned long greenStartDelay = 0;
unsigned long redBlinkTimeout = 0;

int lastButtonState = HIGH;

void setup() {
  Serial.begin(9600);
  pinMode (RED_LED, OUTPUT);
  pinMode (GREEN_LED, OUTPUT);
  pinMode (BUTTON_PIN, INPUT_PULLUP);

  digitalWrite(RED_LED, HIGH);
  digitalWrite(GREEN_LED, LOW);

  redBlinkTimeout = millis() + 1000;
  greenStartDelay = millis() + random(2000, 5000);
}

void loop() {
  // RED_LED laten knipper
  if (millis() > redBlinkTimeout)
  {
    digitalWrite(RED_LED, !digitalRead(RED_LED));
    redBlinkTimeout = millis() + random(2000, 10000);
  }

  // GREEN_LED laten knipper na willekeurige tijd
  if (!greenIsOn && millis() > greenStartDelay)
  {
    digitalWrite(GREEN_LED, HIGH);
    greenOnTime = millis();
    greenIsOn = true;
  }

  // knop uitlezen
  int buttonState = digitalRead(BUTTON_PIN);

  if (greenIsOn && lastButtonState == HIGH && buttonState == LOW)
  {
    unsigned long reactieTijd = millis() - greenOnTime;
    Serial.print("Reactietijd: ");
    Serial.print(reactieTijd);
    Serial.println(" ms");
/* oude library
  float chk = DHT.read11(DHT11_PIN); // weeet niet warom dit moet van documentatie. Lees in elk geval de sensor. Denk dat chk in de libray van DHT11 vandaan komt.
  Serial.print("Temperature = ");
  Serial.print(DHT.readTemperature);
  Serial.println(" Celcius");
  Serial.print("Humidity = ");
  Serial.print(DHT.readHumidity);
  Serial.println(" %");
*/
    digitalWrite(GREEN_LED, LOW);
    greenIsOn = false;
    greenStartDelay = millis() + random(10000, 50000);
  }

  lastButtonState = buttonState;
}

/*
Wat heb ik ervan geleerd. 
  - Dat het best nog wel lastig is
  - Dat de code zichzelf snel uitbreid, wordt snel groot, voor zoiets simpels al
  - Ik echt nog opnames, google en chatgpt nodig heb om zelfs zoiets simpels te maken.
      - Ik heb wel zelf alles overgetyped zodat ik moet weten wat er gebeurt en wat ik waar fout doe.
*/
