#include <Arduino.h>
#include "DHT11_Aggregator.h"

#define DHTTYPE DHT11
const uint8_t pins[] = {7, 8, 9}; //uint8_t staat voor unsigned interger 8 bits type, maar klopt de _t? Gedlt ook voor de classe DHT11_Aggregator

DHT11_Aggregator sensorGroup(pins, 3, DHTTYPE); // Hier maken we het object aan dat de 3 sensoren regelt

void setup() {
  Serial.begin(9600);
  sensorGroup.begin();
}

void loop() {
  if (Serial.available() > 0) {
    byte incomingByte = Serial.read();

    if (incomingByte == 0b10100101) {
      Serial.println("ACK");

      sensorGroup.update();

      String data = "{\"temperatuur\":";
      data += String(sensorGroup.getTemperature(), 2);
      data += ",\"luchtvochtigheid\":";
      data += String(sensorGroup.getHumidity(), 2);
      data += "}";
      Serial.println(data);
    } else {
      Serial.println("NACK");
    }
  }

  delay(10);
}