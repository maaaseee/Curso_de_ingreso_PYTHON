import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Federico
apellido: Aieta
---
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.

Los participantes en la placa son: Giovanni, Gianni y Esteban. Matias no fue nominado y Renato no está en la placa esta semana por haber ganado la inmunidad.

Cada televidente que vota deberá ingresar:

Nombre del votante

Edad del votante (debe ser mayor a 13)

Género del votante (Masculino, Femenino, Otro)

El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:

El promedio de edad de las votantes de género Femenino 

Del votante más viejo, su nombre.

Nombre del votante más joven qué votó a Gianni.

Nombre de cada participante y porcentaje de los votos qué recibió.

El nombre del participante que debe dejar la casa (El que tiene más votos)
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, padx=30, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
            bandera = True
            bandera_votante_viejo = True

            acumulador_edad_femenino = 0

            edad_mas_viejo = 0
            edad_joven = 0

            contador_esteban = 0
            contador_gianni = 0
            contador_giovanni = 0

            contador_femenino = 0

            nombre_mas_joven = ""

            porcentaje_esteban = 0
            porcentaje_gianni = 0
            porcentaje_giovanni = 0
            contador_votos = 0

            while bandera == True:

                nombre_votante = prompt("Nombre", "Ingrese su nombre")

                edad_votante = prompt("Edad", "Ingrese su edad")
                edad_votante = int(edad_votante)
                while edad_votante < 13:
                    edad_votante = prompt("Error", "Reingrese una edad valida")
                    edad_votante = int(edad_votante)
                
                genero_votante = prompt("Genero", "Ingrese su genero")
                if genero_votante == "Femenino":
                        contador_femenino += 1
                        acumulador_edad_femenino += edad_votante
                while genero_votante != "Masculino" and genero_votante != "Femenino" and genero_votante != "Otro":
                    genero_votante = prompt("Error", "Reingrese un genero valido")
                            
                    

                voto_participante = prompt("Participante", "Ingrese su voto")
                while voto_participante != "Giovanni" and voto_participante != "Gianni" and voto_participante != "Esteban":
                    voto_participante = prompt("Participante", "Reingrese un participante que esté en la placa")
                
                contador_votos += 1

                # Del votante más viejo, su nombre.
                while bandera_votante_viejo == True or edad_votante > edad_mas_viejo:
                    edad_mas_viejo = edad_votante
                    nombre_mas_viejo = nombre_votante
                    bandera_votante_viejo = False

            
                match voto_participante:
                    case "Esteban":
                        contador_esteban += 1
                        if contador_esteban != 0:
                            porcentaje_esteban = (contador_esteban * 100) / contador_votos
                    case "Gianni": 
                        contador_gianni += 1
                        if contador_gianni != 0:
                            porcentaje_gianni = (contador_gianni * 100) / contador_votos
                # Nombre del votante más joven qué votó a Gianni.
                        while edad_votante > edad_joven:
                            edad_joven = edad_votante
                            nombre_mas_joven = nombre_votante
                    case "Giovanni":
                        contador_giovanni += 1
                        if contador_giovanni != 0:
                            porcentaje_giovanni = (contador_giovanni * 100) / contador_votos
            

                

                bandera = question("FIN", "¿Desea ingresar otro usuario y voto?")

            
#El promedio de edad de las votantes de género Femenino 

            
            if contador_femenino != 0:
                promedio_edad_femenino = acumulador_edad_femenino / contador_femenino
                print(f"El promedio de edad de las votantes Femenino es de {promedio_edad_femenino}")
            else:
                print("No se ingresó ningun votante femenino")

# Nombre de cada participante y porcentaje de los votos qué recibió.
            print(f"El porcentaje de votos de Esteban es de: {porcentaje_esteban}%\n\tEl de Gianni: {porcentaje_gianni}%\n\tEl de Giovanni: {porcentaje_giovanni}%")

# El nombre del participante que debe dejar la casa (El que tiene más votos)

            if contador_esteban > contador_giovanni and contador_esteban > contador_gianni:
                print("El participante que debe dejar la casa es Esteban")
            elif contador_giovanni > contador_gianni:
                print("El participante que debe dejar la casa es Giovanni")
            else:
                print("El participante que debe dejar la casa es Gianni")

            
            # Nombre del votante más joven qué votó a Gianni.
            if contador_gianni != 0:
                print(f"El nombre del votante mas joven que votó a Gianni es {nombre_mas_joven}")
            else:
                print("Nadie votó por Gianni")
            # Del votante más viejo, su nombre.
            print(f"El votante mas viejo se llama {nombre_mas_viejo}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()