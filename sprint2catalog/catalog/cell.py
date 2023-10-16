from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, path, title, description):
        self.path = path
        self.title = title
        self.description = description

        image = Image.open(self.path)
        #Redimensionamos la imagen NO editada
        image = image.resize((100, 100), Image.Resampling.LANCZOS)
        #La lanzamos
        self.image_tk = ImageTk.PhotoImage(image)