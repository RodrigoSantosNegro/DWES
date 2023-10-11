import tkinter as ttk
from cell import Cell


class MainWindow:

    def __init__(self,root):
        root.title("MainWindow")
        self.root = root 
        #guardamos en cells todas las imágenes que queremos mostrar
        self.cells = [
            Cell("catalog/data/unedited/cuchara.jpg"),
            Cell("catalog/data/unedited/mike.png"),
            Cell("catalog/data/unedited/op.jpg"),
            Cell("catalog/data/unedited/padreando.jpg"),
            Cell("catalog/data/unedited/women.jpg")
        ]
        #Asignamos a cada imagen una fila distinta (i)
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, compound= ttk.BOTTOM)
            label.grid(row=i,column=0)


if __name__ == "__main__":
    root = ttk.Tk()
    app = MainWindow(root)
    root.mainloop()