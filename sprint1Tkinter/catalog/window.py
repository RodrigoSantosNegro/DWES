import tkinter as ttk
from cell import Cell


class MainWindow:

    def __init__(self,root):
        root.title("MainWindow")
        self.root = root 

        self.cells = [
            Cell("catalog/data/edited/cuchara.jpg"),
            Cell("catalog/data/edited/mike.png"),
            Cell("catalog/data/edited/op.jpg"),
            Cell("catalog/data/edited/padreando.jpg"),
            Cell("catalog/data/edited/women.jpg")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, compound= ttk.BOTTOM)
            label.grid(row=i,column=0)


if __name__ == "__main__":
    root = ttk.Tk()
    app = MainWindow(root)
    root.mainloop()