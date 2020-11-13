from tkinter import *

class Test():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame
        self.create_widgets()

    def create_widgets(self):
        botones = [("BOMBA ENTRADA", lambda ch=self.root.bomba_entrada, s=1: self.root.pin_on(ch, s)),
                ("BOMBA SALIDA", lambda: self.boton("bs")]
        for nombre_boton, comando in botones:
            pass
