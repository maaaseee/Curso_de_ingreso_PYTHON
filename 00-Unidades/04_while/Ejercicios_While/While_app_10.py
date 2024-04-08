
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Federico Gustavo
apellido: Aieta
---
Ejercicio: while_practica_clase
---
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir = True
        contador_Masculino_IOT_IA = 0
        contador_Femenino_IA = 0
        acumulador_Femenino_IA = 0
        contador_IOT_edad = 0

        contador_IA = 0
        contador_IOT = 0
        contador_RV_RA = 0

        contador_masculino = 0
        contador_femenino = 0
        contador_genero_otro = 0

        minima_edad = 0
        bandera_minima_edad = False

        lista = ""

        while seguir == True:
            nombre = prompt("", "Ingrese el nombre: ")
            
            edad = prompt("", "Ingrese la edad: ")
            edad = int(edad)
            while edad < 18:
                edad = prompt("", "Ingrese nuevamente la edad (no puede ser menor a 18 años): ")
                edad = int(edad)

            genero = prompt("", "Ingrese el género: Masculino, Femenino, u Otro: ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("", "Ingrese nuevamente el género: Masculino, Femenino, u Otro: ")
            
            tecnologia = prompt("", "Ingrese la tecnología: IA, RV/RA , u IOT: ")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("", "Ingrese la tecnología: IA, RV/RA , u IOT: ")

            lista += f"{nombre} - {edad} - {genero} - {tecnologia}\n"
            
            match tecnologia:
                case "IA":
                    contador_IA += 1
                case "IOT":
                    contador_IOT += 1
                    if (edad > 18 and edad < 25) or (edad > 33 and edad < 42):
                        contador_IOT_edad += 1
                case "RV/RA":
                    contador_RV_RA += 1
                    if bandera_minima_edad == False or edad < minima_edad:
                        minima_edad = edad
                        bandera_minima_edad = True
                        nombre_minima_edad = nombre
                        genero_minima_edad = genero

            match genero:
                case "Masculino":
                    contador_masculino += 1
                    if (tecnologia == "IOT" or tecnologia == "IA") and (edad >= 25 and edad <= 50):
                        contador_Masculino_IOT_IA += 1

                case "Femenino":
                    contador_femenino += 1
                    if tecnologia == "IA":
                        contador_Femenino_IA += 1
                        acumulador_Femenino_IA += edad

                case "Otro":
                    contador_genero_otro += 1

            seguir = question("Continuar" , "¿Desea continuar?")
        
        if contador_IA > contador_RV_RA and contador_IA > contador_IOT:
            mensaje_mas_votado = ("La tecnología que más se votó fue IA.")
        elif contador_RV_RA > contador_IA and contador_RV_RA > contador_IOT:
            mensaje_mas_votado =("La tecnología que más se votó fue RV/RA.")
        else:
            mensaje_mas_votado = ("La tecnología que más se votó fue IOT.")
        
        total_genero_empleados = contador_masculino + contador_femenino + contador_genero_otro

        porcentaje_masculinos = round((contador_masculino * 100) / total_genero_empleados, 2)
        porcentaje_femeninos = round((contador_femenino * 100) / total_genero_empleados, 2)
        porcentaje_genero_otro = round((contador_genero_otro * 100) / total_genero_empleados, 2)
        
        if contador_IOT > 0:
            porcentaje_iot_rango = round((contador_IOT_edad * 100) / contador_IOT, 2)
        else:
            porcentaje_iot_rango = 0

        if contador_Femenino_IA > 0:
            promedio_edades_ia_femenino = round(acumulador_Femenino_IA / contador_Femenino_IA, 2)
        else:
            promedio_edades_ia_femenino = "0 (Ninguna de las encuestadas votó por IA)."

        alert("", f"Cantidad de empleados que votaron IOT u IA de entre 25 a 50 años: {contador_Masculino_IOT_IA}.")
        alert("", f"{mensaje_mas_votado}")
        alert("", f"{porcentaje_masculinos}% que votó fueron del género masculino, otro {porcentaje_femeninos}% que votó fue del género \
                femenino, y el otro {porcentaje_genero_otro}% que votó fue del genero otro.")
        alert("", f"El {round(porcentaje_iot_rango, 2)}% de los encuestados de edad entre los 18 y 25, o 33 a 42 años, votaron por la tecnología IOT.")
        alert("", f"El promedio de edad de las encuestadas que votaron por IA es de {promedio_edades_ia_femenino}.")
        alert("", f"{nombre_minima_edad}, de género {genero_minima_edad} es el encuestado más joven que votó por RV/RA.")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()