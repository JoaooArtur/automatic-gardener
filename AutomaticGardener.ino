#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <ESP8266HTTPClient.h>
#include <DHT.h>

#define pinoDHT11 D4
#define DHTTYPE DHT11  

const char* ssid = "Eduardo";
const char* password = "12345678";

const char* apiUrl = "https://6fwmz9m4gf.execute-api.us-east-1.amazonaws.com/default/automatic-gardener-api";

DHT sensorDHT11(pinoDHT11, DHTTYPE);

const int sensor_pin = A0;
int sensor;
const int threshold = 50;

void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, password);
  Serial.print("Conectando-se ao Wi-Fi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }

  Serial.println("\nConectado ao Wi-Fi!");
  sensorDHT11.begin();
}

void loop() {
  int sunlight = analogRead(sensor_pin);

  float humidity = sensorDHT11.readHumidity();
  float temperature = sensorDHT11.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  int humidityInt = (int)humidity;
  int temperatureInt = (int)temperature;

  Serial.print("Humidity: ");
  Serial.print(humidityInt);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(temperatureInt);
  Serial.println(" *C");

  if (WiFi.status() == WL_CONNECTED) {
    WiFiClientSecure client;
    client.setInsecure();

    HTTPClient http;

    http.begin(client, apiUrl);
    http.addHeader("Content-Type", "application/json");

    String jsonBody = String("{\"key1\": ") + humidityInt +
                      String(", \"key2\": ") + temperatureInt +
                      String(", \"key3\": ") + sunlight + String("}");

    int httpResponseCode = http.POST(jsonBody);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Resposta da API: " + response);
    } else {
      Serial.println("Erro na requisição: " + String(httpResponseCode));
    }

    http.end();
  } else {
    Serial.println("Erro ao conectar ao Wi-Fi.");
  }
  
  delay(300000);
}
