#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

int led = 5;
int led2 = 23;
int sw = 34;
#define Float_Sensor 21

const char* ssid = "realme XT";
const char* password = "sira12345";
const char* url_put = "https://beatsets.info/api/car/4";

static TaskHandle_t Task1 = NULL;
static TaskHandle_t Task2 = NULL;

char str[50];
String names;
const int _size = 2*JSON_OBJECT_SIZE(4);

StaticJsonDocument<_size> JSONPut;


void WiFi_Connect(){
  WiFi.disconnect();
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("Connecting....");
  }
   Serial.println("Connected");
}


void _putc(bool has) {
  if(WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(url_put);
    http.addHeader("Content-Type", "application/json");

    JSONPut["has_accident"] = has;
    JSONPut["has_drowned"] = false;
    serializeJson(JSONPut, str);
    int httpCode = http.PUT(str);

    if(httpCode == HTTP_CODE_OK) {
      String payload = http.getString();
      Serial.println(httpCode);
      Serial.println(payload);
      }else {
          Serial.println(httpCode);
          Serial.println("ERROR on HTTP Request");
      }
    }else {
            WiFi_Connect();
          }
    delay(100);
  }


void _putf(bool has) {
  if(WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(url_put);
    http.addHeader("Content-Type", "application/json");

    JSONPut["has_accident"] = false;
    JSONPut["has_drowned"] = has;
    serializeJson(JSONPut, str);
    int httpCode = http.PUT(str);

    if(httpCode == HTTP_CODE_OK) {
      String payload = http.getString();
      Serial.println(httpCode);
      Serial.println(payload);
      }else {
          Serial.println(httpCode);
          Serial.println("ERROR on HTTP Request");
      }
    }else {
            WiFi_Connect();
          }
    delay(100);
  }

void Crash(void *parameter){
  while (1){
      if (digitalRead(sw) == 1){
        digitalWrite(led, LOW);
      }else{
        digitalWrite(led, HIGH);
      }
      vTaskDelay(100/ portTICK_PERIOD_MS);
    }
}

void Float(void *parameter){
  while (1){
    if (digitalRead(Float_Sensor) == HIGH){
      digitalWrite(led2, HIGH);
    }else{
      digitalWrite(led2, LOW);
    }
   vTaskDelay(100/ portTICK_PERIOD_MS);
  }
}


void setup() {
  Serial.begin(115200);
  WiFi_Connect();
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(sw, INPUT);
  pinMode(Float_Sensor, INPUT);
  digitalWrite(led, HIGH);
  digitalWrite(led2, LOW);
  
  xTaskCreatePinnedToCore(Crash, "Task_1", 1024, NULL, 1, &Task1, 1);
  xTaskCreatePinnedToCore(Float, "Task_2", 1024, NULL, 1, &Task2, 1);
} 

void loop() {
  if (digitalRead(sw) == 1){
    _putc(true);
    }
  if (digitalRead(Float_Sensor) == HIGH){
    _putf(true);
  }
  delay(100);
}
