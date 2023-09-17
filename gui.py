from tkinter import *
from tkinter import ttk
import pandas as pd
import pickle
import os
import sklearn
import time
import string
import csv
import numpy as np

def createCanvas():
    # creating a frame for the main label
    # Create a canvas widget to draw the rectangle
    canvas = Canvas(window, width=300, height=200)
    canvas.pack()

    # Create a red rectangle on the canvas
    rectangle = canvas.create_rectangle(50, 100, 250, 200, fill= '#e74c3c')

    # Add text on top of the rectangle
    text = canvas.create_text(150, 150, text="Abnormal Value Detected!", fill="white", font=("Helvetica", 16))


# function to display more information
def openPatientWindow(information_array):
    # Toplevel object will be treated as a new window
    newWindow = Toplevel(window)
    newWindow.title("Patient Profile")
    newWindow.geometry("600x300")

    # Create labels and entry widgets for patient data
    labels = ["Patient ID", "Age", "Timestamp", "Heart Rate", "Systolic BP", "Diastolic BP", "Resp. Rate", "Body Temp", "Oxygen Saturation"]
    rectangles = []

    for label_text in labels:
        label = ttk.Label(newWindow, text=label_text)
        label.grid(row=len(rectangles), column=0, padx=10, pady=5, sticky="w")
        
        # Create a white rectangle (Canvas)
        rectangle = Canvas(newWindow, bg="white", width=150, height=20, highlightthickness=0)
        rectangle.grid(row=len(rectangles), column=1, padx=10, pady=5)
        text = rectangle.create_text(row=len(rectangles), text=information_array[i], fill="white", font=("Helvetica", 16))
        
        rectangles.append(rectangle)

def useModel():
    # Get the current directory of the script
    relative_path = os.path.dirname(__file__)

    # Read the CSV file using the relative path
    dataframe = pd.read_csv(os.path.join(relative_path, 'testing_data.csv'))
    model = pickle.load(open(os.path.join(relative_path, 'decision_tree_model.sav'), 'rb'))

    dataframe = dataframe.iloc[:, dataframe.columns != 'Timestamp']
    dataframe = dataframe.iloc[:, dataframe.columns != 'Patient_ID']
    prediction = model.predict(dataframe)
    print(prediction)

    return prediction

    # make model predict severity score

if __name__ == "__main__":

    data_array = useModel()
    for i in range(data_array):
        if data_array(i) > 8:

            # Get the current directory of the script
            relative_path = os.path.dirname(__file__)

            # read csv file
            X_train = pd.read_csv(os.path.join(relative_path, 'testing_data.csv'))

            # take data from ith row and input into openPatientWindow(needs inputs)
            Y_train_np = np.zeros((X_train.shape[0], 1))
            Y_train_np[i, 0] = string(X_train.iloc[i,0]), string(X_train.iloc[i,1]), string(X_train.iloc[i,2]), string(X_train.iloc[i,3]), string(X_train.iloc[i,4]), string(X_train.iloc[i,5]), string(X_train.iloc[i,6]), string(X_train.iloc[i,7]), string(X_train.iloc[i,8]) 

            # creating the main application window
            window = Tk()
            window.title("PATIENT ALERT")
            window.geometry("500x400")

            createCanvas()

            # "view patient" button
            patient_button = ttk.Button(window, text = "View Patient Information", command = openPatientWindow(Y_train_np[i,0]))
            patient_button.place(x = 150, y = 250)

            window.mainloop()


        time.sleep(1)
        


