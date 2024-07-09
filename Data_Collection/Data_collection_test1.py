import serial
import time

# Set up the serial connection to the Arduino
ser = serial.Serial('COM3', 115200)  # Replace 'COM3' with the correct port for your Arduino

# Open the text file in write mode
with open('voltage_data.txt', 'w') as file:
    print("Press 'Ctrl+C' to stop recording.")
    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()  # Read and decode the data from the serial port
                file.write(data + '\n')  # Write the data to the text file
                print(data)  # Print the data to the console (optional)
                time.sleep(0.005)  # Wait for 5 milliseconds before reading the next line
    except KeyboardInterrupt:
        print("Recording stopped by user.")
    finally:
        ser.close()  # Close the serial connection
