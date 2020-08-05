from tkinter import *
import inicio

class Menu_principal(Frame):
    def __init__(self, root, menu):
        super().__init__(root)
        # Variables
        self.root = root
        self.mensaje = "STATUS: LISTO PARA OPERAR"
        self.current_state = 0
        self.current_menu  = menu
        self.timer = 0
        self.state = ("Normal", "Step", "Testing", "Manual")
        self.funcs = [("START/STOP", self.start_menu), ("CONF", self.conf_menu), ("DIAG", self.diag_menu), ("LOG", self.log_menu)]
        self.menu_buttons = []
        # Metodos
        self.config(bg="white")
        self.grid(column=0, row=0)

        self.create_widgets(self.current_menu)

    def create_widgets(self, menu):

        self.menu = Frame(self, bg="white")
        self.menu.grid(column=0, row=0)

        for func, command in self.funcs:
            self.menu_button_principal(func, command)

        self.main_container = Frame(self, bg="white")
        self.main_container.grid(column=0, row=1)
        # --------------------------- Menu START/STOP ------------------------
        if menu == "START/STOP":
            # ----------- Boton de inicio de secuencia -----------------------
            
            # Imagenes del boton de encendido
            self.start_button_pause = PhotoImage(
                file="images//off.png").subsample(6)
            self.start_button_active = PhotoImage(
                file="images//on.png").subsample(6)
            # Frame del botón de inicio
            self.start_button_frame = Frame(self.main_container, bg="white")
            self.start_button_frame.pack(anchor="n", side=LEFT, pady=(10,10))
            # Texto del botón de iniciado
            self.start_button_label = Label(self.start_button_frame,
                bg="white", text=self.state[0], font=self.root.myFont)
            self.start_button_label.pack(side=BOTTOM)
            # Dependiendo del estado actual del botón es la imagen que se pone
            if self.current_state == 0:
                self.start_button = Label(self.start_button_frame, bg="white",
                    image=self.start_button_pause)
                self.start_button.bind("<Button-1>", self.activate)
                self.start_button.pack(side=TOP)
            else:
                self.start_button = Label(self.start_button_frame, bg="white",
                    image=self.start_button_active)
                self.start_button.bind("<Button-1>", self.activate)
                self.start_button.pack(side=TOP)

            # -----------------------------------------------------------------

            # ----------------------- Seccion central -------------------------
            self.centro = Frame(self.main_container, bg="white", width=550)
            self.centro.pack(side=LEFT, expand=YES)
            # -----------------------------------------------------------------

            # ------------------ Menus visuales -------------------------------
            # Frame para las imagenes de los menus
            self.visual_menus_frame = Frame(self.main_container, bg="white")
            self.visual_menus_frame.pack(side=RIGHT)

            self.conf_icon = PhotoImage(file="images//conf.png")
            self.diag_icon = PhotoImage(file="images//diag.png").subsample(7)
            self.log_icon = PhotoImage(file="images//log.png").subsample(7)

            self.visual_menus_list = (
                (self.funcs[1][0], self.conf_icon, self.conf_menu),
                (self.funcs[2][0], self.diag_icon, self.diag_menu),
                (self.funcs[3][0], self.log_icon, self.log_menu)
            )

            for text, image, func in self.visual_menus_list:
                self.visual_menus(text, image, func)
            # -----------------------------------------------------------------
            # ------------------ Barra inferior -------------------------------
            self.barra_inferior = Frame(self, bg="white")
            self.barra_inferior.grid(column=0, row=2, sticky="NW")

                # ----------------- Mensaje de alertas ------------------------
            self.alertas_frame = Frame(self.barra_inferior, bg=self.root.color,
            bd=2, relief=SOLID)
            self.alertas_frame.pack()
            self.alertas_label = Label(self.alertas_frame, bg=self.root.color,
                fg="white", font=self.root.myFont, text=self.mensaje).pack(
                padx=5, pady=5)
                # -------------------------------------------------------------
            # -----------------------------------------------------------------
        # ------------------ Termina menu START/STOP --------------------------

        # --------------------------- Menu CONF -------------------------------
        elif menu == "CONF":
            pass

        # ------------------ Termina menu CONF -------------------------------
        elif menu == "DIAG":
            pass
        elif menu == "LOG":
            pass

    def clear(self, frame):
        for l in frame.grid_slaves():
            l.destroy()

    def start_menu(self, event=None):
        self.switch_menu("START/STOP")

    def conf_menu(self, event=None):
        self.switch_menu("CONF")

    def diag_menu(self, event=None):
        self.switch_menu("DIAG")

    def log_menu(self, event=None):
        self.switch_menu("LOG")

    def switch_menu(self, menu):
        self.current_menu = menu
        self.clear(self)
        self.create_widgets(self.current_menu)

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

    def activate(self, event):
        if self.current_state == 0:
            self.quit()
            # self.start_button.config(image=self.start_button_active)
            self.current_state = 1
        else:
            # self.start_button.config(image=self.start_button_pause)
            self.current_state = 0

        self.clear(self)
        self.create_widgets(self.current_menu)

    def menu_button_principal(self, text, func):
        if text == self.current_menu:
            self.menu_buttons.append(Button(self.menu, fg="white", width=18,
                bg="#60FEA3", font=self.root.myFont, text=text, relief=FLAT,
                command=func).pack(fill=BOTH, side=LEFT, expand=YES, ipady=10))
        else:
            self.menu_buttons.append(Button(self.menu, fg="white", width=18,
                bg=self.root.color, font=self.root.myFont, text=text,
                command=func).pack(fill=BOTH, side=LEFT, expand=YES, ipady=10))

    def menu_button(self, text):
        pass

    def cambiar_sesion(self):
        self.grid_forget()
        self.root.sesion = ""
        inicio.Inicio(self.root).tkraise()
