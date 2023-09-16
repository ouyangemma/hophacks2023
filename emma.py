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
    newWindow.geometry("500x400")


# "view patient" button
patient_button = ttk.Button(window, text = "View Patient Information", command = openPatientWindow)
patient_button.place(x = 150, y = 250)


window.mainloop()