import numpy as np
import pandas as pd

# Number of patients and data points per patient
num_patients = 10
num_data_points = 144
abnormal_pts = 20
test_pts = 20

#method to generate "realistic" timestamp
def time_stamp(start_time, end_time, interval):

    # Convert start and end times to minutes since midnight
    start_minutes = int(start_time[:2]) * 60 + int(start_time[3:5])
    end_minutes = int(end_time[:2]) * 60 + int(end_time[3:5])

    # Create a NumPy array with timestamps at <interval>-minute intervals
    timestamps = np.arange(start_minutes, end_minutes+1, interval)

    # Convert timestamps back to HH:MM:SS format
    time_strings = [f"{timestamp // 60:02}:{timestamp % 60:02}:00" for timestamp in timestamps]
    # repeat_time_strings = np.tile(time_strings, 10)
    print(len(time_strings))

    # Display the resulting array of time strings
    return time_strings

# Generate synthetic patient data

unchanging_data = {
    'Patient_ID': np.arange(1, num_patients + 1),
    'Patient_Name': np.array(['Tamara Miranda' 'Jason Simmons' 'George Knight' 'Timothy Sloan' 'Christina Shaw' 'James Henderson' 'Amanda Simpson' 'Jeffrey Benjamin' 'Jennifer Escobar' 'Philip Weaver']),
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

data_abnormal_low_heart = {
    'Patient_ID': np.repeat(unchanging_data['Patient_ID'], abnormal_pts),
    'Patient_age': np.repeat(unchanging_data['Patient_age'], abnormal_pts),
    'Timestamp': np.random.choice(time_stamp("00:00:00", "23:55:00", 10), num_patients * abnormal_pts, replace=True),
    'Heart_Rate': np.random.randint(40, 70, num_patients * abnormal_pts),
    'Blood_Pressure_Systolic': np.random.randint(70, 120, num_patients * abnormal_pts),
    'Blood_Pressure_Diastolic': np.random.randint(30, 50, num_patients * abnormal_pts),
    'Respiratory_Rate': np.random.randint(30, 48, num_patients * abnormal_pts),
    'Body_Temperature': np.random.uniform(36.0, 40.5, num_patients * abnormal_pts),
    'Oxygen_Saturation': np.random.randint(60, 88, num_patients * abnormal_pts),
}
data_abnormal_high_heart = {
    'Patient_ID': np.repeat(unchanging_data['Patient_ID'], abnormal_pts),
    'Patient_age': np.repeat(unchanging_data['Patient_age'], abnormal_pts),
    'Timestamp': np.random.choice(time_stamp("00:00:00", "23:55:00", 10), num_patients * abnormal_pts, replace=True),
    'Heart_Rate': np.random.randint(110, 140, num_patients * abnormal_pts),
    'Blood_Pressure_Systolic': np.random.randint(130, 180, num_patients * abnormal_pts),
    'Blood_Pressure_Diastolic': np.random.randint(90, 130, num_patients * abnormal_pts),
    'Respiratory_Rate': np.random.randint(30, 48, num_patients * abnormal_pts),
    'Body_Temperature': np.random.uniform(36.0, 40.5, num_patients * abnormal_pts),
    'Oxygen_Saturation': np.random.randint(60, 88, num_patients * abnormal_pts),
}

data_testing = {
    'Patient_ID': np.repeat(1, num_patients * test_pts),
    'Patient_age': np.repeat(36, num_patients * test_pts),
    'Timestamp': np.random.choice(time_stamp("00:00:00", "23:55:00", 10), num_patients * test_pts, replace=True),
    'Heart_Rate': np.random.randint(60, 110, num_patients * test_pts),
    'Blood_Pressure_Systolic': np.random.randint(90, 140, num_patients * test_pts),
    'Blood_Pressure_Diastolic': np.random.randint(60, 90, num_patients * test_pts),
    'Respiratory_Rate': np.random.randint(12, 20, num_patients * test_pts),
    'Body_Temperature': np.random.uniform(36.0, 37.5, num_patients * test_pts),
    'Oxygen_Saturation': np.random.randint(75, 100, num_patients * test_pts)
}

# Create a DataFrame
# df1 = pd.DataFrame(data_normal)
# df2 = pd.DataFrame(data_abnormal_low_heart)
# df3 = pd.DataFrame(data_abnormal_high_heart)
df4 = pd.DataFrame(data_testing)

# Save to a CSV file
# df1.to_csv('patient_data_normal.csv', index=False)
# df2.to_csv('patient_data_abnormal_low.csv', index=False)
# df3.to_csv('patient_data_abnormal_high.csv', index=False)
df4.to_csv('testing_data.csv', index=False)