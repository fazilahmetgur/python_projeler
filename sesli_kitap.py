import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog

def pdf_metni_cikart(pdf_way):
    pdf_metin= ""
    pdf_okuyucu= PyPDF2.PdfReader(open(pdf_way, "rb"))
    for sayfa_num in range(len(pdf_okuyucu.pages)):
        pdf_metin += pdf_okuyucu.pages[sayfa_num].extract_text()
    
    return pdf_metin

def metni_sese_cevir(pdf_metin, sesli_kitap):
    pdf_metin= pdf_metni_cikart(pdf_way) # type: ignore
    ses= gTTS(text=pdf_metin, lang="tr")
    ses.save("sesli_kitap.mp3")
    os.system("start sesli_kitap.mp3")
    
def dosya_sec():
    dosya_yolu= filedialog.askopenfilename(filetypes=(("PDF Dosyaları", "*.pdf"),))
    if dosya_yolu:
        pdf_metin= pdf_metni_cikart(pdf_way) # type: ignore
        metni_sese_cevir(pdf_metin, "kaydet.mp3")
        os.system("start kaydet.mp3")
        
#tkinter arayüzü
app=tk.Tk()
app.title("Sesli Kitap Uygulaması")
app.geometry("250x150")

secim_butonu= tk.Button(app, text="PDF Seç", command=dosya_sec)
secim_butonu.pack(padx=20, pady=20)



app.mainloop()
        