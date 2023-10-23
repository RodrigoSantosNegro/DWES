from io import BytesIO
import tkinter as ttk

import requests

from PIL import Image, ImageTk
from detail_window import DetailWindow
from cell import Cell


class MainWindow:

    def on_button_click(self, cell):
        #Pasamos los parámetros de cell para pasarle a DetailWindow
        detail_window = DetailWindow(cell.image_tk, cell.title, cell.description)
        detail_window.mainloop()

    def load_image(self, url):
        response = requests.get(url)
        image_data = Image.open(BytesIO(response.content))
        image = ImageTk.PhotoImage(image_data)
        return image

    def __init__(self,root, json_data):
        root.title("MainWindow")
        self.root = root 
        #guardamos en cells todas las imágenes que queremos mostrar
        self.cells = []
        data = json_data
        for x in range(len(data)):
            name = data[x].get("name")
            description = data[x].get("description")
            image_url = data[x].get("image_url")
            image = self.load_image(image_url)

            self.cells.append(Cell (image, name, description))

        #Asignamos a cada imagen una fila distinta (i)
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image= cell.image_tk, text=cell.title, compound= ttk.BOTTOM)
            label.grid(row=i,column=0)
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_click(cell))