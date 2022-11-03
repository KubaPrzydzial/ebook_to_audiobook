import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pyttsx3


window = tk.Tk()
window.title('ebook to audiobook reader')
window.geometry('200x100')
window.resizable(False, False)
frame = Frame(window)
frame.pack()


reader = pyttsx3.init()
rate = reader.getProperty('rate')  # getting details of speech speed
reader.setProperty('rate', 170)  # speech rate


def open_file():
    file = filedialog.askopenfilename(initialdir='/', title='Open file', filetypes=[("Text Files", "*.txt")])
    fileHandle = open(file, 'r')
    book_read = fileHandle.readlines()
    for i in book_read:
        reader.say(i)
        reader.runAndWait()


canvas = Canvas(window, bg="skyblue3", width=180, height=40)
canvas.create_text(90, 20, anchor='c', text="Ebook reader", font=('', 13))
canvas.pack()
search_button = Button(window, text='Load File and Play', command=open_file).pack(padx=10)


window.mainloop()
