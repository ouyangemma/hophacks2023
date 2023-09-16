import numpy as np
import pandas as pd

# Number of patients and data points per patient
num_patients = 20
num_data_points = 20

# Generate synthetic patient data
data = {
    'Patient_ID': np.repeat(np.arange(1, num_patients + 1), num_data_points),
    'Timestamp': np.tile(np.arange(1, num_data_points + 1) * 5, num_patients),
    'Heart_Rate': np.random.randint(60, 100, num_patients * num_data_points),
    'Blood_Pressure_Systolic': np.random.randint(100, 140, num_patients * num_data_points),
    'Blood_Pressure_Diastolic': np.random.randint(60, 90, num_patients * num_data_points),
    'Respiratory_Rate': np.random.randint(12, 20, num_patients * num_data_points),
    'Body_Temperature': np.random.uniform(36.0, 37.5, num_patients * num_data_points),
    'Oxygen_Saturation': np.random.randint(95, 100, num_patients * num_data_points),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('patient_data.csv', index=False)