#include <Wire.h>
#include <Adafruit_MPU6050.h>

Adafruit_MPU6050 mpu;

float rotX;
float rotY;
float rotZ;
float accX;
float accY;
float accZ;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  mpu.setAccelerometerRange('MPU6050_Range_8_G'); //setting the Accelerometer range 2g, 4g, 8g and 16g can be defined
  mpu.setGyroRange('MPU6050_RANGE_500_DEG'); //setting the angular velocity 250, 500, 1000 and 2000 degrees per second can be set
  mpu.setFilterBandwidth('MPU6050_BAND_5_HZ');
}

void loop() {
  sensors_event_t rotation, acc, temp; // a struct to hold sensor event data 
  mpu.getEvent(&rotation, &acc, &temp); 
  rotX = rotation.gyro.x;
  rotY = rotation.gyro.y;
  rotZ = rotation.gyro.z;
  accX = acc.gyro.x;
  accY = acc.gyro.y;
  accZ = acc.gyro.z;

  Serial.print("Rotation X: ");
  Serial.print(rotX);
  Serial.print(" ");
  Serial.print("Rotation Y: " );
  Serial.print(rotY);
  Serial.print(" ");
  Serial.print("Rotation Z: ");
  Serial.print(rotZ);
  Serial.print(" ");
  Serial.print("Acceleration X: ");
  Serial.print(accX);
  Serial.print(" ");
  Serial.print("Acceleration Y: ");
  Serial.print(accX);
  Serial.print(" ");
  Serial.print("Acceleration Z: ");
  Serial.print(accZ);
  Serial.println(" ");
  delay(2000);
}
