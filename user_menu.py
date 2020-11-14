from tkinter import *
import teclado

class User_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.root_frame.current_user = 0
        self.root.user_menu = self
        self.create_widgets()

    def create_widgets(self):
        self.container = Frame(self.root_frame, bg="white")
        self.container.pack(side=TOP, expand=YES, fill=BOTH, anchor=NW)        
        # imágenes usadas en ésta ventana
        self.images = {
            "admin": PhotoImage(file=self.root.path+"Admin.png").subsample(4),
            "operador": PhotoImage(file=self.root.path+"User.png").subsample(4),
            "service": PhotoImage(file=self.root.path+"Service.png").subsample(4),
            "derecha": PhotoImage(file=self.root.path+"der.png").subsample(6),
            "izquierda": PhotoImage(file=self.root.path+"izq.png").subsample(6)
            }
        self.user_images = [self.images["admin"], self.images["operador"],
                            self.images["operador"], self.images["operador"],
                            self.images["service"]]
        # Primera fila de la ventana llamada row a
        self.rowa = Frame(self.container, bg="white")
        self.rowa.grid(column=0, row=0, sticky=NW)
        # Botón de volver
        self.btn_volver = Button(self.rowa, bg="lightgray", text="VOLVER",
            font=self.root.myFont,
            command=lambda:self.root_frame.switch_menu("CONF"))
        self.btn_volver.pack(side=LEFT, padx=20)
        # Frame para título de la ventana
        self.frm_title = Frame(self.rowa, bg="white", relief=RIDGE,
            bd=5)
        self.frm_title.pack(pady=20, padx=40)
        # Título de la ventana en una label
        self.title = Label(self.frm_title, bg="white",
            font=("Verdana", 15, "bold"),
            text="Cambiar nombre de usuario o contraseña")
        self.title.pack(pady=10)
        # Fila para poner flechas y los tres campos para cambiar configuraciones
        self.rowb = Frame(self.container, bg="white")
        self.rowb.grid(column=0,  row=1, sticky="nw")
        #Imagen de flecha izquierda
        self.flecha_izquierda = Label(self.rowb, bg="white",
                            image=self.images["izquierda"])
        self.flecha_izquierda.image = image=self.images["izquierda"]
        self.flecha_izquierda.pack(pady=40, padx=10, side=LEFT)
        self.flecha_izquierda.bind("<Button-1>",
                    lambda e, d=0:self.cambiar_imagen_usuario(e, d))
        # Frame para campos intermedios
        self.frm_campos_usuario = Frame(self.rowb, bg="white")
        self.frm_campos_usuario.pack(side=LEFT, padx=40)
        # Imagen del Usuario
        self.imagen_usuario_actual = Label(self.frm_campos_usuario, bg="white",
                                image=self.images["admin"])
        self.imagen_usuario_actual.image = self.images["admin"]
        self.imagen_usuario_actual.grid(column=0, row=0, pady=10)
        # Nombre del Usuario a editar
        self.nombre_usuario = Label(self.frm_campos_usuario, bg="white",
                        text=self.root.usernames[self.root_frame.current_user],
                        font=self.root.myFont)
        self.nombre_usuario.grid(column=0, row=1, pady=5)
        # Imagen de flecha derecha
        self.flecha_derecha = Label(self.rowb, bg="white",
                        image=self.images["derecha"])
        self.flecha_derecha.image = self.images["derecha"]
        self.flecha_derecha.pack(side=LEFT, pady=50)
        self.flecha_derecha.bind("<Button-1>",
                lambda e, d=1:self.cambiar_imagen_usuario(e, d))
        # Frame Opciones
        self.frame_opciones = Frame(self.frm_campos_usuario, bg="white")
        self.frame_opciones.grid(column=0, row=2, pady=20)
        # Opcion Cambiar nombre de usuario
        self.boton_cambiar_username = Button(self.frame_opciones,
                        bg="SteelBlue1", fg="white",
                        text="Cambiar nombre de usuario", font=self.root.myFont,
                        command=self.cambiar_username)
        self.boton_cambiar_username.pack(side=LEFT, padx=10, ipady=5)
        # Opcion Cambiar contraseña
        self.boton_cambiar_password = Button(self.frame_opciones,
                        bg="SteelBlue1", fg="white",
                        text="Cambiar contraseña", font=self.root.myFont,
                        command=self.cambiar_password)
        self.boton_cambiar_password.pack(side=LEFT, padx=10, ipady=5)

    def cambiar_imagen_usuario(self, event, direccion):
        if direccion:
            if(self.root_frame.current_user == 4):
                self.root_frame.current_user = 0
            else:
                self.root_frame.current_user = self.root_frame.current_user + 1
        else:
            if(not(self.root_frame.current_user)):
                self.root_frame.current_user = 4
            else:
                 self.root_frame.current_user = self.root_frame.current_user - 1
        self.imagen_usuario_actual.config(
                            image=self.user_images[self.root_frame.current_user])
        self.imagen_usuario_actual.imagen=self.user_images[self.root_frame.current_user]

        self.nombre_usuario.config(text=self.root.usernames[self.root_frame.current_user])

    def cambiar_username(self):
        self.teclado("Nuevo nombre de usuario", self.root.usernames[self.root_frame.current_user],
                "username")

    def cambiar_password(self):
        self.teclado("Nueva contraseña ",  self.root.usernames[self.root_frame.current_user],
                    "change_password")

    def teclado(self, text, titulo_teclado, opcion):
        self.root_frame.pack_forget()
        self.root.frames[2].menu_anterior = 3
        self.root.frames[2].pack(side=LEFT, expand=YES, fill=BOTH)
        self.root.frames[2].titulo.config(text=text)
        self.root.frames[2].title = titulo_teclado
        self.root.frames[2].titulo_teclado.config(text=titulo_teclado)
        self.root.frames[2].entry_pass.delete(0, END)
        self.root.frames[2].pass_try = ""
        self.root.frames[2].opcion = opcion

    def widgets_unpack(self):
        self.flecha_derecha.pack_forget()
        self.flecha_izquierda.pack_forget()
        self.frm_campos_usuario.pack_forget()
