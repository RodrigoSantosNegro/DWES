import tkinter as ttk
from detail_window import DetailWindow
from cell import Cell


class MainWindow:

    def on_button_click(self, cell):
        #Pasamos los parámetros de cell para pasarle a DetailWindow
        detail_window = DetailWindow(cell.image_tk, cell.title, cell.description)
        detail_window.mainloop()

    def __init__(self,root, json_data):
        root.title("MainWindow")
        self.root = root 
        #guardamos en cells todas las imágenes que queremos mostrar
        self.cells = [
            
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