from tkinter import *

class User_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.current_user = 0

        self.create_widgets()

    def create_widgets(self):
        self.main_container = Frame(self.root_frame, bg="white")
        self.main_container.grid(column=0, row=1, sticky="nw")
        path = "images/"
        # self.path="/home/pi/Desktop/Interfaz-Sanosil/images/"
        # imágenes usadas en ésta ventana
        self.images = {
            "admin": PhotoImage(file=path+"Admin.png").subsample(4),
            "operador": PhotoImage(file=path+"User.png").subsample(4),
            "service": PhotoImage(file=path+"Service.png").subsample(4),
            "derecha": PhotoImage(file=path+"der.png").subsample(6),
            "izquierda": PhotoImage(file=path+"izq.png").subsample(6)
            }
        self.user_images = [self.images["admin"], self.images["operador"],
                            self.images["operador"], self.images["operador"],
                            self.images["service"]]
        # Primera fila de la ventana llamada row a
        self.rowa = Frame(self.main_container, bg="white")
        self.rowa.grid(column=0, row=0)
        # Frame para título de la ventana
        self.frm_title = Frame(self.rowa, bg="white", relief=RIDGE,
            bd=5)
        self.frm_title.pack(pady=40, padx=130)
        # Título de la ventana en una label
        self.title = Label(self.frm_title, bg="white",
            font=("Verdana", 15, "bold"),
            text="Cambiar nombre de usuario y contraseña")
        self.title.pack(padx=20, pady=10)
        # Fila para poner flechas y los tres campos para cambiar configuraciones
        self.rowb = Frame(self.main_container, bg="white")
        self.rowb.grid(column=0,  row=1, sticky="w")
        #Imagen de flecha izquierda
        self.flecha_izquierda = Label(self.rowb, bg="white",
                            image=self.images["izquierda"])
        self.flecha_izquierda.image = image=self.images["izquierda"]
        self.flecha_izquierda.pack(pady=50, padx=10, side=LEFT)
        self.flecha_izquierda.bind("<Button-1>", lambda e, d=0:self.cambiar_imagen_usuario(e, d))
        # Frame para campos intermedios
        self.frm_campos_usuario = Frame(self.rowb, bg="white")
        self.frm_campos_usuario.pack(side=LEFT, padx=210)
        # Imagen del Usuario
        self.imagen_usuario_actual = Label(self.frm_campos_usuario, bg="white",
                                image=self.images["admin"])
        self.imagen_usuario_actual.image = self.images["admin"]
        self.imagen_usuario_actual.grid(column=0, row=0, pady=10)
        # Imagen de flecha derecha
        self.flecha_derecha = Label(self.rowb, bg="white",
                        image=self.images["derecha"])
        self.flecha_derecha.image = self.images["derecha"]
        self.flecha_derecha.pack(side=LEFT, pady=50)
        self.flecha_derecha.bind("<Button-1>", lambda e, d=1:self.cambiar_imagen_usuario(e, d))

    def cambiar_imagen_usuario(self, event, direccion):

        if direccion:
            if(self.current_user == 4):
                self.current_user = 0
            else:
                self.current_user = self.current_user + 1
            self.imagen_usuario_actual.config(image=self.user_images[self.current_user])
            self.imagen_usuario_actual.imagen=self.user_images[self.current_user]
        else:
            if(not(self.current_user)):
                self.current_user = 4
            else:
                 self.current_user = self.current_user - 1
            self.imagen_usuario_actual.config(image=self.user_images[self.current_user])
            self.imagen_usuario_actual.imagen=self.user_images[self.current_user]
