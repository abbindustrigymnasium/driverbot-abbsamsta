#include <Servo.h>
#define motorPinDir 0   //D2
#define motorPinSpeed 5 //D1
#include "EspMQTTClient.h"
#include "PubSubClient.h"

// ---- Defines variables---
Servo servo;
String Sub = "samuel.staflin@abbindustrigymnasium.se/motor";
int speedValue = 0;
int dirValue = 0;
int rotateValue = 0;

// ------ MQTT Connect --------
void onConnectionEstablished();

EspMQTTClient client(
    "Hollywood",                              // Wifi ssid
    "05070507",                               // Wifi password
    "maqiatto.com",                           // MQTT broker ip
    1883,                                     // MQTT broker port
    "samuel.staflin@abbindustrigymnasium.se", // MQTT username
    "Samuel0303",                             // MQTT password
    "enheteeeen",                             // Client name
    onConnectionEstablished,                  // Connection established callback
    true,                                     // Enable web updater
    true                                      // Enable debug messages
);

// ------ When client connected -------
void onConnectionEstablished()
{
  client.subscribe(Sub, [](const String &payload) {
    dirValue = payload.substring(0, 1).toInt();    // Parse forward / backwards
    speedValue = payload.substring(1, 5).toInt();  // Parse speed value
    rotateValue = payload.substring(5, 8).toInt(); // Parse front wheel direction
  });
}

// ----- Update values to RC -------
void DriveDirSpeed(int Dirpin, int Speedpin, int Direction, int Speed)
{
  if (Direction == 1)
    Serial.println("Framåt");
  else
    Serial.println("Bakåt");

  Serial.println("Hastighet: " + String(Speed));

  digitalWrite(Dirpin, Direction); // Update direction
  analogWrite(Speedpin, Speed);    // Update speed
}

void setup()
{
  pinMode(motorPinDir, OUTPUT);
  pinMode(motorPinSpeed, OUTPUT);
  servo.attach(2); //D4
  servo.write(0);
  Serial.begin(115200);
}

void loop()
{
  client.loop();                                                   // Connect to client
  onConnectionEstablished();                                       // Get values from controller
  servo.write(rotateValue);                                        // Rotate steering wheel
  DriveDirSpeed(motorPinDir, motorPinSpeed, dirValue, speedValue); // Update driving values
}
