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
        self.geometry("800x400")

        # Home(self).tkraise()
        Inicio(self).tkraise()
# -----------------------------------------------------------------------------

# ---------------------- Ventana de inicialización ----------------------------
class Home(Frame):
    def __init__(self, root):
        super().__init__(root)  # Se inicializa la ventana
        self.root = root
        self.grid(column=0, row=0)  # Se coloca la ventana home en interfaz
        self.config(bg="white")  # Fondo blanco
        # Colores para hacer el efecto de desvanecido y aparecer
        self.colores = ["#777777", "#888888", "#999999", "#AAAAAA", "#BBBBBB",
                        "#DDDDDD", "#EEEEEE", "#EFEFEF", "#F0F0F0"]
        self.count = 0
        self.gam = 1  # Color gamma de la imagen
        self.version = Label(self, bg="white", fg="#444444",text="Version 1.0.0",
                            font=("Verdana", 18), anchor=S)
        self.version.grid(column=0, row=1)
        # Logo de la empresa
        self.logo_file = PhotoImage(file="images//logo.png").subsample(2)
        # Widget del logo
        self.logo = Label(self, bg="white", image=self.logo_file)
        self.logo.image = self.logo_file  # Keep the reference
        self.logo.grid(column=0, row=0, padx=100, pady=100)
        self.welcome = Label(self, bg="white", text="BIENVENIDO",
                            fg="white", font=("Verdana", 40, "bold"))
        self.after(3000, self.animacion)

# -------------------- Animación de inicio ------------------------------------
    def animacion(self):
        # Cambian los colores gamma de la imagen
        self.logo_file.config(gamma=self.gam)
        # Cambian los colores del label de version
        self.version.config(foreground=self.colores[self.count])
        # Condicion para terminar la animación
        if self.gam < 256:
            # Se multiplica el valor gamma por 2
            self.gam = self.gam * 2
            # SE reinicia la animación
            self.after(100, self.animacion)
            # Se incrementa la variable de los colores del label
            self.count = self.count + 1
        # Valor alternativo de la condicional
        else:
            # Se borran los elementos del frame
            self.version.grid_forget()
            self.logo.grid_forget()
            #----------------------------------
            # Se añade un nuevo elemento al frame
            self.welcome.grid(column=0, row=0, padx=200, pady=150)
            # Se inicia la animación dos
            self.after(1000, self.animacion_dos)
# -----------------------------------------------------------------------------

# -------------------- Animación dos ------------------------------------------
    def animacion_dos(self):
        self.welcome.config(fg=self.colores[self.count - 1])
        if self.count > 0:
            self.count = self.count - 1
            self.after(100, self.animacion_dos)
        else:
            self.welcome.config(fg="#444444")
            self.after(2000, self.animacion_tres)
# -----------------------------------------------------------------------------
# ----------------------- Animación tres --------------------------------------
    def animacion_tres(self):
        self.welcome.config(fg=self.colores[self.count])
        if self.count < 8:
            self.count = self.count + 1
            self.after(100, self.animacion_tres)
        else:
            self.welcome.config(fg="white")
            self.welcome.grid_forget()
            self.grid_forget()
            Inicio(self.root).tkraise()
# -----------------------------------------------------------------------------

# --------------------- Termina la ventana home -------------------------------

#---------------------- Ventana de inicio -------------------------------------
class Inicio(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(bg="white")
        self.root = root
        self.usuario = "Admin"
        self.grid(column=0, row=0)
        self.user_container = Frame(self, bg="white")
        self.user_container.grid(column=0, row=0)
        self.user_images = {
            "admin": PhotoImage(file="images//Admin.png").subsample(4),
            "service": PhotoImage(file="images//Service.png").subsample(4),
            "user": PhotoImage(file="images//User.png").subsample(4)
        }
        self.sel_label = Label(self.user_container, bg="white",
                    font=("Verdana", 18, "bold"), text="Seleccione\nusuario")
        self.sel_label.grid(column=1, row=0, padx=(100, 100), pady=(50, 50))

        # Usuario Administrador
        self.frame_admin = Frame(self.user_container, bg="white", takefocus=1,
                        highlightthickness=2, highlightcolor=root.color,
                        highlightbackground="white")
        self.frame_admin.focus_set()
        self.admin = Label(self.frame_admin, bg="white",
                    image=self.user_images["admin"])
        self.admin.bind("<Button-1>",
                    lambda e, f=self.frame_admin, u=root.usernames[0]:
                    self.evento(e, f, u))
        self.admin_label = Label(self.frame_admin, bg="white",
                    font=self.root.myFont, text=root.usernames[0])
        self.frame_admin.grid(column=0, row=0)
        self.admin.grid(column=0, row=0)
        self.admin_label.grid(column=0, row=1)
        # Usuario de servicio
        self.frame_service = Frame(self.user_container, bg="white", takefocus=1,
                            highlightthickness=2, highlightcolor=root.color,
                            highlightbackground="white")
        self.service = Label(self.frame_service, bg="white",
                        image=self.user_images["service"])
        self.service_label = Label(self.frame_service, bg="white",
                        font=self.root.myFont, text=root.usernames[1])
        self.frame_service.grid(column=2, row=0)
        self.service.grid(column=0, row=0)
        self.service.bind("<Button-1>",
                    lambda e, f=self.frame_service, u=root.usernames[1]:
                    self.evento(e, f, u))
        self.service_label.grid(column=0, row=1)
        # Operadores
        self.frame_operador = []
        self.labels_operador = []
        self.operador = []
        for i in range(3):
            self.frame_operador.append(Frame(self.user_container, bg="white",
                takefocus=1, highlightcolor=root.color, highlightthickness=2,
                highlightbackground="white"))
            self.operador.append(Label(self.frame_operador[i], bg="white",
                            image=self.user_images["user"]))
            self.labels_operador.append(Label(self.frame_operador[i],
                        bg="white", font=self.root.myFont, text=root.usernames[i+2]))
            if i == 0:
                self.frame_operador[i].grid(column=i, row=1, padx=(70, 0))
            else:
                self.frame_operador[i].grid(column=i, row=1)
            self.operador[i].grid(column=0, row=0)
            self.operador[i].bind("<Button-1>",
                        lambda e, f=self.frame_operador[i], u=root.usernames[i+2]:
                        self.evento(e, f, u))
            self.labels_operador[i].grid(column=0, row=1)


        # Contenedor de la contraseña
        self.container_pass = Frame(self, bg="white")
        self.container_pass.grid(column=0, row=1, padx=(30,0), pady=(30, 0))
        self.pass_label = Label(self.container_pass, bg="white",
                        font=self.root.myFont, text="Contraseña:")
        self.pass_label.grid(column=0, row=0, padx=(0, 30))
        self.password = Entry(self.container_pass, fg="gray",
            font=self.root.myFont, width=60)
        self.password.insert(0, "Escriba la contraseña de %s" % self.usuario)
        self.password.bind("<Button-1>", self.teclado)
        self.password.grid(column=1, row=0)

    def evento(self, event, frame, user):
        self.usuario = user
        self.password.delete(0, 100)
        self.password.insert(0, "Escriba la contraseña de %s" % self.usuario)
        frame.focus_set()

    def teclado(self, event):
        self.grid_forget()
        Teclado(self.root, self.usuario).tkraise()
# --------------------- Termina ventana de inicio -----------------------------

# ---------------------- Teclado númerico password ----------------------------
class Teclado(Frame):
    def __init__(self, root, titulo=None):
        super().__init__(root)
        self.root = root  # Ventana principal
        self.color = "ivory3"
        self.title = titulo
        self.config(bg="white")  # Fondo del frame del teclado
        self.pass_try = ""
        self.grid(column=0, row=0)  # Se pone el teclado en pantalla
        self.myFont = ("Verdana", 17)
        self.contenedor = Frame(self, bg="white")  # color de fondo contenedor
        self.contenedor.grid(column=0, row=0)  # Se pone en fame teclado

        self.rowa = Frame(self.contenedor, bg="white")
        self.rowa.pack(side=TOP, expand=YES, fill=BOTH)

        # Boton regresar
        self.volver = Button(self.rowa, text="Regresar",
                font=self.myFont, activebackground="white", bg=root.color,
                command=self.volver)
        self.volver.pack(side=LEFT, fill=BOTH, expand=YES)

        # --------------------------- titulo teclado --------------------------
        self.frame_titulo_entry = Frame(self.rowa, relief=RIDGE, bd=4)
        self.frame_titulo_entry.pack(side=LEFT)

        self.titulo = Label(self.frame_titulo_entry, font=self.myFont,
                bg="black", fg="white", text=titulo)
        self.titulo.pack(side=TOP, expand=YES, fill=BOTH)

        self.entry_pass = Entry(self.frame_titulo_entry, font=self.myFont,
            width=20)
        self.entry_pass.focus_set()
        self.entry_pass.pack(side=BOTTOM, expand=YES, fill=BOTH)
        # --------------------------------------------------------------------

        # --------------------- Tecla borrar ---------------------------------
        self.del_tecla = Button(self.rowa, background=root.color, text = "DEL",
            font=self.myFont, command=self.borrar)
        self.del_tecla.pack(side=RIGHT, expand=YES, fill=BOTH)
        # --------------------------------------------------------------------

        # Frame de espacio
        self.espacio = Frame(self.contenedor, height=60, relief=RIDGE, bd=3, bg="black")
        self.espacio.pack(side=TOP, expand=YES, fill=BOTH)

        self.mensaje = Label(self.espacio, text="Contraseña incorrecta",
            bg="red", font=("Verdana", 30))
        # ----------------

        self.teclas = (
                ("Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"),
                ("A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ"),
                ("Z", "X", "C", "V", "B", "N", "M", "Enter")
        )
        self.width = 5
        self.rowb = Frame(self.contenedor, bg="white")
        for num in range(9):
            self.tecla(num+1, self.rowb, self.width)
        self.tecla(0, self.rowb, self.width)
        self.rowb.pack(side=TOP, expand=YES, fill=BOTH)

        for row in self.teclas:
            rowc = Frame(self.contenedor, bg="white")
            for tecla in row:
                self.tecla(tecla, rowc, self.width)
            rowc.pack(side=TOP, fill=BOTH, expand=YES)

        self.rowd = Frame(self.contenedor, bg="white")
        self.rowd.pack(side=TOP, expand=YES, fill=BOTH)

        self.left_image = PhotoImage(file="images//left.png").subsample(8)
        self.right_image = PhotoImage(file="images//right.png").subsample(8)

        self.boton_izquierda = Button(self.rowd, image=self.left_image,
                bg=self.color)
        self.space_bar = Button(self.rowd, text="Espacio", font=self.myFont,
                bg=self.color, command=self.space)
        self.boton_derecha = Button(self.rowd, image=self.right_image,
                bg=self.color)
        self.boton_izquierda.pack(side=LEFT, expand=YES, fill=BOTH)
        self.space_bar.pack(side=LEFT, expand=YES, fill=BOTH)
        self.boton_derecha.pack(side=LEFT, expand=YES, fill=BOTH)

    def space(self):
        self.pass_try = self.pass_try + " "
        self.entry_pass.insert(END, " ")

    def volver(self):
        self.grid_forget()
        Inicio(self.root).tkraise()

    def tecla(self, cont, contenedor, width=5):
        contenedor_tecla = Frame(contenedor, bg="white")
        if cont == "Enter":
            tecla = Button(contenedor_tecla, activebackground="white",
                bg=self.root.color, width=16, font=self.myFont, text=cont,
                command=self.ver_pass)
        else:
            tecla = Button(contenedor_tecla, activebackground="white",
                bg=self.color, width=width, font=self.myFont, text=cont,
                command=lambda l=cont: self.letra(l))
        contenedor_tecla.pack(side=LEFT, fill=BOTH, expand=YES)
        tecla.pack(side=LEFT, fill=BOTH, expand=YES)

    def letra(self, letra):
        self.pass_try = self.pass_try + str(letra)
        self.entry_pass.insert(END, letra)

    def borrar(self):
        self.entry_pass.delete(len(self.pass_try)-1)
        self.pass_try = self.pass_try[:-1]

    def ver_pass(self):
        if self.root.passwords[self.title] == self.pass_try:
            self.espacio.config(bg="blue")
            self.root.sesion = self.title
            self.after(500, self.acceso)
        else:
            self.espacio.config(bg="red")
            self.mensaje.pack(expand=YES, fill=BOTH)
            self.after(2000, self.normal)

    def normal(self):
        self.espacio.config(bg="black")
        self.mensaje.pack_forget()

    def acceso(self):
        self.grid_forget()
        Menu_principal(self.root, "Principal").tkraise()
# ---------------- Termina ventana de teclado numérico ------------------------

class Menu_principal(Frame):
    def __init__(self, root, menu):
        super().__init__(root)
        # Variables
        self.root = root
        self.mensaje = ""
        self.current_state = 0
        self.current_menu = "Principal"
        self.timer = 0
        self.state = ("Normal", "Step", "Testing", "Manual")
        self.funcs = ["START/STOP", "CONF", "DIAG", "LOG"]
        self.menu_buttons = []
        # Metodos
        self.config(bg="white")
        self.grid(column=0, row=0)

        self.create_widgets(self.current_menu)

    def create_widgets(self, menu):
        if menu == "Principal":
            self.menu = Frame(self, bg="white", bd=2, relief=SOLID)
            self.menu.grid(column=0, row=0)

            for func in self.funcs:
                self.menu_button_principal(func)

            self.main_container = Frame(self, bg="white")
            self.main_container.grid(column=0, row=1)
            # Imagenes del boton de encendido
            self.start_button_pause = PhotoImage(
                file="images//off.png").subsample(6)
            self.start_button_active = PhotoImage(
                file="images//on.png").subsample(6)

            self.start_button_frame = Frame(self.main_container, bg="white")
            self.start_button_frame.pack(side=LEFT, pady=(10,10))

            if self.current_state == 0:
                self.start_button = Label(self.start_button_frame, bg="white",
                    image=self.start_button_pause)
                self.start_button.bind("<Button-1>", self.activate)
                self.start_button.pack(side=TOP)
                self.start_button_label = Label(self.start_button_frame,
                    bg="white", text=self.state[0], font=self.root.myFont)
                self.start_button_label.pack(side=BOTTOM)
            else:
                self.start_button.config(image=self.start_button_active)

            # Frame para las imagenes de los menus
            self.visual_menus_frame = Frame(self.main_container, bg="white")
            self.visual_menus_frame.pack(side=RIGHT)

            self.conf_icon = PhotoImage(file="images//conf.png")
            self.diag_icon = PhotoImage(file="images//diag.png").subsample(6)
            self.log_icon = PhotoImage(file="images//log.png").subsample(6)

            self.visual_menus_list = (
                (self.funcs[1], self.conf_icon, self.conf_menu),
                (self.funcs[2], self.diag_icon, self.diag_menu),
                (self.funcs[3], self.log_icon, self.log_menu)
            )

            for text, image, func in self.visual_menus_list:
                self.visual_menus(text, image, func)

        elif menu == "Config":
            pass
        elif menu == "DIAG":
            pass
        elif menu == "LOG":
            pass

    def conf_menu(self):
        pass

    def diag_menu(self):
        pass

    def log_menu(self):
        pass

    def visual_menus(self, text, image, func):
        frame_button = Frame(self.visual_menus_frame, bg="white")
        frame_button.pack(side=TOP)
        button = Label(frame_button, bg="white",
            image=image)
        button.bind("<Button-1>", func)
        button.pack(side=TOP)
        button_label = Label(frame_button, bg="white",
            text=text)
        button_label.pack(side=BOTTOM)

    def activate(self, event):
        if self.current_state == 0:
            self.current_state = 1
        else:
            self.current_state = 0

        self.create_widgets(self.current_menu)

    def menu_button_principal(self, text):
        self.menu_buttons.append(Button(self.menu, fg="white", width=19,
            bg=self.root.color, font=self.root.myFont, text=text).pack(
            fill=BOTH, side=LEFT, expand=YES))

    def menu_button(self, text):
        pass

    def cambiar_sesion(self):
        self.grid_forget()
        self.root.sesion = ""
        Inicio(self.root).tkraise()

Interfaz().mainloop()
