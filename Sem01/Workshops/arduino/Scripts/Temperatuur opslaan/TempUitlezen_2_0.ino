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

  float t1 = dht1.readTemperature();
  float t2 = dht2.readTemperature();
  float t3 = dht3.readTemperature();

  float h1 = dht1.readHumidity();
  float h2 = dht2.readHumidity();
  float h3 = dht3.readHumidity();

  // Gemiddelde terug geven
  float gem_tem = (t1 + t2 + t3) / 3.0;
  float gem_hum = (h1 + h2 + h3) / 3.0;

  // Gegevens printen naar serial
  Serial.print("Temperature 1= ");
  Serial.print(t1);
  Serial.println(" Celcius");
  Serial.print("Humidity 1= ");
  Serial.print(h1);
  Serial.println(" %");

  Serial.print("Temperature 2= ");
  Serial.print(t2);
  Serial.println(" Celcius");
  Serial.print("Humidity 2= ");
  Serial.print(h2);
  Serial.println(" %");

  Serial.print("Temperature 3= ");
  Serial.print(t3);
  Serial.println(" Celcius");
  Serial.print("Humidity 3= ");
  Serial.print(h3);
  Serial.println(" %");

  Serial.print("Temperature gemiddelde= ");
  Serial.print(gem_tem);
  Serial.println(" Celcius");
  Serial.print("Humidity gemiddelde= ");
  Serial.print(gem_hum);
  Serial.println(" %");
  Serial.println();

  delay(20000);
}
/*

10:27:32.088 -> Temperature 1= 21.40 Celcius
10:27:32.121 -> Humidity 1= 55.00 %
10:27:32.153 -> Temperature 2= 24.10 Celcius
10:27:32.186 -> Humidity 2= 41.70 %
10:27:32.186 -> Temperature 3= 21.50 Celcius
10:27:32.218 -> Humidity 3= 46.30 %
10:27:32.249 -> Temperature gemiddelde= 22.33 Celcius
10:27:32.283 -> Humidity gemiddelde= 47.67 %
10:27:32.316 -> 
10:27:52.352 -> Temperature 1= 21.40 Celcius
10:27:52.389 -> Humidity 1= 55.00 %
10:27:52.389 -> Temperature 2= 24.00 Celcius
10:27:52.415 -> Humidity 2= 41.50 %
10:27:52.447 -> Temperature 3= 21.50 Celcius
10:27:52.480 -> Humidity 3= 46.30 %
10:27:52.511 -> Temperature gemiddelde= 22.30 Celcius

kwaliteit verschil tussen sensoren is groot. 
nogmaals testen, wellicht dat mijn arm tedichtbij die ene sensor zat. nu ik de sensor dichterbij de rest heb gelegd gaat de temperatuur omlaag

luchtvochtigheid blijft wel flink verschillende van elkaar. Na het langer draai van de temp senosr, lag het verschil in temp aan mijn arm
*/
/*
Wat leer ik hiervan?
  - Dat het aanpassen van script dat ik eerder maakte, dit best wel eenvoudig maakt
  - dat de sensoren niet precies zijn. Ze staan vlak naast elkaar maar geven toch andere waardens op. 
  float h2 = dth2.readHumidity();
  - documentatie opzoeken voor keywords: https://github.com/adafruit/DHT-sensor-library/blob/master/keywords.txt
  - bevenstaande was documentatie voor een andere library. Nu kijken hoe ik die library kan toeveogen.
  - kan library link via arduino IDE vinden
*/
