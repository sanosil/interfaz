from tkinter import *

class Wifi_menu():
    def __init__(self, root, root_frame):
        self.root = root
        self.root_frame = root_frame

        self.create_widgets()

    def create_widgets(self):
        self.root_frame.main_container.pack(side=LEFT, expand=YES, fill=BOTH)
