import tkinter as tk
taille = int(input("choisir la taille de l'image"))
i = 0
root = tk.Tk()
toile = tk.Canvas(root, width=taille, height=taille, bg='black')
while True :
    toile.create_oval((i, i), (taille - i, taille - i), outline='blue', width=10)
    toile.create_oval((i+10, i+10), (taille - (i+10), taille - (i+10)), outline='green', width=10)
    toile.create_oval((i+20, i+20), (taille - (i+20), taille - (i+20)), outline='black', width=10)
    toile.create_oval((i+30, i+30), (taille - (i+30), taille - (i+30)), outline='yellow', width=10)
    toile.create_oval((i+40, i+40), (taille - (i+40), taille - (i+40)), outline='magenta', width=10)
    toile.create_oval((i+50, i+50), (taille - (i+50), taille - (i+50)), outline='red', width=10)
    i += 60
    if i >= taille / 2 :
        break
toile.grid()
root.mainloop()