from tkinter import *
from tkinter import ttk

# creating the main application window
window = Tk()
window.title("PATIENT ALERT")
window.geometry("500x400")

# creating a frame for the main label
# Create a canvas widget to draw the rectangle
canvas = Canvas(window, width=300, height=200)
canvas.pack()

# Create a red rectangle on the canvas
rectangle = canvas.create_rectangle(50, 100, 250, 200, fill= '#e74c3c')

# Add text on top of the rectangle
text = canvas.create_text(150, 150, text="Abnormal Value Detected!", fill="white", font=("Helvetica", 16))

# creating label widgets (substituting this with text on a rectangle)
# outlier_label = ttk.Label(window, text = "Out of Bounds Value Detected")
# outlier_label.place(x = 40, y = 60)

# function to display more information
def openPatientWindow():
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
        
        rectangles.append(rectangle)



# "view patient" button
patient_button = ttk.Button(window, text = "View Patient Information", command = openPatientWindow)
patient_button.place(x = 150, y = 250)


window.mainloop()