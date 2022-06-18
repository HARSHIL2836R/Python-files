from tkinter import *
from PyDictionary import PyDictionary

root = Tk()
root.geometry('1200x600')


def find_meaning():
    word = entry.get()
    dictionary = PyDictionary(word)
    meaning = dictionary.printMeanings()
    output = Label(root, meaning)
    output.pack()


entry = Entry(root, font=("consolas", 20, "bold"))
entry.grid(row=2, column=1, pady=100, padx=100)
btn = Button(root, text="find meaning", command=find_meaning)
btn.grid(row=4, column=1)

root.mainloop()
