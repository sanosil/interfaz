from tkinter import *

class Start_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame

        # ----------- Boton de inicio de secuencia y timer --------------------
        self.frame_timer_y_encendido = Frame(root_frame.main_container,
            bg="white")
        self.frame_timer_y_encendido.pack(anchor="n", side=LEFT, padx=10, pady=10)
        # Imagenes del boton de encendido
        self.start_button_pause = PhotoImage(
            file="images//off.png").subsample(6)
        self.start_button_active = PhotoImage(
            file="images//on.png").subsample(6)
        # Frame del botón de inicio
        self.start_button_frame = Frame(self.frame_timer_y_encendido,
            bg="white")
        self.start_button_frame.pack(anchor="w", side=TOP, pady=(10,80))
        # Texto del botón de iniciado
        self.start_button_label = Label(self.start_button_frame,
            bg="white", fg=self.root.color, text=root_frame.state[3],
            font=self.root.myFont)
        self.start_button_label.pack(side=BOTTOM)
        # Dependiendo del estado actual del botón es la imagen que se pone
        if root_frame.current_state == 0:
            self.start_button_label.config(fg="red")
            self.start_button = Label(self.start_button_frame, bg="white",
                image=self.start_button_pause)
            self.start_button.bind("<Button-1>", self.activate)
            self.start_button.pack(side=TOP)
        else:
            self.start_button = Label(self.start_button_frame, bg="white",
                image=self.start_button_active)
            self.start_button.bind("<Button-1>", self.activate)
            self.start_button.pack(side=TOP)

        # ----------------------- timer -----------------------------------
        # imagen
        self.timer_image = PhotoImage(file="images//timer.png").subsample(7)
        self.timerFrame = Frame(self.frame_timer_y_encendido,
            bg="white")
        self.timerFrame.pack(side=BOTTOM)
        self.timer_icon = Label(self.timerFrame, bg="white",
            image=self.timer_image).pack(side=TOP)
        self.timer_label = Label(self.timerFrame, bg="white",
            font=self.root.myFont)
        self.timer_label.pack(side=BOTTOM)
        if self.root_frame.timer == 0:
            self.timer_label.config(text="Timer off", fg="red")
        else:
            self.timer_label.config(text="Timer on", fg="#2ECC71")
        # -----------------------------------------------------------------

        # ----------------------- Seccion central -------------------------
        self.centro = Frame(root_frame.main_container, bg="white", width=560)
        self.centro.pack(side=LEFT, expand=YES)
        # -----------------------------------------------------------------

        # ------------------ Menus visuales -------------------------------
        # Frame para las imagenes de los menus
        self.visual_menus_frame = Frame(root_frame.main_container, bg="white")
        self.visual_menus_frame.pack(side=RIGHT)

        self.conf_icon = PhotoImage(file="images//conf.png")
        self.diag_icon = PhotoImage(file="images//diag.png").subsample(7)
        self.log_icon = PhotoImage(file="images//log.png").subsample(7)

        self.visual_menus_list = (
            (root_frame.funcs[1][0], self.conf_icon, root_frame.conf_menu),
            (root_frame.funcs[2][0], self.diag_icon, root_frame.diag_menu),
            (root_frame.funcs[3][0], self.log_icon, root_frame.log_menu)
        )

        for text, image, func in self.visual_menus_list:
            self.visual_menus(text, image, func)
        # -----------------------------------------------------------------

        # ------------------ Barra inferior -------------------------------
        self.barra_inferior = Frame(root_frame, bg="white")
        self.barra_inferior.grid(column=0, row=2, sticky="NW")

            # ************* Mensaje de alertas ***************************
        self.alertas_frame = Frame(self.barra_inferior, bg=self.root.color,
        bd=2, relief=SOLID)
        self.alertas_frame.pack(side=TOP, anchor="w")
        self.alertas_label = Label(self.alertas_frame, bg=self.root.color,
            fg="white", font=self.root.myFont, text=self.root_frame.mensaje)
        self.alertas_label.pack(padx=(5, 400), pady=10)
            # ************************************************************
            # ************* Volumen a sanitizar *************************
        self.volumen_frame = Frame(self.barra_inferior, bd=2, bg="gray",
            relief=SOLID)
        self.volumen_frame.pack(side=LEFT, anchor="w")
        self.volumen_label = Label(self.volumen_frame, bg="gray", fg="white",
            font=self.root.myFont, text="Volumen: %d m3" % self.root_frame.vol)
        self.volumen_label.pack(padx=30, pady=10)
            # ***********************************************************
            # ************* Sesión **************************************
        self.sesion_frame = Frame(self.barra_inferior, bd=2, bg="gray",
            relief=SOLID)
        self.sesion_frame.pack(side=LEFT)
        self.sesion = Label(self.sesion_frame, bg="gray", fg="white",
            font=self.root.myFont, text=self.root.sesion).pack(side=LEFT,
            padx=(30, 200), pady=10)
        self.tiempo_a_sanitizar = Label(self.sesion_frame, bg="gray",
            fg="white", font=self.root.myFont,
            text="Tiempo: %d s" % self.root_frame.tiempo_sanitizacion)
        self.tiempo_a_sanitizar.pack(side=RIGHT, padx=(40,10))
            # ***********************************************************
            # *********** Cerrar sesión *********************************
        self.boton_cerrar_sesion = Button(self.barra_inferior, fg="white",
            bg="red", bd=2, relief=SOLID, font=self.root.myFont,
            text="Cerrar sesión", command=self.root_frame.cambiar_sesion)
        self.boton_cerrar_sesion.pack(side=BOTTOM, ipady=8, ipadx=4)
            # ***********************************************************

        # -----------------------------------------------------------------
    # --------------------------- Funciones --------------------------------
    def visual_menus(self, text, image, func):
        frame_button = Frame(self.visual_menus_frame, bg="white")
        frame_button.pack(side=TOP, pady=10)
        button = Label(frame_button, bg="white",
            image=image)
        button.bind("<Button-1>", func)
        button.pack(side=TOP)
        button_label = Label(frame_button, bg="white",
            text=text)
        button_label.pack(side=BOTTOM)

    def activate(self, event=None):
        # self.root.destroy()
        if self.root_frame.current_state == 0:
            self.start_button.config(image=self.start_button_active)
            self.start_button_label.config(fg=self.root.color)
            self.root_frame.current_state = 1
            self.root_frame.mensaje = "STATUS: OPERANDO"
            self.alertas_label.config(text=self.root_frame.mensaje)
            # self.root.pin_on(self.root.ch3, 0)
        else:
            self.start_button.config(image=self.start_button_pause)
            self.start_button_label.config(fg="red")
            self.root_frame.current_state = 0
            self.root_frame.mensaje = "STATUS: LISTO PARA OPERAR"
            self.alertas_label.config(text=self.root_frame.mensaje)
            # self.root.pin_on(self.root.ch3, 1)

# ------------------ Termina menu START/STOP --------------------------
