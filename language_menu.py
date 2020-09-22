from tkinter import *

class Language_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.new_language = ""

        self.create_widgets()

    def create_widgets(self):
        self.main_frm = Frame(self.root_frame, bg="white")
        self.main_frm.grid(column=0, row=1, sticky=W)

        self.rowa = Frame(self.main_frm, bg="white")
        self.rowa.grid(column=0, row=0, sticky=W)

        self.rowb = Frame(self.main_frm, bg="white")
        self.rowb.grid(column=0, row=1, padx=(200, 0))

        self.rowc = Frame(self.main_frm, bg="white")
        self.rowc.grid(column=0, row=2, padx=(150,0))

        self.lbl_idioma = Label(self.rowc, bg="white", font=self.root.myFont, text="NUEVO IDIOMA")
        self.lbl_idioma.pack(side=LEFT, padx=10)
        self.new_entry = Entry(self.rowc, font=("Verdana", 25), bd=3, width=6)
        self.new_entry.pack(side=LEFT, ipadx=5, ipady=3, padx=10)
        self.btn_confirmar = Button(self.rowc, text="CONFIRMAR", fg="white",
            font=self.root.myFont, bg=self.root.color, command=lambda:
            self.confirmar())
        self.btn_confirmar.pack(side=LEFT)

        self.btn_volver = Button(self.rowa, bg="lightgray", text="VOLVER",
            font=self.root.myFont, command=lambda:self.root_frame.switch_menu("CONF"))
        self.btn_volver.pack(side=LEFT, padx=(20, 150))

        self.frame_titulo = Frame(self.rowa, bg="white", bd=3, relief=RIDGE)
        self.label_titulo = Label(self.frame_titulo, text="IDIOMA",
            font=("Verdana", 15, "bold"), bg="white")
        self.label_titulo.pack(side=LEFT, padx=70)
        self.frame_titulo.pack(pady=20)

        self.flags = (
            ("spanish", PhotoImage(file=self.root.path+"spanish.png").subsample(2)),
            ("english", PhotoImage(file=self.root.path+"english.png").subsample(3)),
            ("french", PhotoImage(file=self.root.path+"french.png").subsample(8)),
            ("german", PhotoImage(file=self.root.path+"german.png").subsample(7))
            )

        col = 0
        row = 0
        for language, image in self.flags:
            self.create_frm(language, image, col, row)
            col = col + 1
            if col == 2:
                col = 0
                row = 1

    def create_frm(self, language, image, col, row):
        frm = Frame(self.rowb, bg="white", highlightthickness=2,
            highlightcolor=self.root.color, highlightbackground="white",
            takefocus=1)        
        if language == self.root.language:
            frm.focus_set()
            self.new_entry.insert(0, language.capitalize())

        if row == 0:
            frm.grid(column=col, row=row, padx=20, pady=(30, 10))
        else:
            frm.grid(column=col, row=row, padx=20, pady=(10, 30))
        lbl_flag = Label(frm, image=image, bg="white")
        lbl_flag.image = image
        lbl_flag.bind("<Button-1>", lambda e, f=frm, l=language: self.evento(e, f, l))
        lbl_flag.pack()

    def evento(self, event, frm, language):
        frm.focus_set()
        self.new_language = language
        self.new_entry.delete(0, END)
        self.new_entry.insert(0, language.capitalize())

    def confirmar(self):
        self.root.language = self.new_language
        self.root.database.execute("UPDATE user_settings SET " \
            f"language='{self.root.language}' WHERE username = '{self.root.sesion}';")
        self.root.database.commit()
        self.root_frame.switch_menu("START/STOP")
