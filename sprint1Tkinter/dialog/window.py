import tkinter as ttk
from yes_window import YesWindow
from no_window import NoWindow

class MainWindow:

    def __init__(self, root):
        self.root = root

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.root, text="¿Desea realizar alguna acción?")
        self.label.pack()

        self.yes_button = ttk.Button(self.frame, text="Sí", command=self.open_yes_window)
        self.yes_button.pack(side=ttk.LEFT)

        self.no_button = ttk.Button(self.frame, text="No", command=self.open_no_window)
        self.no_button.pack(side=ttk.RIGHT)

    def open_yes_window(self):
        yes_root = ttk.Toplevel(self.root)
        app = YesWindow(yes_root)

    def open_no_window(self):
        no_root = ttk.Toplevel(self.root)
        app = NoWindow(no_root)


if __name__ == "__main__":
    root = ttk.Tk()
    app = MainWindow(root)
    root.mainloop()