from tkinter import *

class Test():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.create_widgets()

    def create_widgets(self):
        # Contenedor de los widgets
        self.container = Frame(self.root_frame, bg="white")
        self.container.pack(side=LEFT, expand=YES, fill=BOTH)
        # Frame para las inputs
        self.frame_inputs = Frame(self.container, bg="white")
        self.frame_inputs.pack(side=LEFT, expand=YES, fill=BOTH, padx=20)
        # Label del título de inputs
        self.frm_titulo_inputs = Frame(self.frame_inputs, bg="white",
                relief=RIDGE, bd=3)
        self.frm_titulo_inputs.pack(side=TOP, pady=15)
        self.titulo_inputs = Label(self.frm_titulo_inputs, text="INPUTS",
                font=self.root.myFont, bg="white")
        self.titulo_inputs.pack(padx=20, pady=10)
        # Label de humedad
        self.frm_humedad_LyV = Frame(self.frame_inputs, bg="white")
        self.frm_humedad_LyV.pack(side=TOP, pady=15)
        self.humedad = Label(self.frm_humedad_LyV, text="HUMEDAD", bg="white",
                    font=self.root.myFont)
        self.humedad.pack(side=LEFT, fill=X, padx=15)
        # Frame para mostrar la humedad
        self.frm_valor_humedad = Frame(self.frm_humedad_LyV, bg="white",
                    relief=SUNKEN, bd=3)
        self.frm_valor_humedad.pack(side=LEFT, fill=X)
        # Label valor HUMEDAD
        self.valor_humedad = Label(self.frm_valor_humedad, bg="white",
                    font=self.root.myFont, text=self.root.humidity_dht)
        self.valor_humedad.pack(side=RIGHT)
        # Frame para los outputs
        self.frame_outputs = Frame(self.container, bg="white")
        self.frame_outputs.pack(side=LEFT, fill=Y, expand=YES)
        self.frm_titulo_outputs = Frame(self.frame_outputs, bg="white",
                relief=RIDGE, bd=3)
        self.frm_titulo_outputs.pack(side=TOP, pady=15)
        self.titulo_outputs = Label(self.frm_titulo_outputs, text="OUTPUTS",
                font=self.root.myFont, bg="white")
        self.titulo_outputs.pack(padx=20, pady=10)
        self.botones = [("Sanitizador 1", lambda ch=self.root.s1:self.toogle(ch, 0), 0),
            ("Sanitizador 2", lambda ch=self.root.s2:self.toogle(ch, 1), 1),
            ("Bomba entrada", lambda ch=self.root.be:self.toogle(ch, 2), 2),
            ("Bomba salida", lambda ch=self.root.bs:self.toogle(ch, 3), 3),
            ("Ventilador", lambda ch=self.root.ven:self.toogle(ch, 4), 4)]
        self.buttons = []
        for nombre_boton, comando, row in self.botones:
            self.boton(nombre_boton, comando, row)

    def boton(self, nombre_boton, comando, row):
        self.buttons.append(Button(self.frame_outputs, bg="red", fg="white", text=nombre_boton,
                font=self.root.myFont, command=comando))
        self.buttons[row].pack(padx=100, pady=10, ipady=5, side=TOP, fill=X)

    def toogle(self, canal, boton):
        if canal[1] == 1:
            canal[1] = 0
            self.buttons[boton].config(bg="green", activebackground="green")
        else:
            canal[1] = 1
            self.buttons[boton].config(bg="red", activebackground="red")
        self.root.pin_on(canal[0], canal[1])
