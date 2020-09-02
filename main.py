# -----------------------------------------------------------------------------
#                Sanosil desinfectants for life
# Prohibida su venta y reproducción sin el consentimiento escrito del autor
# All rights reserved
# @Author: Manuel Calzadillas
# @July 2020
# @Versión 1.0.0
#
# -----------------------------------------------------------------------------

# --------- Paquetes necesarios para el funcionamiento ------------------------
from tkinter import *
import home, inicio
import RPi.GPIO as GPIO
import datetime as dt
import board
import os
import adafruit_dht
import sqlite3
# -----------------------------------------------------------------------------


# -------------------------- Clase principal ----------------------------------
class Interfaz(Tk):
    def __init__(self):
        super().__init__()  # Se inicia la ventana
        self.rasp_variables()
        self.variables()

        self.title("Sanosil 1.0.0")  # Título de la interfaz
        self.overrideredirect(True)  # Se elimina la barra superior
        self.config(bg="white", cursor="dot")
        self.geometry("800x480")
        self.geometry("%dx%d" % (self.winfo_screenwidth(),
                             self.winfo_screenheight()))
        self.actualizar_temp_humedad()
        home.Home(self).tkraise()
        # inicio.Inicio(self).tkraise()

    def variables(self):
        self.mensaje = "STATUS: LISTO PARA OPERAR"
        self.fecha_inicio = None
        self.hora_inicio = None
        self.fecha_termino = None
        self.hora_termino = None
        self.database = sqlite3.connect("/home/pi/Desktop/Interfaz-Sanosil/program_database.db")
        self.usernames = []
        self.program_object = None
        self.vol = 0
        self.concentracion = 0
        self.time = (self.vol * self.concentracion) * 2
        self.timer = 0
        self.current_button_state = 0
        self.current_program = 0
        self.myFont = ("Verdana", 12)
        self.myFont_bold = ("Verdana", 12, "bold")
        # self.color = "#2ECC71"
        self.color = "green"
        self.selected_color = "white"
        self.color_alertas = self.color
        self.sesion = ""
        # Usernames
        usernames = self.database.execute("SELECT username FROM user_settings;")
        for row in usernames:
            self.usernames.append(row[0])
        # Passwords
        self.passwords = {
            self.usernames[0]: "ADMIN",
            self.usernames[1]: "1234", self.usernames[2]: "1234",
            self.usernames[3]: "1234", self.usernames[4]:"SERVICE"
        }

    def actualizar_temp_humedad(self):
         try:
             self.temp_dht = self.dhtDevice.temperature
             self.humidity_dht = self.dhtDevice.humidity
         except RuntimeError as error:
             print(error)

         self.after(2000, self.actualizar_temp_humedad)

    def rasp_variables(self):
        self.pulsos = 0
        self.tanque_lleno = 0
        self.temp_dht = 25
        self.temp_dht_inicial = 0
        self.humidity_dht = 50
        self.humidity_dht_inicial = 0
        self.dhtDevice = adafruit_dht.DHT11(board.D16)
        self.bomba_entrada = 26
        self.bomba_salida = 20
        self.ch = (self.bomba_entrada, self.bomba_salida, 21)
        self.sensor_flujo = 23
        self.ml = 0
        self.flotador = 12
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_flujo,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.sensor_flujo, GPIO.RISING)
        GPIO.add_event_callback(self.sensor_flujo, self.count_pulses)
        GPIO.setup(self.flotador, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.ch, GPIO.OUT)
        self.pin_on(self.ch, 1)

    def shutdown(self):
         os.system("sudo shutdown -h now")

    # Prender y apagar pines en la raspberry
    def pin_on(self, ch, s):
         GPIO.output(ch, s)

    # Medir sensor_flujo
    def count_pulses(self, event=None):
        self.pulsos = self.pulsos + 1
# -----------------------------------------------------------------------------

# ------------------------ Inicia aplicación ----------------------------------
Interfaz().mainloop()
GPIO.cleanup()
