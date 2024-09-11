#include <DHT.h>

#define pinoDHT11 4
#define DHTTYPE DHT11  

DHT sensorDHT11(pinoDHT11, DHTTYPE);

const int led = 8;
const int sensor_pin = A0;
int sensor;
const int threshold = 50;

void setup() {
  pinMode(led, OUTPUT);
  sensorDHT11.begin();
  Serial.begin(9600);
}

void loop() {
  sensor = analogRead(sensor_pin);

  float humidity = sensorDHT11.readHumidity();
  float temperature = sensorDHT11.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" *C");
  
  // Serial.println(sensor);
  if(sensor<threshold){
    digitalWrite(led, HIGH);
  }
  else{
    digitalWrite(led, LOW);
  }
}
