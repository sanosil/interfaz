from tkinter import *

class Test():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.create_widgets()

    def create_widgets(self):
        # Contenedor de los widgets
        self.container = Frame(self.root_frame, bg="white", relief=RIDGE, bd=3)
        self.container.pack(side=LEFT, expand=YES, fill=BOTH)
        # Frame para las entradas
        self.frame_inputs = Frame(self.container, bg="white", relief=SOLID,
                    bd=3)
        self.frame_inputs.pack(side=LEFT, expand=YES, fill=BOTH)
        self.titulo_inputs = Label(self.frame_inputs, text="INPUTS", font=self.root.myFont,
                bg="white")
        self.titulo_inputs.pack(side=TOP, fill=X)
        self.humedad = Label(self.frame_inputs, text="HUMEDAD", bg="white",
                    font=self.root.myFont)
        self.humedad.pack(side=LEFT, fill=X)
        self.frame_outputs = Frame(self.container, bg="white", relief=SOLID,
                    bd=3, width=self.root.width/2)
        self.frame_outputs.pack(side=LEFT, expand=YES, fill=BOTH)
        self.titulo_outputs = Label(self.frame_outputs, text="OUTPUTS",
                font=self.root.myFont, bg="white")
        self.titulo_outputs.pack(side=TOP, fill=X)
        self.botones = [("Sanitizador 1", lambda ch=self.root.s1:self.toogle(ch), 0),
            ("Sanitizador 2", lambda ch=self.root.s2:self.toogle(ch), 1),
            ("Bomba entrada", lambda ch=self.root.be:self.toogle(ch), 2),
            ("Bomba salida", lambda ch=self.root.bs:self.toogle(ch), 3),
            ("Ventilador", lambda ch=self.root.ven:self.toogle(ch), 4)]
        self.buttons = []
        for nombre_boton, comando, row in self.botones:
            self.boton(nombre_boton, comando, row)

    def boton(self, nombre_boton, comando, row):
        self.buttons.append(Button(self.frame_outputs, bg="red", fg="white", text=nombre_boton,
                font=self.root.myFont, command=comando))
        self.buttons[row].pack(padx=200, pady=10, ipady=10, side=TOP, fill=X)

    def toogle(self, canal):
        if canal[1] == 0:
            canal[1] = 1
            self.buttons[canal[0]].config(bg="green")
        else:
            canal[1] = 0
            self.buttons[canal[0]].config(bg="red")
        self.root.pin_on(canal[0], canal[1])
