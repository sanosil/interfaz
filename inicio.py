from tkinter import *
import teclado

#---------------------- Ventana de inicio -------------------------------------
class Inicio(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(bg="white")
        self.root = root
        self.usuario = "Admin"
        self.grid(column=0, row=0)
        self.user_container = Frame(self, bg="white")
        self.user_container.grid(column=0, row=0)
        self.user_images = {
            "admin": PhotoImage(file="images//Admin.png").subsample(4),
            "service": PhotoImage(file="images//Service.png").subsample(4),
            "user": PhotoImage(file="images//User.png").subsample(4)
        }
        self.sel_label = Label(self.user_container, bg="white",
                    font=("Verdana", 18, "bold"), text="Seleccione\nusuario")
        self.sel_label.grid(column=1, row=0, padx=(100, 100), pady=(50, 100))

        # Usuario Administrador
        self.frame_admin = Frame(self.user_container, bg="white", takefocus=1,
                        highlightthickness=2, highlightcolor=root.color,
                        highlightbackground="white")
        self.frame_admin.focus_set()
        self.admin = Label(self.frame_admin, bg="white",
                    image=self.user_images["admin"])
        self.admin.bind("<Button-1>",
                    lambda e, f=self.frame_admin, u=root.usernames[0]:
                    self.evento(e, f, u))
        self.admin_label = Label(self.frame_admin, bg="white",
                    font=self.root.myFont, text=root.usernames[0])
        self.frame_admin.grid(column=0, row=0)
        self.admin.grid(column=0, row=0)
        self.admin_label.grid(column=0, row=1)
        # Usuario de servicio
        self.frame_service = Frame(self.user_container, bg="white", takefocus=1,
                            highlightthickness=2, highlightcolor=root.color,
                            highlightbackground="white")
        self.service = Label(self.frame_service, bg="white",
                        image=self.user_images["service"])
        self.service_label = Label(self.frame_service, bg="white",
                        font=self.root.myFont, text=root.usernames[1])
        self.frame_service.grid(column=2, row=0)
        self.service.grid(column=0, row=0)
        self.service.bind("<Button-1>",
                    lambda e, f=self.frame_service, u=root.usernames[1]:
                    self.evento(e, f, u))
        self.service_label.grid(column=0, row=1)
        # Operadores
        self.frame_operador = []
        self.labels_operador = []
        self.operador = []
        for i in range(3):
            self.frame_operador.append(Frame(self.user_container, bg="white",
                takefocus=1, highlightcolor=root.color, highlightthickness=2,
                highlightbackground="white"))
            self.operador.append(Label(self.frame_operador[i], bg="white",
                            image=self.user_images["user"]))
            self.labels_operador.append(Label(self.frame_operador[i],
                        bg="white", font=self.root.myFont, text=root.usernames[i+2]))
            if i == 0:
                self.frame_operador[i].grid(column=i, row=1, padx=(70, 0))
            else:
                self.frame_operador[i].grid(column=i, row=1)
            self.operador[i].grid(column=0, row=0)
            self.operador[i].bind("<Button-1>",
                        lambda e, f=self.frame_operador[i], u=root.usernames[i+2]:
                        self.evento(e, f, u))
            self.labels_operador[i].grid(column=0, row=1)


        # Contenedor de la contraseña
        self.container_pass = Frame(self, bg="white")
        self.container_pass.grid(column=0, row=1, padx=(30,0), pady=(30, 0))
        self.pass_label = Label(self.container_pass, bg="white",
                        font=self.root.myFont, text="Contraseña:")
        self.pass_label.grid(column=0, row=0, padx=(0, 30))
        self.password = Entry(self.container_pass, fg="gray",
            font=self.root.myFont, width=60)
        self.password.insert(0, "Escriba la contraseña de %s" % self.usuario)
        self.password.bind("<Button-1>", self.teclado)
        self.password.grid(column=1, row=0)

    def evento(self, event, frame, user):
        self.usuario = user
        self.password.delete(0, 100)
        self.password.insert(0, "Escriba la contraseña de %s" % self.usuario)
        frame.focus_set()

    def teclado(self, event):
        self.grid_forget()
        teclado.Teclado(self.root, self.usuario).tkraise()
# --------------------- Termina ventana de inicio -----------------------------
