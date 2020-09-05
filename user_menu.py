from tkinter import *

class User_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame

        self.create_widgets()

    def create_widgets(self):
        self.main_container = Frame(self.root_frame, bg="white")
        self.main_container.grid(column=0, row=1, sticky=W)
        path = "images/"
        # self.path="/home/pi/Desktop/Interfaz-Sanosil/images/"

        self.images = {
            "admin": PhotoImage(file=path+"Admin.png").subsample(8),
            "operador": PhotoImage(file=path+"User.png").subsample(8),
            "service": PhotoImage(file=path+"Service.png").subsample(8)
            }

        for i in range(5):
            row = Frame(self.main_container, bg="white")
            row.grid(column=0, row=i, sticky=W)
            if i == 0:
                self.field(row, self.images["admin"], self.root.usernames[i])
            elif i < 4:
                self.field(row, self.images["operador"], self.root.usernames[i])
            else:
                self.field(row, self.images["service"], self.root.usernames[i])

    def field(self, row, image, username):

        frm = Frame(row, bg="white", bd=3, relief=SUNKEN)
        frm.pack(padx=(50, 20), pady=5, side=LEFT)
        lbl = Label(frm, image=image, bg="white")
        lbl.image = image
        lbl.pack(side=LEFT)

        frame_labels = Frame(row, bg="white")
        frame_labels.pack(side=LEFT, padx=(0, 40))
        lbl_user = Label(frame_labels, text=username, font=self.root.myFont,
            bg="white")
        lbl_user.grid(column=0, row=0, sticky=W)
        lbl_psw = Label(frame_labels, text="password", font=self.root.myFont,
            bg="white")
        lbl_psw.grid(column=0, row=1, sticky=W)

        frm_entry = Frame(row, bg="white")
        frm_entry.pack(side=LEFT)
        if username != "ADMIN":
            entry_username = Entry(frm_entry, bd=3, width=40, font=self.root.myFont, fg="gray")
            entry_username.insert(0, "Nuevo username")
            entry_username.grid(column=0, row=0, sticky=W)
        else:
            space = Label(frm_entry, bg="white")
            space.grid(column=0, row=0, sticky=W)
        entry_psw = Entry(frm_entry, bd=3, width=40, font=self.root.myFont, fg="gray")
        entry_psw.insert(0, "Nueva contraseña")
        entry_psw.grid(column=0, row=1, sticky=W)
