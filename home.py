from tkinter import *
import inicio

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
                            font=("Verdana", 22), anchor=S)
        self.version.grid(column=0, row=1)
        # Logo de la empresa
        self.logo_file = PhotoImage(file="/home/pi/Desktop/Interfaz-Sanosil/images/logo.png").subsample(2)
        # Widget del logo
        self.logo = Label(self, bg="white", image=self.logo_file)
        self.logo.image = self.logo_file  # Keep the reference
        self.logo.grid(column=0, row=0, padx=100, pady=150)
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
            self.grid_forget()
            self.version.grid_forget()
            #----------------------------------
            # Se añade un nuevo elemento al frame
            self.welcome.grid(column=0, row=0, padx=200, pady=180)
            # Se inicia la animación dos
            self.after(1000, self.animacion_dos)
# -----------------------------------------------------------------------------

# -------------------- Animación dos ------------------------------------------
    def animacion_dos(self):
        self.grid(column=0, row=0)
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
        if self.count < 8:
            self.welcome.config(fg=self.colores[self.count])
            self.count = self.count + 1
            if self.count == 8:
                    self.welcome.grid_forget()
            self.after(100, self.animacion_tres)
        else:
            self.grid_forget()
            inicio.Inicio(self.root).tkraise()
# -----------------------------------------------------------------------------

# --------------------- Termina la ventana home -------------------------------
