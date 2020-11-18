from tkinter import *
import programas, teclado_numerico

class Start_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.root.start_menu = self
        # ----------- Boton de inicio de secuencia y timer --------------------
        self.frame_timer_y_encendido = Frame(root_frame.main_container,
            bg="white")
        self.frame_timer_y_encendido.pack(anchor="n", side=LEFT, padx=10, pady=10)
        # Imagenes del boton de encendido
        self.start_button_pause = PhotoImage(
            file=self.root.path+"off.png").subsample(6)
        self.start_button_active = PhotoImage(
            file=self.root.path+"on.png").subsample(6)
        # Frame del botón de inicio
        self.start_button_frame = Frame(self.frame_timer_y_encendido,
            bg="white")
        self.start_button_frame.pack(anchor="w", side=TOP, pady=(10,80))
        # Texto del botón de iniciado
        self.start_button_label = Label(self.start_button_frame,
            bg="white", fg=self.root.color,
            text=self.root_frame.current_program,
            font=("Verdana", 12, "bold"))
        self.start_button_label.pack(side=BOTTOM)
        # Dependiendo del estado actual del botón es la imagen que se pone
        if self.root.current_button_state == 0:
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
        self.timer_image = PhotoImage(file=self.root.path+"timer.png").subsample(7)
        self.timer_off_image = PhotoImage(file=self.root.path+"timer_off.png").subsample(7)
        self.timerFrame = Frame(self.frame_timer_y_encendido,
            bg="white")
        self.timerFrame.pack(side=BOTTOM)
        self.timer_icon = Label(self.timerFrame, bg="white",
            image=self.timer_image)
        self.timer_icon.grid(column=0, row=0)
        # self.timer_icon.bind("<Button-1>", self.activate_timer)
        self.timer_icon.bind("<Button-1>", self.root_frame.quit)
        self.timer_label = Label(self.timerFrame, bg="white",
            font=("Verdana", 12, "bold"))
        self.timer_label.grid(column=0, row=1)
        if self.root.timer == 0:
            self.timer_label.config(text="Timer off", fg="red")
        else:
            self.timer_label.config(text="Timer on", fg="#2ECC71")
        # -----------------------------------------------------------------

        # ----------------------- Seccion central -------------------------
        self.centro = Frame(root_frame.main_container, bg="white", width=480)
        self.centro.pack(side=LEFT, expand=YES)
        # -----------------------------------------------------------------

        # ------------------ Menus visuales -------------------------------
        # Frame para las imagenes de los menus
        self.visual_menus_frame = Frame(root_frame.main_container, bg="white")
        self.visual_menus_frame.pack(side=RIGHT, padx=10)

        self.conf_icon = PhotoImage(file=self.root.path+"conf.png")
        self.diag_icon = PhotoImage(file=self.root.path+"diag.png").subsample(7)
        self.log_icon = PhotoImage(file=self.root.path+"log.png").subsample(7)

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
        self.barra_inferior.pack(side=BOTTOM, expand=YES, fill=BOTH)

            # ************* Mensaje de alertas ***************************
        self.alertas_frame = Frame(self.barra_inferior, bg=self.root.color_alertas,
        bd=2, relief=SOLID)
        self.alertas_frame.pack(side=TOP, anchor="w", expand=YES, fill=BOTH)
        self.alertas_label = Label(self.alertas_frame, bg=self.root.color_alertas,
            fg="white", font=self.root.myFont, text=self.root.mensaje)
        self.alertas_label.pack(side=LEFT, padx=(20, 20), pady=5)
        if self.root.program_object != None:
            self.root.program_object.set_previous_frame(self)
            # ************************************************************
            # ************* Volumen a sanitizar *************************
        self.volumen_frame = Frame(self.barra_inferior, bd=2, bg="gray",
            relief=SOLID)
        self.volumen_frame.pack(side=LEFT, anchor="w")
        self.volumen_label = Label(self.volumen_frame, bg="gray", fg="white",
            font=self.root.myFont, text="Volumen: %d m3" % self.root.vol)
        self.volumen_label.pack(padx=25-(len(str(self.root.vol))*5), pady=10)
        self.volumen_label.bind("<Button-1>", self.set_volumen)
            # ***********************************************************
            # ************* Sesión **************************************
        self.sesion_frame = Frame(self.barra_inferior, bd=2, bg="gray",
            relief=SOLID)
        self.sesion_frame.pack(side=LEFT, expand=YES, fill=BOTH)
        self.sesion = Label(self.sesion_frame, bg="gray", fg="white",
            font=self.root.myFont, text=self.root.sesion).pack(side=LEFT,
            padx=(30, 200), pady=10)
        self.tiempo_a_sanitizar = Label(self.sesion_frame, bg="gray",
            fg="white", font=self.root.myFont,
            text="Tiempo: %d s" % self.root.time)
        self.tiempo_a_sanitizar.pack(side=RIGHT, padx=(15,10))
            # ***********************************************************
            # *********** Cerrar sesión *********************************
        self.boton_cerrar_sesion = Button(self.barra_inferior, fg="white",
            bg="red", bd=2, relief=SOLID, font=self.root.myFont,
            text="Cerrar sesión", command=lambda: self.confirmacion(
            "Seguro que desea cerrar sesión", lambda: self.root_frame.cambiar_sesion()))
        self.boton_cerrar_sesion.pack(side=LEFT, expand=YES, fill=BOTH)
            # ***********************************************************

        # -----------------------------------------------------------------
    # --------------------------- Funciones --------------------------------
    def actualizar_valores(self, color):
        self.alertas_label.config(text=self.root.mensaje, bg=color)
        self.alertas_frame.config(bg=color)
        if self.root.current_button_state == 0:
            self.start_button_label.config(fg="red")
            self.start_button.config(image=self.start_button_pause)
            self.start_button["image"] = self.start_button_pause
        else:
            self.start_button.config(image=self.start_button_active)
            self.start_button["image"] = self.start_button_active

    def visual_menus(self, text, image, func):
        frame_button = Frame(self.visual_menus_frame, bg="white")
        frame_button.pack(side=TOP, pady=8)
        button = Label(frame_button, bg="white",
            image=image)
        button.bind("<Button-1>", func)
        button.pack(side=TOP)
        button_label = Label(frame_button, bg="white",
            text=text)
        button_label.pack(side=BOTTOM)

    def activate(self, event=None):
        # self.root.destroy()
        if self.root.current_button_state == 0 and self.root.program_object == None:
            self.start_button.config(image=self.start_button_active)
            self.start_button_label.config(fg=self.root.color)
            self.root.current_button_state = 1
            self.root.program_object = programas.Programas(self.root,
                self.root_frame, self,
                self.root_frame.current_program)
            self.alertas_label.config(text=self.root.mensaje)

        else:
            self.confirmacion("Seguro que desea abortar el programa", lambda: self.si())

    def confirmacion(self, text, command=None):
        self.frame_confirmacion = Frame(self.root, bg="white", bd=3, relief=RIDGE)
        self.root_frame.pack_forget()
        self.frame_confirmacion.pack(side=LEFT, padx=(150,0))
        self.confirmacion_label = Label(self.frame_confirmacion, bg="white",
            font=("Verdana", 18), text=text)
        self.confirmacion_label.pack(side=TOP, padx=50, pady=(80, 20))
        self.frame_botones = Frame(self.frame_confirmacion, bg="white")
        self.frame_botones.pack(side=BOTTOM, pady=20)
        self.button_yes = Button(self.frame_botones, text="Sí", fg="white",
            bg="red", font=("Verdana", 18), command=command)
        self.button_yes.grid(column=0, row=0, padx=20, ipadx=20, ipady=20)
        self.button_no = Button(self.frame_botones, text="No", fg="white",
            bg=self.root.color, font=("Verdana", 18), command=self.no)
        self.button_no.grid(column=1, row=0, padx=20, ipadx=20, ipady=20)

    def si(self):
        self.root_frame.clear(self.root)
        self.root.color_alertas = "green"
        self.root.current_button_state = 0
        self.root_frame.__init__(self.root, self.root_frame.current_menu)

    def no(self):
        self.frame_confirmacion.pack_forget()
        self.root.frames[3].pack(side=LEFT, expand=YES, fill=BOTH)

    def activate_timer(self, event=None):
        if self.root.timer == 0:
            self.root.timer = 1
            self.root_frame.timer = self.root.timer
            self.timer_label.config(fg=self.root.color, text="Timer on")
        else:
            self.root.timer = 0
            self.root_frame.timer = 0
            self.timer_label.config(fg="red", text="Timer off")

        self.root.database.execute("UPDATE user_settings SET " \
            f"timer = {self.root.timer} WHERE username = '{self.root.sesion}'")
        self.root.database.commit()

    def set_volumen(self, event):
        self.root_frame.pack_forget()
        teclado_numerico.Teclado(self.root, "Nuevo volumen", self.root_frame)

# ------------------ Termina menu START/STOP --------------------------
