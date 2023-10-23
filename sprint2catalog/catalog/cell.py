from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, image, title, description):
        self.image_tk = image
        self.title = title
        self.description = description