from random import randint
from tkinter import *
from tkinter import simpledialog, messagebox

main = Tk()
main. withdraw()

random_number = randint(0,10)
print(random_number)
x = -1
while x != random_number:
    if x != -1:
       messagebox.showinfo("wrong", "wrong guess")
    x = simpledialog.askstring("guesss","Enter a Numbers")
    x = int(x)

    if x == random_number:
        messagebox.showinfo("Right", "you guessed right")
        exit()
main.mainloop()
   
