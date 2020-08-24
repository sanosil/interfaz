from tkinter import *
# import RPi.GPIO as GPIO

class Programas():
	def __init__(self, root, root_frame, previous_frame, programa):
		self.root = root
		self.root_frame = root_frame
		self.previous_frame = previous_frame
		self.program = programa
		if self.program == "Normal":
			self.normal()
		elif self.program == "Step":
			self.step()
		elif self.program == "Testing":
			self.testing()
		elif self.program == "Manual":
			self.manual()

	def set_previous_frame(self, previous_frame):
		self.previous_frame = previous_frame

	def normal(self):
			self.root.ml = 0
			self.tiempo_salida = 5
			self.root.color_alertas = "orange"
			self.previous_frame.alertas_frame.config(bg=self.root.color_alertas)
			self.previous_frame.alertas_label.config(bg=self.root.color_alertas)
			self.root.mensaje = "STATUS: Comenzando a operar salga de la habitación en " + str(self.tiempo_salida) + " seg"
			self.previous_frame.alertas_label.config(text=self.root.mensaje)
			if self.root.concentracion != 0 and self.root.vol != 0:
				self.total_ml = self.root.concentracion * self.root.vol
				self.root.after(1000, self.salida_start)

	def salida_start(self):
		self.tiempo_salida = self.tiempo_salida - 1
		if self.root_frame.current_menu == "START/STOP":
			self.root.mensaje = "STATUS: Comenzando a operar salga de la habitación en " + str(self.tiempo_salida) + " seg"
			self.previous_frame.alertas_label.config(text=self.root.mensaje)
		if self.tiempo_salida == 0:
			self.root.mensaje = "STATUS: OPERANDO"
			self.root.color_alertas = self.root.color
			self.previous_frame.alertas_frame.config(bg=self.root.color_alertas)
			self.previous_frame.alertas_label.config(text=self.root.mensaje,
				bg=self.root.color_alertas)
			self.root.pin_on(self.root.bomba_entrada, 0)
			self.root.after(100, self.measure_ml)
		else:
			self.root.after(1000, self.salida_start)

	def step(self):
		pass

	def testing(self):
		pass

	def manual(self):
		pass

	def measure_ml(self):
		if self.root.current_button_state == 1:
            # flujo en ml/s
			self.flujo = ((self.root.pulsos/0.1)/98)*(1000/60)
			self.root.pulsos = 0
			self.root.ml = self.root.ml + (self.flujo * .1)
			if self.root_frame.current_menu == "START/STOP":
				self.root.mensaje = "STATUS: OPERANDO " + str(self.root.ml) + " ml UTILIZADOS"
				self.previous_frame.alertas_label.config(text=self.root.mensaje)
            # if GPIO.input(self.root.flotador) == 0:
            #     self.root.pin_on(self.root.bomba_entrada, 1)
            #     if self.root.ml < self.total_ml:
            #         self.root.after(120000, self.llenar_tanque)
			if self.root.ml >= self.total_ml:
				# Fin de programa
				self.root.pin_on(self.root.bomba_entrada, 1)
			else:
				# Después de 200 ms se vuelven a medir los ml
				self.root.after(100, self.measure_ml)
		else:
			self.root.pulses = 0
			self.root.ml = 0
			self.root.pin_on(self.root.bomba_entrada, 1)
			self.root.pin_on(self.root.bomba_salida, 0)
			self.root.after(80000, self.apagar_bomba)

	def llenar_tanque(self):
                self.root.pin_on(self.root.bomba_entrada, 0)
                self.root.after(100, self.measure_ml)

	def apagar_bomba(self):
		self.root.pin_on(self.root.bomba_salida, 1)
