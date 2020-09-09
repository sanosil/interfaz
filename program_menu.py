from tkinter import *

class Program_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame

        self.create_widgets()

    def create_widgets(self):
        self.main = Frame(self.root_frame, bg="white")
        sel.main.grid(sticky=W, column=0, row=1)

        self.frame_programa = Frame(self.main, bg=white)
