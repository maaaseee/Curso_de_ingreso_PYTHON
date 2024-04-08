import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre = Federico Gustavo
apellido = Aieta
division = B
DNI = 46.745.279

De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál fue el sexo mas ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre de la mascota más pesada
Informe D- El sexo y nombre del gato más viejo
Informe E- El promedio de edad de todas las mascotas
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_f_mascotas = 0
        contador_m_mascotas = 0

        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0

        peso_maximo = 0
        bandera_peso_maximo = False

        edad_gato_maximo = 0
        bandera_gato_maximo = False

        acumulador_edad = 0

        for iteracion in range(1, 6):
            nombre = prompt("", "Ingrese el nombre del animal aquí: ")

            tipo_animal = prompt("", "Ingrese el tipo de mascota aquí (Gato, Perro, o Exotico): ")
            while tipo_animal != "Gato" and tipo_animal != "Perro" and tipo_animal != "Exotico":
                tipo_animal = prompt("", "Ingrese nuevamente el género: Gato, Perro, o Exotico: ")

            peso = prompt("", "Ingrese el peso del animal aquí (en KG): ")
            peso = float(peso)
            while peso < 10 or peso > 80:
                peso = prompt("", "Ingrese nuevamente el peso del animal aquí (en KG): ")
                peso = float(peso)

            sexo = prompt("", "Ingrese el sexo del animal aquí (F o M): ")
            while sexo != "F" and sexo != "M":
                sexo = prompt("", "Ingrese nuevamente el sexo del animal aquí (F o M): ")

            edad = prompt("", "Ingrese la edad del animal aquí: ")
            edad = int(edad)
            while edad < 0:
                edad = prompt("", "Ingrese nuevamente la edad del animal aquí: ")
                edad = int(edad)

            match sexo:
                case "F":
                    contador_f_mascotas += 1
                case "M":
                    contador_m_mascotas += 1

            match tipo_animal:
                case "Gato":
                    contador_gato += 1
                    if edad > edad_gato_maximo or bandera_gato_maximo == False:
                        edad_gato_maximo = edad
                        nombre_gato_maximo = nombre
                        sexo_gato_maximo = sexo
                        bandera_gato_maximo = True
                case "Perro":
                    contador_perro += 1
                case _:
                    contador_exotico += 1

            if peso > peso_maximo or bandera_peso_maximo == False:
                        peso_maximo = peso
                        nombre_peso_maximo = nombre
                        bandera_peso_maximo = True

            acumulador_edad += edad

        if contador_f_mascotas > contador_m_mascotas:
            mensaje_sexo = "El sexo más ingresado fue el F."
        else:
            mensaje_sexo = "El sexo más ingresado fue el M."

        total_mascotas = contador_gato + contador_perro + contador_exotico

        porcentaje_gato = round((contador_gato * 100) / total_mascotas, 2)
        porcentaje_perro = round((contador_perro * 100) / total_mascotas, 2)
        porcentaje_exotico = round((contador_exotico * 100) / total_mascotas, 2)

        promedio_edad_mascotas = round(acumulador_edad / total_mascotas)

        print(mensaje_sexo)
        print(f"El porcentaje de gatos ingresados es del {porcentaje_gato}%")
        print(f"El porcentaje de perros ingresados es del {porcentaje_perro}%")
        print(f"El porcentaje de exoticos ingresados es del {porcentaje_exotico}%")
        print(f"El animal más pesado de todos los ingresados se llama {nombre_peso_maximo}.")
        print(f"El gato más pesado de todos los ingresados se llama {nombre_gato_maximo} y su sexo es {sexo_gato_maximo}.")
        print(f"El promedio de edad de las mascotas es de {promedio_edad_mascotas} años.")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()