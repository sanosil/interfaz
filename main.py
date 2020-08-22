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
# -----------------------------------------------------------------------------


# -------------------------- Clase principal ----------------------------------
class Interfaz(Tk):
    def __init__(self):
        super().__init__()  # Se inicia la ventana
        self.rasp_variables()
        self.variables()

        self.title("Sanosil 1.0.0")  # Título de la interfaz
        self.overrideredirect(True)  # Se elimina la barra superior
        self.config(bg="white")
        self.geometry("800x480")
        # self.geometry("%dx%d" % (self.winfo_screenwidth(),
        #                       self.winfo_screenheight()))
        self.actualizar_temp_humedad()
        # home.Home(self).tkraise()
        inicio.Inicio(self).tkraise()

    def variables(self):
        self.myFont = ("Verdana", 12)
        self.color = "#2ECC71"
        self.sesion = ""
        # Usernames
        self.usernames = ("Admin", "Service", "Operador 1", "Operador 2",
                    "Operador 3")
        # Passwords
        self.passwords = {
            self.usernames[0]: "ADMIN",
            self.usernames[1]: "SERVICE", self.usernames[2]: "1234",
            self.usernames[3]: "1234", self.usernames[4]:"1234"
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
        self.temp_dht = 25
        self.humidity_dht = 50
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
