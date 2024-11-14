from re import I
import tkinter as tk
import random
import tkinter.messagebox as tkm



window = tk.Tk()
window.title("Hangman")

window.configure(bg="black")
window.geometry("400x400")

with open("words_en.txt") as file:
    data = file.read()
words = data.split()
word = random.choice(words)
letters = []



def checkletter():
    letter = entry_letter.get()
    letters.append(letter)
    entry_letter.delete(0,"end")
    show_word = ""
    for character in word:
        if character in letters:
            show_word += character
        else:
            show_word += "*"

    label_word["text"] = show_word
    if show_word == word:
        tkm.showinfo("Victory!","You have guessed the word!")


def new_game():
    global word
    global letters
    letters = []
    word = random.choice(words)
    label_word["text"] = "New Game Started"














label_word = tk.Label(window,text="Here will be the word: ",font = ("Arial",13),fg="white",bg="black")
label_word.place(x=30,y=20)

entry_letter = tk.Entry(window,width=8,font = ("Arial",13))
entry_letter.place(x=30,y=60)

button_check = tk.Button(window,text="Check the letter",font = ("Arial",13),command=checkletter)
button_check.place(x=30,y=100)

button_new = tk.Button(window,text="Restart",font = ("Arial",13),command=new_game)
button_new.place(x=300,y=350)




window.mainloop()