import tkinter as tk
root = tk.Tk()
liste = []
def coloriage(event) :
    global liste
    liste.append(event.x)
    liste.append(event.y)
    if len(liste) == 4 :
        if liste[0] < 250 and liste[2] < 250 :
            canvas.create_line((liste[0], liste[1]), (liste[2], liste[3]), fill='blue')
        else :
            canvas.create_line((liste[0], liste[1]), (liste[2], liste[3]), fill='red')
        liste = []
        
canvas = tk.Canvas(width=500, height=500, bg='black')
ligne = canvas.create_line((250, 0), (250, 500), fill='white', width=1)
canvas.bind("<Button-1>", coloriage)

canvas.grid()

root.mainloop()