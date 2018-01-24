import tkinter
import FontFile
from tkinter import *

window = Tk()
window.title("Character Creator")
window.geometry("600x600")

window.configure(bg = "gray", )


title = Label(window,bg = "springgreen2",fg = "white", height = 1, width =17, text = "Character Creator")
title.config(font=("Courier", 40))
title.place(x = 25, y = 10)


#Images
guy1 = PhotoImage(file = "character01.png")
guy2 = PhotoImage(file = "character02.png")
guy3 = PhotoImage(file = "character03.png")
guy4 = PhotoImage(file = "character04.png")

gun1 = PhotoImage(file = "weapon01.png")
gun2 = PhotoImage(file = "weapon02.png")
gun3 = PhotoImage(file = "weapon03.png")
gun4 = PhotoImage(file = "weapon04.png")
gun5 = PhotoImage(file = "weapon05.png")

pet = PhotoImage(file = "pet.png")


box = Canvas(window, bg = "white", height = 290, width = 250)

man = box.create_image(300, 300, anchor=SE, image=guy1)

box.place(x = 173, y = 300)

def man1():
    global box
    box.delete("all")
    char = box.create_image(300, 300, anchor=SE, image=guy1)
    box.place(x = 173, y = 300)

def man2():
    global box
    box.delete("all")
    char = box.create_image(300, 300, anchor=SE, image=guy2)
    box.place(x = 173, y = 300)

def man3():
    global box
    box.delete("all")
    char = box.create_image(300, 300, anchor=SE, image=guy3)
    box.place(x = 173, y = 300)

def man4():
    global box
    box.delete("all")
    char = box.create_image(300, 300, anchor=SE, image=guy4)
    box.place(x = 173, y = 300)

one = Button(window, bg = "royalblue", fg = "white", text = "Character One",height = 2, width = 35, command = man1)

one.place(x = 173, y = 250)

two = Button(window, bg = "royalblue", fg = "white", text = "Character Two",height = 2, width = 35, command = man2)

two.place(x = 173, y = 200)

three = Button(window, bg = "royalblue", fg = "white", text = "Character Three",height = 2, width = 35, command = man3)

three.place(x = 173, y = 150)

four = Button(window, bg = "royalblue", fg = "white", text = "Character Four",height = 2, width = 35, command = man4)

four.place(x = 173, y = 100)

we = Label(window, bg = "mediumpurple2", text = "Weapon", width = 20, height = 2,fg = "white")
we.place(x = 10,y=200)

def dragon(event):
    cat = weapon.get()
    if cat ==1:
        guncase.delete("all")
        firstgun = guncase.create_image(100, 100, anchor=SE, image=gun1)
        guncase.place(x = 30, y = 80)
    if cat ==2:
        guncase.delete("all")
        firstgun = guncase.create_image(100, 100, anchor=SE, image=gun2)
        guncase.place(x = 30, y = 80)

    if cat ==3:
        guncase.delete("all")
        firstgun = guncase.create_image(100, 100, anchor=SE, image=gun3)
        guncase.place(x = 30, y = 80)
    if cat ==4:
        guncase.delete("all")
        firstgun = guncase.create_image(100, 100, anchor=SE, image=gun4)
        guncase.place(x = 30, y = 80)
    if cat ==5:
        guncase.delete("all")
        firstgun = guncase.create_image(100, 100, anchor=SE, image=gun5)
        guncase.place(x = 30, y = 80)

weapon = Scale(window, bg = "firebrick2", troughcolor = "firebrick3", orient = VERTICAL, showvalue = 0, width = 30
               ,length = 300, from_ = 1, to = 5, command = dragon)

weapon.place(x = 60, y = 250)

num = weapon.get()

guncase = Canvas(window, height = 100, width = 100)
firstgun = guncase.create_image(100, 100, anchor=SE, image=gun1)
guncase.place(x = 30,y=80)




theflash = Checkbutton(window, bg = "thistle4", text = "Do you want a pet")



theflash.place(x = 450,y = 300)


grene = Checkbutton(window, bg = "thistle4", text = "Are you a warrior?")



grene.place(x = 450,y = 320)

yooo = Checkbutton(window, bg = "thistle4", text = "Do you like this game?")



yooo.place(x = 450,y = 340)

bop = IntVar()

pats = Checkbutton(window, bg = "thistle4", text = "Do you want the\nPatriots to win the \nSuperbowl?", variable = bop)



pats.place(x = 450,y = 380)



window.mainloop()