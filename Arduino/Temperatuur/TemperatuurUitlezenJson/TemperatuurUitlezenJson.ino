#include <DHT.h>

#define DHTPIN1 7
#define DHTPIN2 8
#define DHTPIN3 9
#define DHTTYPE DHT11

DHT dht1(DHTPIN1, DHTTYPE);
DHT dht2(DHTPIN2, DHTTYPE);
DHT dht3(DHTPIN3, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht1.begin();
  dht2.begin();
  dht3.begin();
}

void loop() {

  bool measure = false;
  byte incomingByte;

  if (measure == false) {
    if (Serial.available() > 0) {
      incomingByte = Serial.read();
      measure = true;
    }
    // Small delay
    else {
      delay(10);
    }
  }

  // When measure == true then excecute this
  if (incomingByte == 0b10100101){
        // meten
        float t1 = dht1.readTemperature();
        float t2 = dht2.readTemperature();
        float t3 = dht3.readTemperature();

        float h1 = dht1.readHumidity();
        float h2 = dht2.readHumidity();
        float h3 = dht3.readHumidity();

        // Gemiddelde terug geven
        float gem_tem = (t1 + t2 + t3) / 3.0;
        float gem_hum = (h1 + h2 + h3) / 3.0;  

        //terugsturen van data in de vorm van handmatige json
        String data = "{\"temperatuur\":" + String(gem_tem) + ",\"luchtvochtigheid\":" + String(gem_hum) + "}";
        Serial.println(data);

        static measure = false;
  }
  else {
    static measure = false;
  }
}

/*
Wat leer ik hiervan?
  - Dat het aanpassen van script dat ik eerder maakte, dit best wel eenvoudig maakt
  - dat de sensoren niet precies zijn. Ze staan vlak naast elkaar maar geven toch andere waardens op. 
  float h2 = dth2.readHumidity();
  - documentatie opzoeken voor keywords: https://github.com/adafruit/DHT-sensor-library/blob/master/keywords.txt
  - bevenstaande was documentatie voor een andere library. Nu kijken hoe ik die library kan toeveogen.
  - kan library link via arduino IDE vinden

  - Voor data uitwisseling met andere apperaten devices is json slim.
*/
