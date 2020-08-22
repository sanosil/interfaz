from tkinter import *

class Programas():
	def __init__(self, root, root_frame, previous_frame, programa):
		self.root = root
		self.root_frame = root_frame
		self.program = programa
		if self.program == "Normal":
			self.normal()
		elif self.program == "Step":
			self.step()
		elif self.program == "Testing":
			self.testing()
		elif self.program == "Manual":
			self.manual()

	def normal(self):
		print("hello")

	def step(self):
		pass

	def testing(self):
		pass

	def manual(self):
		pass
