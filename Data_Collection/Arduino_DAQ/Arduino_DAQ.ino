void setup() {
  Serial.begin(115200); // Set a high baud rate for fast data transfer
}

void loop() {
  unsigned long currentTime = micros(); // Use microseconds for higher resolution timing
  int sensorValue = analogRead(A0); // Read the analog input on pin A0
  float voltage = sensorValue * (5.0 / 1023.0); // Convert the analog reading to voltage
  
  // Print the time and voltage to the Serial Monitor
  Serial.println(voltage);
  
  delay(20); // Wait for 5000 microseconds (5 milliseconds) to achieve 200 samples per second
}