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
        cantidad_ingresados = 0
        
        contador_m = 0
        contador_f = 0
        contador_nb = 0

        contador_fiebre = 0
        contador_no_fiebre = 0

        contador_menores = 0
        acumulador_fiebre = 0

        bandera_f_fiebre_baja = False
        fiebre_minima = 0
        
        while cantidad_ingresados < 5:
            nombre = input("Coloque su nombre aquí: ")

            temperatura = input("Coloque su temperatura aquí: ")
            temperatura = float(temperatura)
            while temperatura < 35 or temperatura > 42:
                temperatura = input("Coloque nuevamente su temperatura aquí: ")
                temperatura = float(temperatura)

            genero = input("Coloque su género aquí (M, F, NB): ")
            while genero != "M" and genero != "F" and genero != "NB":
                genero = input("Coloque nuevamente su género aquí (M, F, NB): ")

            edad = input("Coloque su edad aquí: ")
            edad = int(edad)
            while edad < 0:
                edad = input("Coloque su edad aquí: ")
                edad = int(edad)

            if edad < 18:
                contador_menores += 1
                acumulador_fiebre += temperatura
            
            match genero:
                case "M":
                    contador_m += 1
                case "F":
                    contador_f += 1
                    if temperatura < fiebre_minima or bandera_f_fiebre_baja == False:
                        fiebre_minima = temperatura
                        nombre_fiebre_minima = nombre
                        bandera_f_fiebre_baja = True
                case "NB":
                    contador_nb += 1

            if temperatura > 38:
                contador_fiebre += 1
            else:
                contador_no_fiebre += 1

            cantidad_ingresados += 1

        if contador_f > contador_m and contador_f > contador_nb:
            mensaje_genero = "El género más frecuente es el femenino."
        elif contador_m > contador_f and contador_m > contador_nb:
            mensaje_genero = "El género más frecuente es el masculino."
        else:
            mensaje_genero = "El género más frecuente es no binario."

        total_fiebre = contador_fiebre + contador_no_fiebre

        porcentaje_fiebre = round((contador_fiebre * 100) / total_fiebre, 2)
        porcentaje_no_fiebre = round((contador_no_fiebre * 100) / total_fiebre, 2)

        if contador_menores != 0:
            promedio_fiebre_menores = acumulador_fiebre / contador_menores
        else:
            promedio_fiebre_menores = "0, ya que no hay menores de edad."

        print(mensaje_genero)
        print(f"El porcentaje de personas con fiebre que ingresaron al hospital es del {porcentaje_fiebre}%")
        print(f"El porcentaje de personas con fiebre que ingresaron al hospital es del {porcentaje_no_fiebre}%")
        print(f"En total ingresaron {contador_menores} menores de edad al hospital.")
        print(f"El promedio de temperatura en los menores de edad es de: {promedio_fiebre_menores}")
        print(f"El nombre de la persona de género F, con menor temperatura, es: {nombre_fiebre_minima}")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()