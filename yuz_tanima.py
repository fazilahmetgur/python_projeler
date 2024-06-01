import cv2 
import tkinter as tk
from tkinter import Canvas, filedialog
from PIL import Image, ImageTk

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        img= cv2.imread(file_path)
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray, scaleFactor= 1.30, minNeighbour= 5, minSize=(30,30)) 
        
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.putText(img, 'Bu Bir İnsan', (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        
        canvas.img = img
        canvas.create_image(0, 0, image=img, anchor=tk.NW)
         
         
face_cascade = cv2.CascadeClassifier('face_detector.xml')

#arayüz oluşturma

root = tk.Tk()
root.title("Yüz Tanıma Uygulaması")

canvas= tk.Canvas(root, width=600, height=400) 
canvas.pack()

open_button = tk.Button(root, text=" Dosya Seç", command= open_file)
open_button.pack()


root.mainloop()