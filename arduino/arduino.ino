#include <Servo.h>
#define motorPinDir  0//D2
#define motorPinSpeed 5//D1
#include "EspMQTTClient.h"
#include "PubSubClient.h"

Servo servo;
String Sub = "samuel.staflin@abbindustrigymnasium.se/motor";
int speedValue = 0;
int dirValue = 0;
int rotateValue = 0;

void onConnectionEstablished();

// Deepspace
// HeSaFe720304!1

// Hollywood
// 05080508

EspMQTTClient client(
  "Hollywood",                       // Wifi ssid
  "05070507",                            // Wifi password
  "maqiatto.com",                           // MQTT broker ip
  1883,                                     // MQTT broker port
  "samuel.staflin@abbindustrigymnasium.se",       // MQTT username
  "Samuel0303",                             // MQTT password
  "enheteeeen",   // Client name
  onConnectionEstablished,                  // Connection established callback
  true,                                     // Enable web updater
  true                                      // Enable debug messages
);

void onConnectionEstablished() {
  client.subscribe(Sub, [] (const String & payload) {
    dirValue = payload.substring(0, 1).toInt() ;
    speedValue = payload.substring(1, 5).toInt();
    rotateValue = payload.substring(5, 8).toInt();
  });
}

void DriveDirSpeed(int Dirpin, int Speedpin, int Direction, int Speed) {
  if (Direction == 1)
    Serial.println("Framåt");
  else
    Serial.println("Bakåt");

  Serial.println("Hastighet: " + String(Speed));

  digitalWrite(Dirpin, Direction);
  analogWrite(Speedpin, Speed);
}

void setup() {
  pinMode(motorPinDir, OUTPUT);
  pinMode(motorPinSpeed, OUTPUT);
  servo.attach(2); //D4
  servo.write(0);
  Serial.begin(115200);
}

void loop() {
  client.loop();
  onConnectionEstablished();
  servo.write(rotateValue);
  DriveDirSpeed(motorPinDir, motorPinSpeed, dirValue, speedValue);
}
