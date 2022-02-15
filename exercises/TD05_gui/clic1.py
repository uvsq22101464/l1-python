import tkinter as tk
root = tk.Tk()
def coloriage(event) :
    pixel = canvas.create_oval((event.x, event.y), (event.x, event.y), outline='red')
canvas = tk.Canvas(width=500, height=500, bg='black')

canvas.bind("<Button-1>", coloriage)

canvas.grid()

root.mainloop()