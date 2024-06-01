import instaloader
import tkinter as tk
from tkinter import messagebox

def download_post():
    # get user name
    username = username_entry.get()
    
    try:
        #create object
        bot = instaloader.Instaloader()
        
        
        #get user profile
        profile = instaloader.Profile.from_username(bot.context, username)
        
        posts = profile.get_posts()
        
        #download post
        for index, post in enumerate(posts, 1):
            bot.download_post(post, target=f"{profile.username}_{index}")
            
        #show message
        messagebox.showinfo("Success", "Downloaded Successfully")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))
        
        
root = tk.Tk()
root.title("İnstagram Kullanıcı Verilerini İndirme")
root.geometry("300x300")

#input user name
label = tk.Label(root, text= "Kullanıcı Adı: ")
label.pack(pady=15)

#enter user name
username_entry = tk.Entry(root)
username_entry.pack()

#download button
download_button = tk.Button(root, text="İndir", command=download_post)
download_button.pack(pady=15)

root.mainloop()
