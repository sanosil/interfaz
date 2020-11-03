from tkinter import *
#import menu_principal, inicio

# ---------------------- Teclado númerico password ----------------------------
class Teclado(Frame):
    def __init__(self, root, titulo=None, titulo_teclado=None, opcion=None):
        super().__init__(root)
        self.root = root  # Ventana principal
        self.color = "ivory3"
        self.title = titulo
        self.config(bg="white")  # Fondo del frame del teclado
        self.pass_try = ""
        self.grid(column=0, row=0)  # Se pone el teclado en pantalla
        self.myFont = ("Verdana", 22)  # Fuente de letra
        self.contenedor = Frame(self, bg="white")  # color de fondo contenedor
        self.contenedor.grid(column=0, row=0, padx=(3,0))  # Se pone en fame teclado

        # Frame de espacio
        self.espacio_2 = Frame(self.contenedor, height=70, bg="white")
        self.espacio_2.pack(side=TOP, expand=YES, fill=BOTH)

        self.titulo_teclado = Label(self.espacio_2, bg="white", font=("Verdana", 25), text=titulo_teclado)
        self.titulo_teclado.pack()
        self.titulo_teclado.bind("<Button-1>", self.salir)

        # First row of buttons
        self.rowa = Frame(self.contenedor, bg="white")
        self.rowa.pack(side=TOP, expand=YES, fill=BOTH)

        # Boton regresar
        self.volver = Button(self.rowa, text="Regresar",
                font=self.myFont, activebackground="white", bg="gray",
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
        self.del_tecla = Button(self.rowa, background="yellow", text = "DEL",
            font=self.myFont, command=self.borrar)
        self.del_tecla.pack(side=RIGHT, expand=YES, fill=BOTH)
        # --------------------------------------------------------------------

        # Frame de contraseña correcta o incorrecta
        self.espacio = Frame(self.contenedor, height=59, relief=RIDGE, bd=3, bg="black")
        self.espacio.pack(side=TOP, expand=YES, fill=BOTH)

        self.mensaje = Label(self.espacio, text="Contraseña incorrecta",
            bg="red", font=("Verdana", 31))
        # ----------------

        self.teclas = (
                ("Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"),
               ("A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ"),
                ("Z", "X", "C", "V", "B", "N", "M", "Enter")
        )
        self.width = 2
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

        self.boton = Button(self.rowd, bg=self.color, text="     ")
        self.boton2 = Button(self.rowd, bg=self.color, text="     ")
        self.space_bar = Button(self.rowd, text="Espacio", font=self.myFont,
                bg=self.color, command=self.space)
        self.boton.pack(side=LEFT, expand=YES, fill=BOTH)
        self.space_bar.pack(side=LEFT, expand=YES, fill=BOTH)
        self.boton2.pack(side=RIGHT, expand=YES, fill=BOTH)

    def space(self):
        self.pass_try = self.pass_try + " "
        self.entry_pass.insert(END, " ")

    def volver(self):
        self.grid_forget()
        inicio.Inicio(self.root).tkraise()

    def tecla(self, cont, contenedor, width=4):
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
            self.after(50, self.acceso)
        else:
            self.espacio.config(bg="red")
            self.mensaje.pack(expand=YES, fill=BOTH)
            self.after(1000, self.normal)

    def normal(self):
        self.espacio.config(bg="black")
        self.mensaje.pack_forget()

    def acceso(self):
        self.grid_forget()
        menu_principal.Menu_principal(self.root, "START/STOP").tkraise()

    def salir(self, event=None):
        if self.title == "SERVICE":
            self.root.destroy()
# ---------------- Termina ventana de teclado numérico ------------------------
