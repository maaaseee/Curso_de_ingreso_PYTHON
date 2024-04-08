import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Federico Gustavo
apellido: Aieta
---
Ejercicio: modelo_examen_taylorswift
---
De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

    nombre , 
    temperatura, entre 35 y 42 
    sexo( f, m , nb ) 
    edad(mayor a 0)

pedir datos por prompt y mostrar por print

Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre
Punto C - por el número de DNI del alumno

DNI terminados en  8 o 9

1)) informar la cantidad de personas menores de edad (menos de 18 años)
2) la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        pass
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()