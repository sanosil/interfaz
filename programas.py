from tkinter import *

class Programas():
	def __init__(self, root, root_frame, programa):
		self.root = root
		self.root_frame = root_frame
		self.program = programa
		if self.programa == "Normal":
			self.normal()
		elif self.programa == "Step":
			self.step()
		elif self.programa == "Testing":
			self.testing()
		elif self.programa == "Manual":
			self.manual()
	def normal(self):
		pass
