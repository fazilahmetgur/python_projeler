import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

# Create the GUI window
root = tk.Tk()
root.title("Face Detection")

# Create a canvas to display the image
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Define the open_file function
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.30, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, 'Bu Bir İnsan', (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        canvas.img = img
        canvas.create_image(0, 0, image=img, anchor=tk.NW)

face_cascade = cv2.CascadeClassifier('face_detector.xml')
# Create a button to open the file dialog
open_button = tk.Button(root, text="Open Image", command=open_file)
open_button.pack()

# Start the GUI event loop
root.mainloop()