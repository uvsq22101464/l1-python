import tkinter as tk
root = tk.Tk()
cpt = 1
def coloriage(event) :
    global cpt
    if cpt != 10 :
        if cpt % 2 != 0 :
            canvas.itemconfigure(carre, fill='white')
            cpt += 1
        else :
            canvas.itemconfigure(carre, fill='black')
            cpt += 1
    else :
        root.destroy()
        
canvas = tk.Canvas(width=500, height=500, bg='black')
carre = canvas.create_rectangle((125, 125), (375, 375), outline='white')
canvas.bind("<Button-1>", coloriage)

canvas.grid()

root.mainloop()