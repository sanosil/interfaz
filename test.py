from tkinter import *

class Test():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.root_frame.current_menu = "TEST"
        self.create_widgets()

    def create_widgets(self):
        # Contenedor de los widgets
        self.container = Frame(self.root_frame, bg="white")
        self.container.pack(side=LEFT, expand=YES, fill=BOTH, pady=(0,20))
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
        # Frame para grid de campos
        self.frame_campos = Frame(self.frame_inputs, bg="white")
        self.frame_campos.pack(side=TOP)
        # Label de humedad
        self.label_humedad = Label(self.frame_campos, text="HUMEDAD", bg="white",
                    font=self.root.myFont)
        self.label_humedad.grid(column=0, row=0, pady=15, padx=15, sticky=W)
        # Frame para mostrar la humedad
        self.frm_valor_humedad = Frame(self.frame_campos, bg="white",
                    relief=SUNKEN, bd=3)
        self.frm_valor_humedad.grid(column=1, row=0)
        # Label valor HUMEDAD
        self.label_valor_humedad = Label(self.frm_valor_humedad, bg="white",
                    font=self.root.myFont, text=self.root.humidity_dht)
        self.label_valor_humedad.pack(side=RIGHT, padx=(10,0))
        # Label temperatura
        self.label_temperatura = Label(self.frame_campos, bg="white",
                font=self.root.myFont, text="TEMPERATURA")
        self.label_temperatura.grid(column=0, row=1, padx=15, pady=15, sticky=W)
        self.frm_valor_temperatura = Frame(self.frame_campos, bg="white",
                relief=SUNKEN, bd=3)
        self.frm_valor_temperatura.grid(column=1, row=1)
        self.label_valor_temperatura = Label(self.frm_valor_temperatura,
                bg="white", font=self.root.myFont, text=self.root.temp_dht)
        self.label_valor_temperatura.pack(side=RIGHT, padx=(10,0))
        # Flujo
        self.label_flujo = Label(self.frame_campos, bg="white",
                font=self.root.myFont, text="FLUJO")
        self.label_flujo.grid(column=0, row=2, pady=(15, 45), padx=15, sticky=W)
        self.frm_valor_flujo = Frame(self.frame_campos, bg="white",
                relief=SUNKEN, bd=3)
        self.frm_valor_flujo.grid(column=1, row=2, pady=(15, 45))
        self.label_valor_flujo = Label(self.frm_valor_flujo, bg="white",
                font=self.root.myFont, text=self.root.flujo)
        self.label_valor_flujo.pack(side=RIGHT, padx=(10,0))
        # Boton para probar el flujo
        self.boton_prueba_flujo = Button(self.frame_inputs, bg="red", fg="white",
                font=self.root.myFont, text="PROBAR FLUJO", command=self.prueba,
		activebackground="red")
        self.boton_prueba_flujo.pack(side=TOP, ipadx=15, ipady=5)
        # Frame para los outputs
        self.frame_outputs = Frame(self.container, bg="white")
        self.frame_outputs.pack(side=LEFT, fill=Y, expand=YES)
        self.frm_titulo_outputs = Frame(self.frame_outputs, bg="white",
                relief=RIDGE, bd=3)
        self.frm_titulo_outputs.pack(side=TOP, pady=15)
        self.titulo_outputs = Label(self.frm_titulo_outputs, text="OUTPUTS",
                font=self.root.myFont, bg="white")
        self.titulo_outputs.pack(padx=20, pady=10)
        self.botones = [("Sanitizador 1", lambda ch=self.root.s1:self.toogle(ch, 0), 0, self.root.s1),
            ("Sanitizador 2", lambda ch=self.root.s2:self.toogle(ch, 1), 1, self.root.s2),
            ("Bomba entrada", lambda ch=self.root.be:self.toogle(ch, 2), 2, self.root.be),
            ("Bomba salida", lambda ch=self.root.bs:self.toogle(ch, 3), 3, self.root.bs),
            ("Ventilador", lambda ch=self.root.ven:self.toogle(ch, 4), 4, self.root.ven)]
        self.buttons = []
        for nombre_boton, comando, row, ch in self.botones:
            self.boton(nombre_boton, comando, row, ch)

        self.root.after(2000, self.actualizar_valores)

    def boton(self, nombre_boton, comando, row, ch):
        if ch[1] == 1:
            self.buttons.append(Button(self.frame_outputs, bg="red", fg="white", text=nombre_boton,
                    font=self.root.myFont, command=comando, activebackground="red"))
        else:
            self.buttons.append(Button(self.frame_outputs, bg="green", fg="white", text=nombre_boton,
                    font=self.root.myFont, command=comando, activebackground="green"))
        self.buttons[row].pack(padx=100, pady=10, ipady=5, side=TOP, fill=X)

    def toogle(self, canal, boton):
        if canal[1] == 1:
            canal[1] = 0
            self.buttons[boton].config(bg="green", activebackground="green")
        else:
            canal[1] = 1
            self.buttons[boton].config(bg="red", activebackground="red")
        self.root.pin_on(canal[0], canal[1])

    def actualizar_valores(self):
        if self.root_frame.current_menu == "TEST":
            self.label_valor_humedad.config(text=self.root.humidity_dht)
            self.label_valor_temperatura.config(text=self.root.temp_dht)
            self.root.after(2000, self.actualizar_valores)

    def prueba(self):
        pass
