import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nos piden diseñar un sistema de control de ventas para una empresa de electrodomésticos. 
(Teniendo en cuenta que no sabemos cuantas ventas hubo en total y que todos los datos deben ser ingresados por prompt y mostrados en un solo alert)

Para ello los empleados deben ingresar:

-Nombre del producto.

-Tipo de producto (Celular o Computadora o Ventilador)

-Precio del producto (No puede ser menor a $1000)

-Día de la semana en el que se realizó la venta (La empresa no trabaja sábados ni domingos)

En base a la información ingresada se debe informar:

1)El porcentaje de productos que se vendieron por tipo.

2)El nombre del producto más caro vendido.

3)El nombre del producto mas barato vendido un viernes.

4)Promedio de computadoras vendidas.

5)Promedio de errores que ocurrieron durante la carga de datos (Ya sea al ingresar el tipo, el precio o el día de la venta, esto para controlar la eficiencia de los empleados al cargar las ventas)
'''
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        seguir = True

        contador_celu = 0
        contador_compu = 0
        contador_ventilador = 0

        maximo_precio = 0
        bandera_maximo = False

        minimo_precio_viernes = 0
        bandera_minimo = False

        acumulador_computadora = 0

        contador_error_precio = 0
        contador_error_tipo_producto = 0
        contador_error_dia = 0
        
        while seguir == True:
            nombre_producto = prompt("", "Ingrese el nombre de su producto: ")

            tipo_producto = prompt("", "Ingrese el tipo de producto (Celular, Computadora, o Ventilador): ")
            while tipo_producto != "Celular" and tipo_producto != "Computadora" and tipo_producto != "Ventilador":
                tipo_producto = prompt("", "Ingrese el tipo de producto (Celular, Computadora, o Ventilador): ")
                contador_error_tipo_producto += 1

            precio = prompt("", "Ingrese el precio del producto aquí: ")
            precio = float(precio)
            while precio < 1000:
                precio = prompt("", "Ingrese el precio del producto aquí: ")
                precio = float(precio)
                contador_error_precio += 1

            dia = prompt("", "Ingrese el día de la semana (Solo Lunes a Viernes): ")
            while dia != "Lunes" and dia != "Martes" and dia != "Miercoles" and dia != "Jueves" and dia != "Viernes":
                dia = prompt("", "Ingrese el día de la semana (Solo Lunes a Viernes): ")
                contador_error_dia += 1

            match tipo_producto:
                case "Celular":
                    contador_celu += 1
                case "Computadora":
                    contador_compu += 1
                    acumulador_computadora += precio
                case "Ventilador":
                    contador_ventilador += 1

            if precio > maximo_precio or bandera_maximo == False:
                maximo_precio = precio
                nombre_maximo_precio = nombre_producto
                bandera_maximo = True

            if (precio < minimo_precio_viernes and dia == "Viernes") or bandera_minimo == False:
                minimo_precio_viernes = precio
                nombre_minimo_viernes = nombre_producto
                bandera_minimo = True

            seguir = question("Continuar", "¿Desea continuar?")

        total_tipo_productos = contador_celu + contador_compu + contador_ventilador

        porcentaje_celu = round((contador_celu * 100) / total_tipo_productos, 2)
        porcentaje_compu = round((contador_compu * 100) / total_tipo_productos, 2)
        porcentaje_ventilador = round((contador_ventilador * 100) / total_tipo_productos, 2)

        if contador_compu > 0:
            promedio_computadora = acumulador_computadora / contador_compu
        else:
            promedio_computadora = 0

        total_errores = contador_error_dia + contador_error_precio + contador_error_tipo_producto

        mensaje = (f"El porcentaje de celulares vendidos es del {porcentaje_celu}%\n"
                    f"El porcentaje de computadoras vendidas es del {porcentaje_compu}%\n"
                        f"El porcentaje de ventiladores vendidos es del {porcentaje_ventilador}%\n"
                            f"El producto más caro vendido se llama {nombre_maximo_precio}\n"
                                f"El producto más barato vendido un viernes se llama {nombre_minimo_viernes}\n"
                                    f"El promedio de los precios de las computadoras vendidas es de ${promedio_computadora}\n"
                                        f"El total de errores es de {total_errores}")

        alert("", mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()