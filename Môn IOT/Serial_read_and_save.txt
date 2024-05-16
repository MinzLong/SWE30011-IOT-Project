import serial
import sqlite3
import RPi.GPIO as GPIO

# Set up GPIO pin for the buzzer on Raspberry Pi
BUZZER_PIN = 11  # Change the GPIO pin number depending on the actual connection
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Connect to the serial port, replace "/dev/ttyUSB0" with the actual serial port of the Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)

# Connect to the SQLite database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS distance (
                    id INTEGER PRIMARY KEY, 
                    distance INTEGER, 
                    motor_status TEXT, 
                    fire_detect TEXT
                )''')

try:
    while True:
        # Read data from the serial port
        data = ser.readline().decode().strip()

        # Parse the data
        if data.startswith("Distance:"):
            distance = int(data.split(":")[1].strip().split(" ")[0])
            motor_status = "on" if distance <= 10 else "off"  # Condition for motor on/off

            # Read fire sensor status from serial port
            fire_detect = ser.readline().decode().strip()
            
            # Save data to the database
            cursor.execute('''INSERT INTO distance (distance, motor_status, fire_detect) VALUES (?, ?, ?)''', (distance, motor_status, fire_detect))
            conn.commit()

            # Print data to terminal
            print(f"Distance: {distance} cm")
            print(f"Motor: {motor_status}")
            print(f"Fire Detect: {fire_detect}")

            # Activate buzzer if distance is less than 10
            if distance < 10:
                GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Activate buzzer
            else:
                GPIO.output(BUZZER_PIN, GPIO.LOW)   # Turn off buzzer

finally:
    # Close connections
    ser.close()
    conn.close()
    GPIO.cleanup()  # Clean up GPIO resources on program exit
