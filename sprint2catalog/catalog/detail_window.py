import tkinter as tk

class DetailWindow:
    def __init__(self, img, ttl, desc):
        root = tk.Toplevel()
        
        #Añadimos un label para cada campo especificando qué es lo que se le pasa en cada caso

        label1 = tk.Label(root ,image=img)
        label1.pack()

        label2 = tk.Label(root, text=ttl)
        label2.pack()

        label3 = tk.Label(root, text=desc)
        label3.pack()

        root.mainloop()