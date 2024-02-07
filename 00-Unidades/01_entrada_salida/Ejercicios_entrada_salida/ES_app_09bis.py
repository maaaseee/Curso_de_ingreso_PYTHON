import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Federico Gustavo
apellido: Aieta
---
Ejercicio: entrada_salida_09bis
---
Enunciado:
Al presionar el botón 'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        sueldo = self.txt_sueldo.get()
        incr = self.txt_incremento.get()

        sueldo = float(sueldo)
        incr = float(incr)
        
        incremento_sueldo = (sueldo) * (incr)
        incremento_sueldo_2 = incremento_sueldo // 100
        cuenta = sueldo + incremento_sueldo_2

        #cuenta = sueldo * (1 + incr_decimal)

        alert("Aumento" , f"Luego del aumento, su sueldo es de: {cuenta}")

        self.txt_sueldo.delete(0, "end")
        self.txt_incremento.delete(0, "end")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()