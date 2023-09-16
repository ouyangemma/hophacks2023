import numpy as np
import pandas as pd

# Number of patients and data points per patient
num_patients = 10
num_data_points = 144
abnormal_pts = 10

#method to generate "realistic" timestamp
def time_stamp(start_time, end_time, interval):

    # Convert start and end times to minutes since midnight
    start_minutes = int(start_time[:2]) * 60 + int(start_time[3:5])
    end_minutes = int(end_time[:2]) * 60 + int(end_time[3:5])

    # Create a NumPy array with timestamps at <interval>-minute intervals
    timestamps = np.arange(start_minutes, end_minutes+1, interval)

    # Convert timestamps back to HH:MM:SS format
    time_strings = [f"{timestamp // 60:02}:{timestamp % 60:02}:00" for timestamp in timestamps]
    repeat_time_strings = np.tile(time_strings, 10)
    print(len(repeat_time_strings))

    # Display the resulting array of time strings
    return repeat_time_strings

# Generate synthetic patient data

unchanging_data = {
    'Patient_ID': np.arange(1, num_patients + 1),
    'Patient_age': np.random.randint(19, 65, num_patients)
}
    
data_normal = {
    'Patient_ID': np.repeat(unchanging_data['Patient_ID'], num_data_points),
    'Patient_age': np.repeat(unchanging_data['Patient_age'], num_data_points),
    'Timestamp': time_stamp("00:00:00", "23:55:00", 10),
    'Heart_Rate': np.random.randint(60, 100, num_patients * num_data_points),
    'Blood_Pressure_Systolic': np.random.randint(100, 140, num_patients * num_data_points),
    'Blood_Pressure_Diastolic': np.random.randint(60, 90, num_patients * num_data_points),
    'Respiratory_Rate': np.random.randint(12, 20, num_patients * num_data_points),
    'Body_Temperature': np.random.uniform(36.0, 37.5, num_patients * num_data_points),
    'Oxygen_Saturation': np.random.randint(95, 100, num_patients * num_data_points),
    }

# np.arange(1, num_patients + 1), num_data_points

data_abnormal = {
    'Patient_ID': unchanging_data['Patient_ID'],
    'Patient_age': unchanging_data['Patient_age'],
    'Timestamp': np.random.choice(time_stamp("00:00:00", "23:55:00", 10), abnormal_pts, replace=False),
    'Heart_Rate': np.random.randint(100, 180, abnormal_pts),
    'Blood_Pressure_Systolic': np.random.randint(100, 180, abnormal_pts),
    'Blood_Pressure_Diastolic': np.random.randint(30, 90, abnormal_pts),
    'Respiratory_Rate': np.random.randint(12, 48, abnormal_pts),
    'Body_Temperature': np.random.uniform(36.0, 40.5, abnormal_pts),
    'Oxygen_Saturation': np.random.randint(88, 100, abnormal_pts),
}

# Create a DataFrame
df1 = pd.DataFrame(data_normal)
df2 = pd.DataFrame(data_abnormal)

# Save to a CSV file
df1.to_csv('patient_data_normal.csv', index=False)
df2.to_csv('patient_data_abnormal.csv', index=False)