from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, path):
        self.path = path

        image = Image.open(self.path)
        self.image_tk = ImageTk.PhotoImage(image)