import tkinter as tk
root = tk.Tk()
def coloriage(event) :
    if event.x < 250 :
        canvas.create_oval((event.x-25, event.y-25), (event.x+25, event.y+25), outline='blue', fill='blue')
    if event.x > 250 :
        canvas.create_oval((event.x-25, event.y-25), (event.x+25, event.y+25), outline='red', fill='red')
        
canvas = tk.Canvas(width=500, height=500, bg='black')
ligne = canvas.create_line((250, 0), (250, 500), fill='white', width=1)
canvas.bind("<Button-1>", coloriage)

canvas.grid()

root.mainloop()