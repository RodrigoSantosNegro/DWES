from io import BytesIO
import tkinter as ttk
from tkinter import messagebox

import requests

from PIL import Image, ImageTk
from detail_window import DetailWindow
from cell import Cell


class MainWindow:

    def on_button_click(self, cell):
        #Pasamos los parámetros de cell para pasarle a DetailWindow
        detail_window = DetailWindow(cell.image_tk, cell.title, cell.description)
        detail_window.mainloop()

    #Cargamos la imagen...
    def load_image(self, url):
        response = requests.get(url)
        image_data = Image.open(BytesIO(response.content))
        image = ImageTk.PhotoImage(image_data)
        return image
    
    #Mostramos el texto acerca del desarrollador
    def show_about_dialog(self):
        about_message = "Acerca del desarrollador:\n\nEste programa fue desarrollado por Rodrigo."
        messagebox.showinfo("Acerca de", about_message)

    #Creamos un menú en la barra superior
    def create_menu(self):
        menu_bar = ttk.Menu(self.root)
        help_menu = ttk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Acerca de", command=self.show_about_dialog)
        menu_bar.add_cascade(label="Ayuda", menu=help_menu)
        self.root.config(menu=menu_bar)

    def __init__(self,root, json_data):
        root.title("MainWindow")
        self.root = root 
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2 
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2 
        self.root.geometry (f"+{int (x)}+{int(y)}")
        
        # Crear un Canvas con una barra de desplazamiento vertical
        canvas = ttk.Canvas(root)
        canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.config(yscrollcommand=scrollbar.set)

        # Crear un marco para contener las celdas
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        
        canvas.grid_rowconfigure(0, weight=1)
        canvas.grid_columnconfigure(0, weight=1)
        
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
            label = ttk.Label(frame, image=cell.image_tk, text=cell.title, compound=ttk.BOTTOM)
            label.grid(row=i, column=0, sticky="w")
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_click(cell))

        # Configurar el enlace de desplazamiento del Canvas para todo el contenido
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        frame.bind("<Configure>", on_configure)
        
        #Creamos el menú superior
        self.create_menu()