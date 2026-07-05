#include <Wire.h>
#include <Adafruit_MPU6050.h>

Adafruit_MPU6050 mpu;

int pinky = A0;
int pinkyData = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pinky, INPUT);
}

void loop() {
  pinkyData = analogRead(pinky);
  Serial.print("Pinky Data: ");
  Serial.print(pinkyData);
  Serial.println("");
  delay(3000);
}
