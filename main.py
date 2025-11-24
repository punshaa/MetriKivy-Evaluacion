import logging
import os
import time
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import platform

# --- CONFIGURACIÓN DE LOGS (MÉTRICAS) ---
# Determinamos dónde guardar el log según el sistema (Android o PC)
if platform == 'android':
    from android.storage import app_storage_path
    log_dir = app_storage_path()
else:
    log_dir = os.path.dirname(os.path.abspath(__file__))

log_file = os.path.join(log_dir, 'metrikivy_metrics.log')

# Configuración del logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
root_logger.addHandler(file_handler)

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        self.counter = 0

        # Elementos de la UI
        self.label_info = Label(text="Métricas de Usuario", font_size='24sp', size_hint=(1, 0.2))
        self.label_counter = Label(text="Clics: 0", font_size='40sp')
        self.label_timer = Label(text="Tiempo sesión: 0s", font_size='20sp')
        
        self.btn_action = Button(text="Registrar Evento (Clic)", size_hint=(1, 0.3), background_color=(0.2, 0.6, 1, 1))
        self.btn_action.bind(on_press=self.registrar_clic)

        self.add_widget(self.label_info)
        self.add_widget(self.label_counter)
        self.add_widget(self.label_timer)
        self.add_widget(self.btn_action)

    def registrar_clic(self, instance):
        self.counter += 1
        self.label_counter.text = f"Clics: {self.counter}"
        # MÉTRICA 1: Registro de eventos (Clics)
        logging.info(f"EVENTO: Botón presionado. Total clics: {self.counter}")
        print(f"Métrica registrada: Clic #{self.counter}")

class MetriKivyApp(App):
    def build(self):
        self.start_time = time.time()
        # MÉTRICA: Inicio de sesión
        logging.info("SESION: Aplicación iniciada")
        
        # Actualizar el timer en pantalla cada segundo
        Clock.schedule_interval(self.update_timer, 1)
        return MainLayout()

    def update_timer(self, dt):
        elapsed = int(time.time() - self.start_time)
        self.root.label_timer.text = f"Tiempo sesión: {elapsed}s"

    def on_stop(self):
        # MÉTRICA 2: Tiempo total de sesión al cerrar
        duration = time.time() - self.start_time
        logging.info(f"SESION: Aplicación cerrada. Duración total: {duration:.2f} segundos")
        logging.info("-" * 30)

if __name__ == '__main__':
    MetriKivyApp().run()