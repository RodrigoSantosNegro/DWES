import tkinter as ttk
from cell import CatalogCell


class MainWindow:

    def __init__(self,root):
        root.title("MainWindow")
        self.root = root 

        self.cells = [
            CatalogCell("catalog/data/unedited/cuchara.jpg"),
            CatalogCell("catalog/data/unedited/mike.png"),
            CatalogCell("catalog/data/unedited/op.jpg"),
            CatalogCell("catalog/data/unedited/padreando.png"),
            CatalogCell("catalog/data/unedited/women.jpg")
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, compound= ttk.BOTTOM)
            label.grid(row=i,column=0)


if __name__ == "__main__":
    root = ttk.Tk()
    app = MainWindow(root)
    root.mainloop()