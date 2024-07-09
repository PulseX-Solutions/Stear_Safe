import serial
import time

# Set up the serial connection to the Arduino
ser = serial.Serial('COM6', 115200)  # Replace 'COM6' with the correct port for your Arduino

start_time = time.time()  # Record the start time

# Open the text file in write mode
with open('voltage_data.txt', 'w') as file:
    print("Press 'Ctrl+C' to stop recording.")
    try:
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()  # Read and decode the data from the serial port
                elapsed_time = time.time() - start_time  # Calculate elapsed time

                minutes = int(elapsed_time // 60)
                seconds = int(elapsed_time % 60)
                milliseconds = int((elapsed_time * 1000) % 1000)
                microseconds = int((elapsed_time * 1000000) % 1000)

                formatted_time = f"{minutes}.{seconds:02}.{milliseconds:03}.{microseconds:03}"  # Format the time string
                file.write(f"{formatted_time} {data}\n")  # Write the time and data to the text file
                #print(f"{formatted_time} {data}")  # Print the time and data to the console (optional)
                time.sleep(0.001)  # Wait for 1 millisecond before reading the next line
    except KeyboardInterrupt:
        print("Recording stopped by user.")
    finally:
        ser.close()  # Close the serial connection
