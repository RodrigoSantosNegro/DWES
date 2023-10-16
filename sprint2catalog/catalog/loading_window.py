# Importamos las bibliotecas necesarias
import threading  # Para ejecutar tareas en segundo plano
import time  # Para simular una carga ficticia
import tkinter as tk  # Para crear la interfaz gráfica

# Definimos una clase para la ventana de carga
class LoadingWindow:
    def __init__(self, root):
        # Configuramos la ventana de carga
        self.root = root
        self.root.title("Cargando...")  # Título de la ventana
        self.root.geometry("170x120")  # Tamaño de la ventana
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

    # Método para simular una carga de datos
    def fetch_json_data(self):
        time.sleep(5)  # Simulamos una carga de 5 segundos
        # Luego de cargar los datos (o completar la tarea), cerramos la ventana de carga
        self.root.destroy()

# Creamos una instancia de la ventana de carga
root = tk.Tk()
loading_window = LoadingWindow(root)
root.mainloop()  # Ejecutamos la aplicación
