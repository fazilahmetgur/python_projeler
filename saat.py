from tkinter import Label, Tk
import time

app_window= Tk()
app_window.title("Dijital Saat")
app_window.geometry("500x500")
app_window.resizable(1,1)
app_window.configure(bg="black")

text_font=("Bolder", 36, "bold")
background="black"
foreground="white"
border_width= 20

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1, padx=10, pady=10)

date_label= Label(app_window, font=text_font, bg=background, fg=foreground , bd=border_width)
label.grid(row=0, column=1, padx=10, pady=10)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)
    date_info= time.strftime("%d %M %Y")
    date_label.config(text=date_info) 
    label.after(200, digital_clock)
    
digital_clock()

app_window.mainloop()