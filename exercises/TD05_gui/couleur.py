import tkinter as tk
from tkinter import font
import random

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color) : 
    canvas.create_oval((i,j), (i,j), outline=color)

def ecran_aleatoire() :
    for i in range(256) :
        for j in range(256) :
            draw_pixel(i,j,get_color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def degrade_gris() :
    for i in range(256) :
        for j in range(256) :
            draw_pixel(i, j, get_color(0 + i, 0 + i, 0 + i))
    
def degrade_2D() :
    for i in range(256) :
        for j in range(256) :
            draw_pixel(i, j, get_color(0 + j, 0, 255 - i))

root = tk.Tk()
aléatoire = tk.Button(root, text="Aléatoire", font=("helvetica", "26"), command=ecran_aleatoire)
bouton2 = tk.Button(root, text="Dégradé de gris", font=("helvetica", "26"), command=degrade_gris)
bouton3 = tk.Button(root, text="Dégradé 2D", font=("helvetica", "26"), command=degrade_2D)
canvas = tk.Canvas(root, bg='black', height=256, width=256)
canvas.grid(rowspan=3, column=1)
aléatoire.grid(row=0, column=0)
bouton2.grid(row=1, column=0)
bouton3.grid(row=2, column=0)
root.mainloop()