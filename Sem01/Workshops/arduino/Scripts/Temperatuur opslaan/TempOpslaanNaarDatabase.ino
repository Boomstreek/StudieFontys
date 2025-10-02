#include <dht.h>

#define DHTPIN 7
#define

const int DHT11_1_PIN = 7;
const int DHT11_2_PIN = 8;
const int DHT11_3_PIN = 9;

void setup() {
  Serial.begin(9600);

}

void loop() {
  // Sensor 1 uitlezen
  int DTH11_1 = DHT.read11(DHT11_1_PIN);
  float temp1 = DHT.temperature;
  float hum1  = DHT.humidity;

  // Sensor 2 uitlezen
  int DTH11_2 = DHT.read11(DHT11_2_PIN);
  float temp2 = DHT.temperature;
  float hum2  = DHT.humidity;

    // Sensor 2 uitlezen
  int DTH11_3 = DHT.read11(DHT11_3_PIN);
  float temp3 = DHT.temperature;
  float hum3  = DHT.humidity;

  // Gemiddelde terug geven
  float gem_temp = (temp1 + temp2 + temp3) / 3.0;
  float gem_hum = (hum1 + hum2 + hum3) / 3.0;

  // Gegevens printen naar serial
  Serial.print("Temperature 1= ");
  Serial.print(temp1);
  Serial.println(" Celcius");
  Serial.print("Humidity 1= ");
  Serial.print(hum1);
  Serial.println(" %");

  Serial.print("Temperature 2= ");
  Serial.print(temp2);
  Serial.println(" Celcius");
  Serial.print("Humidity 2= ");
  Serial.print(hum2);
  Serial.println(" %");

  Serial.print("Temperature 3= ");
  Serial.print(temp3);
  Serial.println(" Celcius");
  Serial.print("Humidity 3= ");
  Serial.print(hum3);
  Serial.println(" %");

  Serial.print("Temperature gemiddelde= ");
  Serial.print(gem_temp);
  Serial.println(" Celcius");
  Serial.print("Humidity gemiddelde= ");
  Serial.print(gem_hum);
  Serial.println(" %");

  delay(10000);
}

/*
Wat leer ik hiervan?
  - Dat het aanpassen van script dat ik eerder maakte, dit best wel eenvoudig maakt
  - dat de sensoren niet precies zijn. Ze staan vlak naast elkaar maar geven toch andere waardens op. 
*/
