import tkinter as ttk
from detail_window import DetailWindow
from cell import Cell


class MainWindow:

    def on_button_click(self, cell):
        #Pasamos los parámetros de cell para pasarle a DetailWindow
        detail_window = DetailWindow(cell.image_tk, cell.title, cell.description)
        detail_window.mainloop()

    def __init__(self,root):
        root.title("MainWindow")
        self.root = root 
        #guardamos en cells todas las imágenes que queremos mostrar
        self.cells = [
            Cell("catalog/data/unedited/cuchara.jpg", "Cuchara", "Una cuchara de metal :D"),
            Cell("catalog/data/unedited/mike.png", "Mike Wasouski", "El increíble monstruo de Monstruos SA aparece en pantalla"),
            Cell("catalog/data/unedited/op.jpg", "Mugiwaras", "Símbolo pirata mu guapo de uno de los mejores animes de todos los tiempos"),
            Cell("catalog/data/unedited/padreando.jpg", "El Nano", "Qué decir, es el Nano, mi padre, tu padre, nuestro padre"),
            Cell("catalog/data/unedited/women.jpg", "Women Cafe", "jaja, women. *Sorbito al cafe* jajaja")
        ]
        #Asignamos a cada imagen una fila distinta (i)
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, text=cell.title, compound= ttk.BOTTOM)
            label.grid(row=i,column=0)
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_click(cell))


if __name__ == "__main__":
    root = ttk.Tk()
    app = MainWindow(root)
    root.mainloop()