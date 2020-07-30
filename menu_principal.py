
from tkinter import *
import inicio

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
        inicio.Inicio(self.root).tkraise()
