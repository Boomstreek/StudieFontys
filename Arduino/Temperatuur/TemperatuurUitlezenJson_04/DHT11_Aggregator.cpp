#include "DHT11_Aggregator.h"

DHT11_Aggregator::DHT11_Aggregator(const uint8_t pins[], uint8_t count, uint8_t type)
  : sensorCount(count), avgTemperature(0), avgHumidity(0), sensorType(type) {
    sensors = new DHT*[sensorCount];  // array van pointers
    for (uint8_t i = 0; i < sensorCount; i++) {
      sensors[i] = new DHT(pins[i], sensorType);  // maak elk object individueel aan
    }
}

DHT11_Aggregator::~DHT11_Aggregator() {
    for (uint8_t i = 0; i < sensorCount; i++) {
        delete sensors[i];
    }
    delete[] sensors;
}

void DHT11_Aggregator::begin() {
  for (uint8_t i = 0; i < sensorCount; i++) {
    sensors[i]->begin();
  }
}

void DHT11_Aggregator::update() {
  float tempSum = 0;
  float humSum = 0;

  for (uint8_t i = 0; i < sensorCount; i++) {
    tempSum += sensors[i]->readTemperature();
    humSum += sensors[i]->readHumidity();
  }

  avgTemperature = tempSum / sensorCount;
  avgHumidity = humSum / sensorCount;
}