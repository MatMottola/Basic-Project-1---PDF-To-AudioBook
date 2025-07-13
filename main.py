import pyttsx3  
from PyPDF2 import PdfReader
from tkinter.filedialog import *
import tkinter as tk
import threading
import keyboard
import time
import os

stop_reading  = False
player = pyttsx3.init()

def listen_for_escape():
    global stop_reading
    keyboard.wait('esc')
    stop_reading = True
    player.stop()
    print("Reading stopped by user.")

def speak_text(text):
    global stop_reading
    if not stop_reading:
        player.say(text)
        player.runAndWait()
    

root = tk.Tk()
root.withdraw()  

book_path = askopenfilename(filetypes=[("PDF files", "*.pdf")])
if not book_path:
    print("No file selected.")
    exit()

threading.Thread(target=listen_for_escape, daemon=True).start()

with open(book_path,"rb") as book_file:
    pdfreader = PdfReader(book_file)
    pages = len(pdfreader.pages)
    if pages == 0:
        print("The PDF file is empty.")
        exit()


    for num in range (0,pages):
     if stop_reading:
        break

     page = pdfreader.pages[num]
     text = page.extract_text()

     if text and text.strip():
        tts_thread = threading.Thread(target=speak_text, args=(text,))
        tts_thread.start()


        while tts_thread.is_alive():
            if stop_reading:
             player.stop()
             break
            time.sleep(0.1)


print("Reading completed.")
player.stop()
os._exit(0)  