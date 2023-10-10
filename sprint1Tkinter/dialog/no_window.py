from tkinter import ttk

class NoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("No")

        self.label = ttk.Label(self.root, text="Pues te la realizo igual.")
        self.label.pack()