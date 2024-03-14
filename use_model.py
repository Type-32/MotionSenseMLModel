import csv
import time
import joblib
import keyboard
import pandas as pd
import serial

# Load the saved model
print("Loading model...")
loaded_model = joblib.load('motionsense_sor_model_1.1k.pkl')
print("Model loaded.")

# Set the serial port and baud rate
print("Loading port...")
ser = serial.Serial('/dev/cu.usbmodem11101', 9600)  # Replace '/dev/cu.usbmodem11101' with the appropriate serial port
print("Port loaded.")

teset = True;

while teset:
    try:
        line = ser.readline().decode('utf-8').rstrip()
        teset = False
    except:
        teset = True

while True:
    pool = []
    print("InSim------------------")
    start_time = time.time()

    print("Recording data for 1 seconds...")

    # Open a CSV file for writing
    with open('mpu_data_prediction.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['mpu_address', 'yaw', 'pitch', 'roll', 'x_accel', 'y_accel', 'z_accel', 'prediction'])

        while time.time() - start_time < 1:  # Record data for 2 seconds
            if ser.in_waiting > 0:
                try:
                    line = ser.readline().decode('utf-8').rstrip()
                except:
                    continue

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

        # Create a DataFrame from the recorded data
        data_df = pd.DataFrame(pool, columns=['mpu_address', 'yaw', 'pitch', 'roll', 'x_accel', 'y_accel', 'z_accel'])

        # Make predictions using the loaded model
        predictions = loaded_model.predict(data_df.drop('mpu_address', axis=1))

        # Write the recorded data and predictions to the CSV file
        for i in range(len(pool)):
            writer.writerow(pool[i] + [predictions[i]])

    print(f"Recorded {len(pool)} lines of data.")

    # Count the occurrences of each prediction
    lift_count = (predictions == 0).sum()
    squat_count = (predictions == 1).sum()

    # Determine the overall prediction based on the majority
    overall_prediction = 'Lift' if lift_count > squat_count else 'Squat'

    print(f"Overall Prediction: {overall_prediction}")
    print(f"Lift Count: {lift_count}")
    print(f"Squat Count: {squat_count}")