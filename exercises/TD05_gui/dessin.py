import tkinter as tk
import random as ra
from tkinter.constants import RAISED
random = 0
random1 = 0
r = 0
v = 0
b = 255
objets = []

def circle() :
    random = ra.randint(10,410)
    random1 = ra.randint(10,410)
    canvas.create_oval((random,random1),(random + 100,random1 + 100), fill=get_color(r, v, b))
    objets.append(random+50)
    objets.append(random1+50)

def square() :
    random = ra.randint(10,410)
    random1 = ra.randint(10,410)
    canvas.create_rectangle((random,random1),(random + 100,random1 + 100), fill=get_color(r, v, b))
    objets.append(random+50)
    objets.append(random1+50)

def cross() :
    random = ra.randint(10,410)
    random1 = ra.randint(10,410)
    canvas.create_line((random,random1), (random + 100, random1 +100), fill=get_color(r, v, b), width=10)
    objets.append(random+50)
    objets.append(random1+50)
    canvas.create_line((random + 100, random1), (random, random1 + 100), fill=get_color(r, v, b), width=10)
    objets.append(random+50)
    objets.append(random1+50)

def afficher_couleur():
    global r
    global v
    global b
    while True:
        r = int(input("Teinte de rouge? "))
        v = int(input("Teinte de vert? "))
        b = int(input("Teinte de bleu? "))
        if 0 <= r <= 255 and 0 <= v <= 255 and 0 <= b <= 255:
            break

def get_color(r=0, g=0, b=0):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def Undo() :
    global objets
    if len(objets) == 0 :
        objets.insert(0, 0)
        objets.insert(0, 0)
    if len(objets) == 2 :
        canvas.delete(canvas.find_closest(objets[-2], objets[-1]))
        del objets[-1]
        del objets[-1]
    elif objets[-1] == objets[-3] and objets[-2] == objets[-4] :
        for i in range(2) :
            canvas.delete(canvas.find_closest(objets[-2], objets[-1]))
            del objets[-1]
            del objets[-1]
    else :
        canvas.delete(canvas.find_closest(objets[-2], objets[-1]))
        del objets[-1]
        del objets[-1]

root = tk.Tk()
root.title("mon dessin")
couleur = tk.Button(root, text="choisir une couleur", font=("helvetica", "26"), command=afficher_couleur)
cercle = tk.Button(root, text="cercle", font=("helvetica", "26"), command=circle)
carre = tk.Button(root, text="carre", font=("helvetica", "26"), command=square)
croix = tk.Button(root, text="croix", font=("helvetica", "26"), command=cross)
canvas = tk.Canvas(root, bg="black", bd=10, cursor="pirate", relief=RAISED, height=500, width=500)
undo = tk.Button(root, text="Undo", font=("helvetica", "26"), command=Undo)

couleur.grid(row=0, column=1)
canvas.grid(rowspan=3, column=1)
cercle.grid(row=1, column=0)
carre.grid(row=2, column=0)
croix.grid(row=3, column=0)
undo.grid(row=0, column=2)

root.mainloop()