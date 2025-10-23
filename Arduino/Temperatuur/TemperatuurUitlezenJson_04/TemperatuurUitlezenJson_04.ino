#include <Arduino.h>
#include "DHT11_Aggregator.h"

#define DHTTYPE DHT11
const uint8_t pins[] = {7, 8, 9};

DHT11_Aggregator sensorGroup(pins, 3, DHTTYPE);

bool handshake = false;

void setup() {
  Serial.begin(9600);
  sensorGroup.begin();
}

void loop() {
  if (Serial.available() > 0) {
    byte incomingByte = Serial.read();

    if (incomingByte == 0b00100100) {
      Serial.println("ACK");
      handshake = true;

    } else if (incomingByte == 0b10100101 && handshake) {
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
