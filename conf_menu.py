from tkinter import *
from datetime import datetime, date
import user_menu, language_menu, wifi_menu, program_menu, test

class Conf_menu():
    def __init__(self, root, root_frame):
        # variables
        self.root = root
        self.root_frame = root_frame
        now = datetime.now()
        self.primera_mitad = Frame(self.root_frame.main_container, bg="white")
        self.primera_mitad.pack(side=LEFT)
        # Barra de fecha y hora con texto
        self.barra_FyH = Frame(self.primera_mitad, bd=3,
            bg=self.root.selected_color, relief=RIDGE)
        self.barra_FyH.pack(pady=(50,10), side=TOP)
        self.FyH_label = Label(self.barra_FyH, text="Fecha y Hora",
            bg=self.root.selected_color, font=("Verdana", 14, "bold"))
        self.FyH_label.pack(padx=80, pady=10)
        # Frame de hora y fecha editable
        self.FyH_frame = Frame(self.primera_mitad, bd=3,
            relief=SUNKEN, bg="yellow")
        self.FyH_frame.pack(side=TOP, padx=45, pady=(10,20))
        self.FyH_valores = Label(self.FyH_frame, font=self.root.myFont,
            bg="yellow")
        self.FyH_valores.pack(padx=70, pady=10)
        self.FyH_valores.bind("<Button-1>", self.set_date_time)
        # frame segunda segunda mitad
        self.segunda_mitad = Frame(self.root_frame.main_container, bg="white")
        self.segunda_mitad.pack(fill=BOTH, expand=YES, side=LEFT)
        # Frame de timer
        self.barra_timer = Frame(self.segunda_mitad, bd=3,
            bg=self.root.selected_color, relief=RIDGE)
        self.barra_timer.pack(side=TOP, pady=(50,15))
        self.timer_label = Label(self.barra_timer, bg=self.root.selected_color,
            font=("Verdana", 14, "bold"), text="Configurar Timer")
        self.timer_label.pack(padx=75, pady=10)
        # Valore editables del timer
        self.timer_valores_frame = Frame(self.segunda_mitad, bg="white")
        self.timer_valores_frame.pack(side=TOP, padx=10, pady=(10,20))
        for i, bg in self.root_frame.timer_valores:
            self.dias(self.timer_valores_frame, i, bg)

        # Botón de usuario
        self.frame_inferior = Frame(self.root_frame, bg="white")
        self.frame_inferior.pack(ipady=78, expand=YES, fill=X)
        self.settings = [("USUARIO", self.user_settings),
                         ("PROGRAMA", self.program_settings),
                         ("IDIOMA", self.language_settings),
                         ("WI-FI", self.wifi_settings),
                         ("TEST", self.test)
                        ]

        for text, command in self.settings:
            if self.root.id[self.root.sesion] == 0 and text != "TEST":
                self.settings_buttons(text, command)
            elif self.root.id[self.root.sesion] == 4 and text == "TEST":
                self.settings_buttons(text, command)
            elif text != "USUARIO" and text != "TEST":
                self.settings_buttons(text,command)

        self.actualizar_hora()



    def settings_buttons(self, text, command):
        Button(self.frame_inferior, fg="white", command=command,
            font=("Verdana", 18), text=text, bg="red", bd=5).pack(side=LEFT,
                                padx=30)


    def dias(self, frame, text, bg):
        dia = Label(frame, text=text, bg=bg, fg="white", font=("Verdana", 15),
            bd=3, relief=RAISED)
        dia.pack(side=LEFT)
        dia.bind("<Button-1>", self.edit_timer)

    def user_settings(self):
        self.frame_inferior.destroy()
        self.root_frame.main_container.destroy()
        user_menu.User_menu(self.root, self.root_frame)

    def test(self):
        self.frame_inferior.destroy()
        self.root_frame.main_container.destroy()
        test.Test(self.root, self.root_frame)

    def language_settings(self):
        self.frame_inferior.destroy()
        self.root_frame.main_container.destroy()
        language_menu.Language_menu(self.root, self.root_frame)

    def wifi_settings(self):
        self.frame_inferior.destroy()
        self.root_frame.main_container.destroy()
        wifi_menu.Wifi_menu(self.root, self.root_frame)

    def program_settings(self, event=None):
        self.frame_inferior.destroy()
        self.root_frame.main_container.destroy()
        program_menu.Program_menu(self.root, self.root_frame)

    def edit_timer(self, event=None):
        print("edit timer")

    def set_date_time(self, event=None):
        print("set date and time")

    def actualizar_hora(self):
        try:
            if self.root_frame.current_menu == "CONF":
                today = date.today()
                now = datetime.now()
                today_str = today.strftime("%d/%m/%y") + " " + now.strftime("%H:%M:%S")
                self.FyH_valores.config(text=today_str)
                self.root.after(1000, self.actualizar_hora)
        except:
            pass
