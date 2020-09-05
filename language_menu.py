from tkinter import *

class Language_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame

        self.create_widgets()

    def create_widgets(self):
        self.flags = (
            ("spanish", PhotoImage(file=self.root.path+"spanish.png").subsample(2), self.spanish),
            ("english", PhotoImage(file=self.root.path+"english.png").subsample(3), self.english),
            ("french", PhotoImage(file=self.root.path+"french.png").subsample(8), self.french),
            ("german", PhotoImage(file=self.root.path+"german.png").subsample(7), self.german)
        )
        self.main_frm = Frame(self.root_frame, bg="white")
        self.main_frm.grid(column=0, row=1)

        col = 0
        row = 0
        for language, image, command in self.flags:
            self.create_frm(language, image, col, row, command)
            col = col + 1
            if col == 2:
                col = 0
                row = 1

    def create_frm(self, language, image, col, row, evento):
        frm = Frame(self.main_frm, bg="white")
        if row == 0:
            frm.grid(column=col, row=row, padx=20, pady=(80, 10))
        else:
            frm.grid(column=col, row=row, padx=20, pady=(10, 10))
        lbl_flag = Label(frm, image=image, bg="white")
        lbl_flag.image = image
        lbl_flag.bind("<Button-1>", evento)
        lbl_flag.pack()
