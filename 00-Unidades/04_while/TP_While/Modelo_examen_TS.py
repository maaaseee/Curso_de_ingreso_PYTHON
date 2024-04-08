
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
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el boton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir = True

        valor_entrada = 0
        descuento_entradas = 0

        contador_masculino_campo = 0
        contador_femenino_campo = 0
        contador_otro_campo = 0

        contador_entrada_general_efectivo = 0
        contador_entrada_campo_efectivo = 0
        contador_entrada_platea_efectivo = 0

        contador_entrada_general_debito = 0
        contador_entrada_campo_debito = 0
        contador_entrada_platea_debito = 0

        contador_entrada_general_credito = 0
        contador_entrada_campo_credito = 0
        contador_entrada_platea_credito = 0

        contador_descuento_general_credito = 0

        acumulador_entradas_credito = 0

        acumulador_edad_entrada_general_credito = 0

        contador_edadprimos_platea = 0

        bandera_maximo_valor = False
        edad_maximo_valor = 0
        nombre_maximo_valor = 0

        numeros_m6_platea_debito = 0

        lista = ""

        while seguir == True:
            nombre = prompt("", "Ingrese su nombre: ")

            edad = prompt("", "Ingrese la edad: ")
            edad = int(edad)
            while edad < 16:
                edad = prompt("", "Ingrese nuevamente la edad (no puede ser menor a 16 años): ")
                edad = int(edad)

            genero = prompt("", "Ingrese el género: Masculino, Femenino, u Otro: ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Ingrese nuevamente el género: Masculino, Femenino, u Otro: ")
            
            entrada_tipo = prompt("", "Ingrese su tipo de entrada: General, Campo delantero, o Platea: ")
            while entrada_tipo != "General" and entrada_tipo != "Campo delantero" and entrada_tipo != "Platea":
                entrada_tipo = prompt("", "Ingrese su tipo de entrada: General, Campo delantero, u Platea: ")
            
            medio_de_pago = prompt("", "Ingrese su método de pago: Efectivo, Debito, o Crédito: ")
            while medio_de_pago != "Efectivo" and medio_de_pago != "Debito" and medio_de_pago != "Credito":
                medio_de_pago = prompt("", "Ingrese su método de pago: Efectivo, Debito, o Crédito: ")

            lista += f"{nombre} - {edad} - {genero} - {entrada_tipo} - {medio_de_pago}\n"

            if entrada_tipo == "General":
                valor_entrada = 16000
            elif entrada_tipo == "Campo delantero":
                valor_entrada = 25000
                # 1)
                if genero == "Masculino":
                    contador_masculino_campo += 1
                elif genero == "Femenino":
                    contador_femenino_campo += 1
                else:
                    contador_otro_campo += 1
            else:
                valor_entrada = 30000
                # 6)
                for rango in range(2, edad +1):
                    contador = 0
                    for rango_2 in range(2, rango +1):
                        if rango % rango_2 == 0:
                            contador += 1
                    if contador < 2 and edad == rango:
                        contador_edadprimos_platea += 1

            match medio_de_pago:
                case "Efectivo":
                    match entrada_tipo:
                        case "General":
                            descuento_entradas = 0
                            # 3)
                            contador_entrada_general_efectivo += 1
                        case "Campo delantero":
                            descuento_entradas = 0
                            # 3)
                            contador_entrada_campo_efectivo += 1
                        case "Platea":
                            descuento_entradas = 0
                            # 3)
                            contador_entrada_platea_efectivo += 1
                case "Debito":
                    match entrada_tipo:
                        case "General":
                            descuento_entradas = valor_entrada * 0.15
                            # 3)
                            contador_entrada_general_debito += 1
                            # 6)
                            if bandera_maximo_valor == False or edad > edad_maximo_valor:
                                edad_maximo_valor = edad
                                bandera_maximo_valor = True
                                nombre_maximo_valor = nombre
                            else:
                                edad_maximo_valor = "No se pudo encontrar"
                                nombre_maximo_valor = "No se pudo encontrar"
                        case "Campo delantero":
                            descuento_entradas = valor_entrada * 0.15
                            # 3)
                            contador_entrada_campo_debito += 1
                        case "Platea":
                            descuento_entradas = valor_entrada * 0.15
                            # 3)
                            contador_entrada_platea_debito += 1
                            # 7)
                            for rango in range(0, edad + 1, 6):
                                if edad == rango:
                                    numeros_m6_platea_debito += 1
                case "Credito":
                    match entrada_tipo:
                        case "General":
                            descuento_entradas = valor_entrada * 0.20
                            # 2)
                            contador_descuento_general_credito += 1
                            acumulador_edad_entrada_general_credito += edad
                            # 2 y 3)
                            contador_entrada_general_credito += 1
                            # 4)
                            acumulador_entradas_credito += descuento_entradas
                        case "Campo delantero":
                            descuento_entradas = valor_entrada * 0.20
                            # 3)
                            contador_entrada_campo_credito += 1
                            # 4)
                            acumulador_entradas_credito += descuento_entradas
                        case "Platea":
                            descuento_entradas = valor_entrada * 0.20
                            # 3)
                            contador_entrada_platea_credito += 1
                            # 4)
                            acumulador_entradas_credito += descuento_entradas

            valor_total = valor_entrada - descuento_entradas
            alert("", f"El total a pagar de su entrada es de ${valor_total}")

            seguir = question("Continuar" , "¿Desea continuar?")

        if contador_femenino_campo > contador_masculino_campo and contador_femenino_campo > contador_otro_campo:
            mensaje_contador_campo = "El género más frecuente entre las entradas de Campo delantero, es el femenino."
        elif contador_masculino_campo > contador_femenino_campo and contador_masculino_campo > contador_otro_campo:
            mensaje_contador_campo = "El género más frecuente entre las entradas de Campo delantero, es el masculino."
        elif contador_masculino_campo == 0 and contador_femenino_campo == 0 and contador_otro_campo == 0:
            mensaje_contador_campo = "No hay un género mas frecuente, ya que no hay entradas vendidas de este tipo"
        else:
            mensaje_contador_campo = "El género más frecuente entre las entradas de Campo delantero, es otro."

        # 1)

        print(f"1) {mensaje_contador_campo}")

        # 2)

        if contador_entrada_general_credito == 0:
            promedio_edad_general_credito = "0"
        else:
            promedio_edad_general_credito = acumulador_edad_entrada_general_credito / contador_entrada_general_credito

        print(f"2) El promedio de edad de las personas que abonaron con tarjeta de credito es de: {promedio_edad_general_credito} y la cantidad de descuentos aplicados a entradas abonadas con tarjeta de credito es de: {contador_entrada_general_credito}")

        # 3)

        total_entradas = (
        contador_entrada_general_credito + contador_entrada_general_debito + contador_entrada_general_efectivo +
        contador_entrada_campo_credito + contador_entrada_campo_debito + contador_entrada_campo_efectivo + 
        contador_entrada_platea_credito + contador_entrada_platea_debito + contador_entrada_platea_efectivo
        )

        promedio_platea_debito = round((contador_entrada_platea_debito * 100) / total_entradas, 2)
        
        print(f"3) El promedio de entradas en Platea abonadas con tarjeta de débito es del {promedio_platea_debito}%")

        # 4)

        print(f"4) La cantidad de plata que se descontó a aquellas personas que abonaron con tarjeta de crédito es de ${acumulador_entradas_credito}")

        # 5)

        print(f"5) El nombre de la persona que más pagó por una entrada general, y abonó con tarjeta de débitto es {nombre_maximo_valor}, y su edad es de {edad_maximo_valor} años")

        # 6)

        print(f"6) {contador_edadprimos_platea}")

        # 7)

        print(f"7) {numeros_m6_platea_debito}")


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()