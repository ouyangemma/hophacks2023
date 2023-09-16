#Alexis (AJ) Moats
#Hophacks 2023

#Initialize Intake Variables
#Taking in multiple input values from different tests. Analyzing to see if they're in range of device. 
#Each of the values/test is assigned a value. A certain amount of each values assigns it to a condition level. 
#From here, the clinical staff is alerted to the patients whose conditions are most serious.

#Heart rate, blood pressure, respiratory rate, body temperature, oxidation rate, cholesterol level
"""
import tkinter as tk
window = tk.Tk()
window.mainloop()
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()
window accessibility
"""

"""
Baseline Numerical Values for Tests:

Heart Rate: 60-120 bpm-done
Diastolic BP:-done
Systolic Blood Pressure:-done
Respiratory Rate:-done
Body Temperature:
Oxidation Rate:
Cholesterol Level:

"""
#Initialize how important it is to get to the patient
severity_level = 0


#Initialize patient age
patient_age = int(input("Please input the patient's age: "))
    

#Initialize bp values from excel sheet/database (not user input--test)
systolic_bp = int(input("Please input a systolic blood pressure: "))
diastolic_bp = int(input("Please input a diastolic (resting) blood pressure: "))


#Does data fall within normal blood pressure range, if not, how severe is it
#AHA
if 90 < systolic_bp < 120 and 60 < diastolic_bp <80:
    print("Blood pressure is normal.")
elif 120 < systolic_bp and 129 & diastolic_bp < 80:
    print("Blood pressure is elevated.")
    severity_level = 1
elif 130 < systolic_bp < 139 or 80 < diastolic_bp < 89:
    print("Blood pressure is in low-level hypertension.")
    severity_level = 2
elif systolic_bp >= 140 or diastolic_bp > 90:
    print("Blood pressure is in middle-stage hypertension.")
    severity_level = 3
elif systolic_bp > 180 or diastolic_bp > 120:
    print("HIGH SEVERITY HYPERTENSION!!")
    severity_level = 5
elif systolic_bp < 90 and diastolic_bp < 60:
    print("HIGH SEVERITY HYPOTENSION!!")
    severity_level = 5
else:
    print("Directly look at the results.")


#Initialize heart rate values
heart_rate = int(input("Please input a heart rate: "))

if 60 < heart_rate < 100:
    print("Normal heart rate.")
elif 40 < heart_rate < 60:
    print("Potential bradycardia, patient may be sleeping.")
    severity_level+= 1
elif heart_rate < 40:
    print("SEVERELY LOW HEART RATE!!")
    severity_level+=5
elif 100 < heart_rate < 140:
    print("Potential tachycardia.")
    severity_level+= 1
elif heart_rate > 140:
    print("SEVERELY HIGH HEART RATE!!")
    severity_level+= 5

else:
    print("Directly look at the results.")


#Initialize respiratory rate (based on age)
resp_rate = int(input("Please input a respiratory rate: "))

if patient_age == 0 and 30 <= resp_rate <= 60: #newborn/infant resp rates
    print("Normal respiratory rate for newborn")
elif patient_age == 0 and resp_rate < 30:
    print("Newborn has a low respiratory rate")
    severity_level+= 5
elif patient_age == 0 and resp_rate > 60:
    print("Newborn has a high respiratory rate")
    severity_level+= 5
elif 1 < patient_age < 3 and 26 <= resp_rate <= 32: #toddler resp rates
    print("Toddler respiratory rate is normal.")
elif 1 < patient_age < 3 and resp_rate <26:
    print("Toddler respiratory rate is low")
    severity_level+= 5
elif 1 < patient_age < 3 and resp_rate > 32:
    print("Toddler respiratory rate is high")
    severity_level+= 5
elif 3 < patient_age < 13 and 20 < resp_rate < 30: #child resp rate
    print("Child respiratory rate is normal")
elif 3 < patient_age < 13 and resp_rate < 20:
    print("Child respiratory rate is low")
    severity_level+=5
elif 3 < patient_age < 13 and resp_rate > 30:
    print("Child respiratory rate is low")
    severity_level+= 5
elif 13 < patient_age < 18 and 16 < resp_rate < 20:
    print("Adolescent respiratory rate is normal")
elif 13 < patient_age < 18 and resp_rate < 16:
    print("Adolescent respiratory rate is low")
    severity_level+= 5
elif 13 < patient_age < 18 and resp_rate > 20:
    print("Adolescent respiratory rate is high")
    severity_level+= 5
elif patient_age > 18 and 16 < resp_rate < 20: #adult resp rate
    print("Adult respiratory rate is normal")
elif patient_age > 18 and resp_rate < 16:
    print("Adult respiratory rate is low")
    severity_level+=5
elif patient_age > 18 and resp_rate > 20:
    print("Adult respiratory rate is high")
    severity_level+=5
else:
    print("Please manually check respiratory rate")


#Initialize body temperature values
body_temp = int(input("Please input the patient's body temperature: "))

if 97 < body_temp < 99:
    print("Patient body temperature is normal")
elif 95 < body_temp < 97:
    print("Body temperature is low")
    severity_level+= 1
elif body_temp < 95:
   print("PATIENT EXPERIENCING HYPOTHERMIA!!!")
   severity_level+= 5
elif 99< body_temp <= 101:
    print("Body temperature is high")
    severity_level+= 1
elif body_temp > 101:
    print("PATIENT EXPERIENCING HIGH GRADE FEVER")
    severity_level+= 5



