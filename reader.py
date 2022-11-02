import pyttsx3

book = open(r'file.txt') # name of the file you want to read
book_read = book.readlines()

reader = pyttsx3.init()

rate = reader.getProperty('rate')   # getting details of speech speed
reader.setProperty('rate', 170)     # speech rate

for i in book_read:
    reader.say(i)
    reader.runAndWait()