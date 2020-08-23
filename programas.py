from tkinter import *
import RPi.GPIO as GPIO

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
                self.root.ml = 0
                self.total_ml = self.root.concentracion * self.root.vol
                self.root.pin_on(self.root.bomba_entrada, 0)
                self.root.after(200, self.measure_ml)

	def step(self):
		pass

	def testing(self):
		pass

	def manual(self):
		pass

	def measure_ml(self):
                if self.root.current_button_state == 1:
                    # flujo en ml/s
                    self.flujo = ((self.root.pulsos/0.2)/98)*(1000/60)
                    print(self.flujo)
                    self.root.pulsos = 0
                    self.root.ml = self.root.ml + (self.flujo * .2)
                    if GPIO.input(self.root.flotador) == 0:
                        self.root.pin_on(self.root.bomba_entrada, 1)
                        if self.root.ml < self.total_ml:
                            self.root.after(60000, self.llenar_tanque)
                    elif self.root.ml >= self.total_ml:
                        # Fin de programa
                        self.root.pin_on(self.root.bomba_entrada, 1)
                    else:
                        # Después de 200 ms se vuelven a medir los ml
                        self.root.after(200, self.measure_ml)
                else:
                    self.root.pulses = 0
                    self.root.ml = 0
                    self.root.pin_on(self.root.bomba_entrada, 1)
                    self.root.pin_on(self.root.bomba_salida, 0)
                    self.root.after(60000, self.apagar_bomba)

	def llenar_tanque(self):
                self.root.pin_on(self.root.bomba_entrada, 0)
                self.root.after(200, self.measure_ml)

	def apagar_bomba(self):
		self.root.pin_on(self.root.bomba_salida, 1)
