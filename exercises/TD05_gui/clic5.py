import tkinter as tk
root = tk.Tk()
cpt = 1
liste = []
def coloriage(event) :
    global cpt
    if cpt <= 8 :
        canvas.create_oval((event.x-25, event.y-25), (event.x+25, event.y+25), outline='red', fill='red')
        liste.append(event.x)
        liste.append(event.y)
    if cpt == 9 :
        for i in range(8) :
            canvas.itemconfigure(canvas.find_closest(liste[-1], liste[-2]), outline='yellow', fill='yellow')
            del liste[-1]
            del liste[-1]
            print(liste)
    if cpt == 10 :
        canvas.destroy()
        tk.Canvas(width=500, height=500, bg='black')
        cpt = 0
    cpt += 1
    print(liste)
canvas = tk.Canvas(width=500, height=500, bg='black')
canvas.bind("<Button-1>", coloriage)

canvas.grid()

root.mainloop()