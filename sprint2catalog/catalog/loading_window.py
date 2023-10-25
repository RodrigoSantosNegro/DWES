# Importamos las bibliotecas necesarias
import threading  # Para ejecutar tareas en segundo plano
from window import MainWindow
import tkinter as tk  # Para crear la interfaz gráfica
import requests

# Definimos una clase para la ventana de carga
class LoadingWindow:
    def __init__(self, root):
        self.finished = False
        self.json_data = []
        # Configuramos la ventana de carga
        self.root = root

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2 
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2 
        self.root.geometry (f"+{int (x)}+{int(y)}")

        self.root.title("Cargando...")  # Título de la ventana
        self.root.resizable(False, False)  # No se puede redimensionar

        # Creamos una etiqueta que muestra "Cargando datos..."
        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14))
        self.label.pack(side=tk.TOP, pady=10)

        # Obtenemos el color de fondo de la etiqueta para el círculo de carga
        label_bg_color = self.label.cget("bg")

        # Creamos un lienzo (canvas) para el círculo de progreso
        self.canvas = tk.Canvas(self.root, width=60, height=60, bg=label_bg_color)
        self.canvas.pack()

        # Inicializamos el progreso en 0
        self.progress = 0

        # Dibujamos el círculo de progreso inicial
        self.draw_progress_circle(self.progress)

        # Iniciamos la animación de carga
        self.update_progress_circle()

        # Creamos un hilo para ejecutar la tarea ficticia en segundo plano
        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()
        self.check_thread()



    # Método para dibujar el círculo de progreso
    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")  # Borramos el círculo existente
        angle = int(360 * (progress / 100))  # Calculamos el ángulo en función del progreso

        # Creamos el arco del círculo de progreso
        self.canvas.create_arc(10, 10, 35, 35, start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)

    # Método para actualizar el progreso del círculo
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 1  # Incrementamos el progreso en 1
        else:
            self.progress = 0  # Reiniciamos el progreso cuando llega al 100%

        # Dibujamos el círculo actualizado
        self.draw_progress_circle(self.progress)
        # Programamos una llamada futura para continuar la animación
        self.root.after(5, self.update_progress_circle)

    # Método para cargar datos de un JSON ubicado en GitHub
    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/RodrigoSantosNegro/DWES/main/resources/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json()
            self.finished = True

    def check_thread(self):
        if(self.finished):
            self.root.destroy()
            launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)

def launch_main_window(json_data):
    root = tk.Tk()
    app = MainWindow(root, json_data)
    root.mainloop()