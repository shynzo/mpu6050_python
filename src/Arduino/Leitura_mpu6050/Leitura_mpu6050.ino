/* 
* Código retirado e adaptado de: https://lastminuteengineers.com/mpu6050-accel-gyro-arduino-tutorial/
* Adaptado por: shynzo
*
*/
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;
int configg = 0;
char command;

void setup(void) {
  Serial.begin(115200);
  // Tentando inicializar
  while (!mpu.begin()) { 
    Serial.println("Falha ao encontrar MPU6050 chip");
    delay(10);
    if (mpu.begin()) {
      break;
    }
  } //Enquanto não conseguir encontrar o chip MPU6050, irá ficar neste loop
  Serial.println("MPU6050 Encontrado!");
  Wire.begin(); //Inicializando leitura
  while (1){ //Neste loop, fica ao aguardo da configuração da escala do acelerômetro
    if (Serial.available()) {
      Serial.println(configg);
      command = Serial.read(); //Lê o comando Serial advindo do Python
      if (command == '0') {
        mpu.setAccelerometerRange(MPU6050_RANGE_2_G); //Setta para +-2g
        break;
      }
      else if (command == '1') {
        mpu.setAccelerometerRange(MPU6050_RANGE_4_G); //Setta para +-4g
        break;
      }
      else if (command == '2') {
        mpu.setAccelerometerRange(MPU6050_RANGE_8_G); //Setta para +-8g
        break;
      }
      else if (command == '3') {
        mpu.setAccelerometerRange(MPU6050_RANGE_16_G); //Setta para +-16g
        break;
      }
      else {
        continue;
      }
    }
  }
  // setta escala de giroscopio para +- 500 deg/s
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  // setta filtro de largura de banda 21hz
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
}

void loop() {
  sensors_event_t a, g, temp; // Lê os eventos do sensor
  mpu.getEvent(&a, &g, &temp); //
  /* Printa os dados em uma linha serial */
  Serial.println((String)a.acceleration.x + ";" + (String)a.acceleration.y + ";" + (String)a.acceleration.z + ";" + (String)temp.temperature + ";" + (String)g.gyro.x + ";" + (String)g.gyro.y + ";" + (String)g.gyro.z);
  /*
    Caso necessite testar, tire este pedaço de código de comentário
    e comente a linha 61.
    Serial.print("Acceleration X: ");
    Serial.print(a.acceleration.x);
    Serial.print(", Y: ");
    Serial.print(a.acceleration.y);
    Serial.print(", Z: ");
    Serial.print(a.acceleration.z);
    Serial.println(" m/s^2");

    Serial.print("Rotation X: ");
    Serial.print(g.gyro.x);
    Serial.print(", Y: ");
    Serial.print(g.gyro.y);
    Serial.print(", Z: ");
    Serial.print(g.gyro.z);
    Serial.println(" rad/s");

    Serial.print("Temperature: ");
    Serial.print(temp.temperature);
    Serial.println(" degC");

    Serial.println("");
  */
  delay(500);
}
