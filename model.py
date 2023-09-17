# decision tree
import numpy as np
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import classification_report
import pickle
from severity_score import calculate_severity

# creating training data

# Get the current directory of the script
relative_path = os.path.dirname(__file__)

# Read the CSV file using the relative path
X_train = pd.read_csv(os.path.join(relative_path, 'patient_data_mixed.csv'))
# print(X_train.head())

X_train = X_train.iloc[:, X_train.columns != 'Timestamp']
X_train = X_train.iloc[:, X_train.columns != 'Patient_ID']
print(X_train.tail())

Y_train_np = np.zeros((X_train.shape[0], 1))

# calculate_severity(Patient_age,Heart_Rate,Blood_Pressure_Systolic,Blood_Pressure_Diastolic,Respiratory_Rate,Body_Temperature,Oxygen_Saturation):
for i in range(0, X_train.shape[0]-1):
    Y_train_np[i, 0] = calculate_severity(X_train.iloc[i,0], X_train.iloc[i,1], X_train.iloc[i,2], X_train.iloc[i,3], X_train.iloc[i,4], X_train.iloc[i,5], X_train.iloc[i,6])

Y_train = pd.DataFrame(Y_train_np)
# Y_train.to_csv('y_data1.csv', index=False)

print(X_train.shape)

print(Y_train.shape)
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

filename = 'decision_tree_model.sav'
pickle.dump(model, open(filename, 'wb'))


# X_test = pd.read_csv('/Users/hyewon/Desktop/Hophacks/hophacks2023/testing_data.csv')
# X_test = X_test.iloc[:, X_test.columns != 'Timestamp']
# X_test = X_test.iloc[:, X_test.columns != 'Patient_ID']
# prediction = model.predict(X_test)
# print(prediction)

# Y_test_np = np.zeros((X_test.shape[0], 1))
# for i in range(0, X_test.shape[0]-1):
#     Y_test_np[i, 0] = calculate_severity(X_test.iloc[i,0], X_test.iloc[i,1], X_test.iloc[i,2], X_test.iloc[i,3], X_test.iloc[i,4], X_test.iloc[i,5], X_test.iloc[i,6])

# Y_test = pd.DataFrame(Y_test_np)
# Y_test.to_csv('y_data2.csv', index=False)
# print(classification_report(Y_test, prediction))
