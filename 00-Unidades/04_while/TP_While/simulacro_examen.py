import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Federico Gustavo
apellido: Aieta
---
Ejercicio: for_04
---
Un famoso casino de mar del plata, requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

    Nombre

    Importe ganado (mayor o igual $1000)

    Género (“Femenino”, “Masculino”, “Otro”)

    Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

    1)Nombre y género de la persona que más ganó.

    2)Promedio de dinero ganado en Ruleta.

    3)Porcentaje de personas que jugaron en el Tragamonedas.

    4)Cuál es el juego menos elegido por los ganadores.

    5)Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000

    6)Porcentaje de dinero en función de cada juego
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #region #> "Inicializaciones"

        seguir = True

        maximo_importe_ganado = 0
        bandera_maximo = True

        contador_juego_poker = 0
        contador_juego_ruleta = 0
        contador_juego_tragamonedas = 0

        acumulador_importe_ruleta = 0

        acumulador_importe15 = 0
        contador_tragamonedas_importe15 = 0
        contador_ruleta_importe15 = 0

        acumulador_poker = 0
        acumulador_ruleta = 0
        acumulador_tragamonedas = 0

        #endregion

        while seguir == True:
            nombre = prompt("", "Ingrese su nombre: ")

            importe_ganado = prompt("", "Ingrese el importe ganado: ")
            importe_ganado = float(importe_ganado)
            while importe_ganado < 1000:
                importe_ganado = prompt("", "Ingrese nuevamente el importe (no puede ser menor a $1000): ")
                importe_ganado = float(importe_ganado)

            genero = prompt("", "Ingrese el género: Masculino, Femenino, u Otro: ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Ingrese nuevamente el género: Masculino, Femenino, u Otro: ")
            
            tipo_juego = prompt("", "Ingrese el tipo de juego: Ruleta, Poker, o Tragamonedas: ")
            while tipo_juego != "Ruleta" and tipo_juego != "Poker" and tipo_juego != "Tragamonedas":
                tipo_juego = prompt("", "Ingrese nuevamente el tipo de juego: Ruleta, Poker, o Tragamonedas: ")


            if importe_ganado > maximo_importe_ganado or bandera_maximo == True:
                maximo_importe_ganado = importe_ganado
                nombre_maximo_valor = nombre
                genero_maximo_valor = genero
                bandera_maximo = False

            match tipo_juego:
                case "Poker":
                    contador_juego_poker += 1
                    acumulador_poker += importe_ganado

                case "Ruleta":
                    contador_juego_ruleta += 1
                    acumulador_importe_ruleta += importe_ganado
                    acumulador_ruleta += importe_ganado
                    if importe_ganado > 15000:                          # Redundante (Abrir un if afuera del match, y juntar los contadores)
                        acumulador_importe15 += importe_ganado
                        contador_ruleta_importe15 += 1

                case "Tragamonedas":
                    contador_juego_tragamonedas += 1
                    acumulador_tragamonedas += importe_ganado
                    if importe_ganado > 15000:                          # Redundante (Abrir un if afuera del match, y juntar los contadores)
                        acumulador_importe15 += importe_ganado
                        contador_tragamonedas_importe15 += 1

            seguir = question("Seguir" , "¿Desea continuar?")

        total_usuarios_juego = contador_juego_tragamonedas + contador_juego_poker + contador_juego_ruleta

        if contador_juego_ruleta > 0:
            promedio_importe_ruleta = round(acumulador_importe_ruleta / contador_juego_ruleta, 2)
        else:
            promedio_importe_ruleta = 0

        promedio_usuarios_tragamonedas = round((contador_juego_tragamonedas * 100) / total_usuarios_juego, 2)

        if contador_juego_poker < contador_juego_ruleta and contador_juego_poker < contador_juego_tragamonedas:
            mensaje_contador_juego = "El juego menos jugado por los usuarios, es el Poker."
        elif contador_juego_ruleta < contador_juego_poker and contador_juego_ruleta < contador_juego_tragamonedas:
            mensaje_contador_juego = "El juego menos jugado por los usuarios, es la Ruleta."
        elif (contador_juego_ruleta == contador_juego_poker) and (contador_juego_poker == contador_juego_tragamonedas) and (contador_juego_tragamonedas == contador_juego_ruleta):
            mensaje_contador_juego = "No hay un juego menos frecuente entre los usuarios."
        else:
            mensaje_contador_juego = "El juego menos jugado por los usuarios, es la Tragamonedas."

        total_usuarios_importe15 = contador_ruleta_importe15 + contador_tragamonedas_importe15

        if total_usuarios_importe15 != 0:
            promedio_importe15 = acumulador_importe15 / total_usuarios_importe15
        else:
            promedio_importe15 = "0, ya que no hubo nadie que ganara mas de 15000 en la Ruleta o la Tragamonedas."

        total_importe_ganancia = acumulador_poker + acumulador_ruleta + acumulador_tragamonedas

        porcentaje_ganancia_ruleta = round((acumulador_ruleta * 100) / total_importe_ganancia, 2)
        porcentaje_ganancia_poker = round((acumulador_poker * 100) / total_importe_ganancia, 2)
        porcentaje_ganancia_tragamonedas = round((acumulador_tragamonedas * 100) / total_importe_ganancia, 2)

        alert("1", f"El género de la persona que más ganó es {genero_maximo_valor}, y su nombre es {nombre_maximo_valor} - {maximo_importe_ganado}.")
        alert("2", f"El promedio de ganancias en la ruleta es de ${promedio_importe_ruleta}.")
        alert("3", f"El porcentaje de usuarios que usaron la tragamonedas, a comparación de otros juegosm es del {promedio_usuarios_tragamonedas}%.")
        alert("4", f"{mensaje_contador_juego}")
        alert("5", f"El promedio de ganancias mayores a 15000, en la Ruleta, y en la Tragamonedas, es de ${promedio_importe15}")
        alert("6", f"Porcentaje de ganancias de todos los juegos:\n\t - Poker: {porcentaje_ganancia_poker}%\n\t - Ruleta: {porcentaje_ganancia_ruleta}%\n\t - Tragamonedas: {porcentaje_ganancia_tragamonedas}%")
            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()