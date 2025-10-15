#include <DHT.h>
JsonDocument doc;

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
  // Controleer of er seriële data is
  if (Serial.available() > 0) {
    byte incomingByte = Serial.read();

    if (incomingByte == 0b10100101) {
      Serial.println("ACK");

      // Meten
      float t1 = dht1.readTemperature();
      float t2 = dht2.readTemperature();
      float t3 = dht3.readTemperature();

      float h1 = dht1.readHumidity();
      float h2 = dht2.readHumidity();
      float h3 = dht3.readHumidity();

      float gem_tem = (t1 + t2 + t3) / 3.0;
      float gem_hum = (h1 + h2 + h3) / 3.0;

      String data = "{\"temperatuur\":" + String(gem_tem) + ",\"luchtvochtigheid\":" + String(gem_hum) + "}";
      Serial.println(data);
    } 
    else {
      Serial.println("NACK"); // verkeerde byte ontvangen
    }
  }

  // Kleine pauze om buffer niet te overbelasten
  delay(10);
}
