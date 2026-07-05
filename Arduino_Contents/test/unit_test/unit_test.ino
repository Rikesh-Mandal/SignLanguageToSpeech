//sign language to speech

//including required libraries
#include <Wire.h> 
#include <Adafruit_MPU6050.h>

Adafruit_MPU6050 mpu; //creating an instance of the class as mpu

int thumb = A0;
int index = A1;
int middle = A2;
int ring = A3;
int pinky = A4;
int thumbData = 0;
int indexData = 0;
int middleData = 0;
int ringData = 0;
int pinkyData = 0;
float rotX;
float rotY;
float rotZ;
float accX;
float accY;
float accZ;


void setup(){
  Serial.begin(9600); //setting the baud rate
  
  //setting the pinmode
  pinMode(thumb, INPUT);
  pinMode(index, INPUT);
  pinMode(middle, INPUT);
  pinMode(ring, INPUT);
  pinMode(pinky, INPUT);

  //an if condition to check the connection of the gyroscope
  if (!mpu.begin()){
    Serial.println("Failed to find MPU6050 chip");

    // an infinite loop that prevents the program from further execution until the condition is false
    while(1){
      delay(10);
    }
  }

  mpu.setAccelerometerRange('MPU6050_Range_8_G'); //setting the Accelerometer range 2g, 4g, 8g and 16g can be defined
  mpu.setGyroRange('MPU6050_RANGE_500_DEG'); //setting the angular velocity 250, 500, 1000 and 2000 degrees per second can be set
  mpu.setFilterBandwidth('MPU6050_BAND_5_HZ'); //setting the digital low pass filter(DLPF) to 5hz to filter out high frequency noises
}

void loop(){
  //reading the flex sensor data and storing them
  thumbData = analogRead(thumb);
  indexData = analogRead(index);
  middleData = analogRead(middle);
  ringData = analogRead(ring);
  pinkyData = analogRead(pinky);

  sensors_event_t rotation, acc, temp; // a struct to hold sensor event data 
  mpu.getEvent(&rotation, &acc, &temp); 
  rotX = rotation.gyro.x;
  rotY = rotation.gyro.y;
  rotZ = rotation.gyro.z;
  accX = acc.gyro.x;
  accY = acc.gyro.y;
  accZ = acc.gyro.z;

  Serial.print("Thumb Data: ");
  Serial.print(thumbData);
  Serial.print(" ");
  
  delay(1000);
  } 
    
  
