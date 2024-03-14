import csv

import keyboard
import serial

# Set the serial port and baud rate
ser = serial.Serial('/dev/cu.usbmodem11101', 9600)  # Replace 'COM3' with the appropriate serial port

pool = []
exitRecord: bool = False


import csv

print("Recording Data. Press any key to exit.")
def on_key_press(event):
    exitRecord = True
    print(f"Exited.")

keyboard.on_press(on_key_press)

# Open a CSV file for writing
with open('mpu_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['mpu_address', 'yaw', 'pitch', 'roll', 'x_accel', 'y_accel', 'z_accel'])
    while not exitRecord:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            data = line.split('-')
            if len(data) == 7:
                mpu_address = int(data[0])
                yaw = float(data[1])
                pitch = float(data[2])
                roll = float(data[3])
                acc_x = float(data[4])
                acc_y = float(data[5])
                acc_z = float(data[6])
                temp = [mpu_address, yaw, pitch, roll, acc_x, acc_y, acc_z]
                pool.append(temp)
                writer.writerow(temp)


print(f"A total amount of {len(pool)} lines of records were recorded")