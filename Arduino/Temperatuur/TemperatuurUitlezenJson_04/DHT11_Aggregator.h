#ifndef DHT11_AGGREGATOR_H
#define DHT11_AGGREGATOR_H

#include <Arduino.h>
#include <DHT.h>

class DHT11_Aggregator {
  public:
    DHT11_Aggregator(const uint8_t pins[], uint8_t count, uint8_t type);
    ~DHT11_Aggregator();

    void begin();
    void update();
    float getTemperature() const { return avgTemperature; }
    float getHumidity() const { return avgHumidity; }

  private:
    DHT** sensors;      // array van pointers
    uint8_t sensorCount;
    float avgTemperature;
    float avgHumidity;
    uint8_t sensorType;
};

#endif