# ----------------------------------------------------------------------------#
#                Sanosil desinfectants for life				      #
#									      #
# @Copyright 2020 All rights reserved					      #
# @Author: Manuel Calzadillas						      #
# @Mail: menycalzadil@hotmail.com					      #
# @July 2020								      #
# @Versión 1.0.0							      #
#									      #
# ----------------------------------------------------------------------------#

# --------- Paquetes necesarios para el funcionamiento ------------------------
from tkinter import *
import home
import datetime as dt
import sqlite3
import os
# import board
# import adafruit_dht
# import RPi.GPIO as GPIO
# -----------------------------------------------------------------------------


# -------------------------- Clase principal ----------------------------------
class Interfaz(Tk):
    def __init__(self):
        super().__init__()  # Se inicia la ventana
        self.mode = "pc"
        self.variables()
        if self.mode == "rasp":
            self.rasp_variables()
            self.actualizar_temp_humedad()
            self.geometry("%dx%d" % (self.winfo_screenwidth(),
                            self.winfo_screenheight()))
        else:
            self.geometry("%dx%d" % (self.width, self.height))
        self.teclado = None
        self.title("Sanosil 1.0.0")  # Título de la interfaz
        self.overrideredirect(True)  # Se elimina la barra superior
        self.config(bg="white", cursor="dot")
        self.frames.append(home.Home(self))

    def variables(self):
        self.width = 800
        self.height = 480
        # Inputs
        self.concentracion = 0
        self.temp_dht = 25
        self.humidity_dht = 50
        if self.mode == "pc":
            self.path="images/"
            self.database = sqlite3.connect("program_database.db")
            self.s1 = [0,1]
            self.s2 = [1,1]
            self.be = [5,1]
            self.bs = [6,1]
            self.ven = [13,1]
        else:
            self.path="/home/pi/Desktop/interfaz/images/"
            self.database = sqlite3.connect("/home/pi/Desktop/interfaz/program_database.db")
        self.mensaje = "STATUS: LISTO PARA OPERAR"
        self.fecha_inicio = None
        self.hora_inicio = None
        self.fecha_termino = None
        self.hora_termino = None
        self.frames = []
        self.program_object = None
        self.vol = 0
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
        self.actualizar_valores()



    def actualizar_valores(self):
        # Usernames
        self.usernames = []
        usernames = self.database.execute("SELECT username FROM user_settings;")
        for row in usernames:
            self.usernames.append(row[0])

        # Passwords
        passwords = self.database.execute("SELECT password FROM user_settings;")
        self.passwords = []
        for row in passwords:
            self.passwords.append(row[0])
        sesion = self.database.execute("SELECT last FROM last_session;")
        for row in sesion:
            self.sesion = row[0]
        idioma = self.database.execute("SELECT language FROM user_settings " \
            f"WHERE username = '{self.sesion}';")
        for row in idioma:
            self.language = row[0]
        self.id = {self.usernames[0]:0, self.usernames[1]:1,
                    self.usernames[2]:2, self.usernames[3]:3,
                    self.usernames[4]:4}

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
        # inputs
        self.temp_dht = 25
        self.temp_dht_inicial = 0
        # outputs
        self.s1 = [0,1]
        self.s2 = [1,1]
        self.be = [5,1]
        self.bs = [6,1]
        self.ven = [13,1]
        self.voltaje = (20)
        self.outputs = (0, 1, 5, 6, 13)
        self.humidity_dht = 50
        self.humidity_dht_inicial = 0
        self.dhtDevice = adafruit_dht.DHT11(board.D16)
        self.sensor_flujo = 23
        self.ml = 0
        self.flotador = 12
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_flujo,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.sensor_flujo, GPIO.RISING)
        GPIO.add_event_callback(self.sensor_flujo, self.count_pulses)
        GPIO.setup(self.flotador, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.outputs, GPIO.OUT)
        GPIO.setup(self.voltaje, GPIO.OUT)
        self.pin_on(self.outputs, 1)
        self.pin_on(self.voltaje, 1)

    def shutdown(self):
         GPIO.cleanup()
         os.system("sudo shutdown -h now")

    # Prender y apagar pines en la raspberry
    def pin_on(self, ch, s):
        if self.mode=="pc":
            print(ch, s)
        else:
            GPIO.output(ch, s)

    # Medir sensor_flujo
    def count_pulses(self, event=None):
        self.pulsos = self.pulsos + 1
# -----------------------------------------------------------------------------

# ------------------------ Inicia aplicación ----------------------------------
Interfaz().mainloop()
