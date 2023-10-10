from tkinter import ttk 

class YesWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Sí")

        self.label = ttk.Label(self.root, text="Así me gusta.")
        self.label.pack()