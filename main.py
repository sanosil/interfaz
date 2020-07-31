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
import time
# import RPi.GPIO as GPIO
# -----------------------------------------------------------------------------


# -------------------------- Clase principal ----------------------------------
class Interfaz(Tk):
    def __init__(self):
        super().__init__()  # Se inicia la ventana
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
        self.title("Sanosil 1.0.0")  # Título de la interfaz
        self.overrideredirect(True)  # Se elimina la barra superior
        self.config(bg="white")

        # self.geometry("%dx%d" % (self.winfo_screenwidth(),
        #                       self.winfo_screenheight()))
        self.geometry("800x480")

        # home.Home(self).tkraise()
        inicio.Inicio(self).tkraise()
# -----------------------------------------------------------------------------

# ------------------------ Inicia aplicación ----------------------------------
Interfaz().mainloop()
