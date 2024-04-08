import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
un gimnasio quiere medir el progreso de sus clientes, para ello se debe de ingresas:
Nombre
Edad(debe ser mayor a 12)
Altura(no debe de ser negativo)
Dias que asiste a la semanq(1,3,5)
Kilos qu elevanta en peso muerto (no debe ser cero, ni negativo)

No sabemos cuántos clientes  Serán consultados.
Se debe de informar 
1) El promedio de kilos que levantan  las personas que asisten solo 3 dias a la semana 
2) El porcentaje de clientes que asiste solo 1 dia  a la semana 
3)Nombre y edad del cliente con mas altura 
4)Determinar si los clientes eligen mas ir 1,3 o 5 días
5)Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
                
        self.title("UTN FRA")
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        acumulador_kilos_3 = 0
        cantidad_dias_1= 0
        cantidad_dias_3= 0
        cantidad_dia_5= 0
        bandera_altura_edad= True
        bandera_mas_joven= True
        bandera = True


        while bandera == True:
            nombre = prompt("", "ingrese nombre")
            edad = prompt("","Ingrese la edad")
            edad = int(edad)
            while edad <= 12: 
                edad = prompt("", "ingrese una edad valida")
                edad = int(edad)

            altura = prompt("","Ingrese la altura")
            altura = float(altura)
            while altura < 0:
                altura = prompt("", "ingrese una altura valida")
            altura = float(altura)

            dias = prompt("","Ingrese los dias que asiste")
            dias = int(dias)
            while dias != 1 and dias != 3 and dias != 5:
                dias = prompt("", "ingrese un dia valido")
                dias = int(dias)
            kilos =prompt("","Ingrese los kilos que levanta")
            kilos = int(kilos)
            while kilos < 1:
                kilos =prompt("", "ingrese una cantidad de kilos valida")
                kilos = int(kilos)

            match dias:
                case 1:
                    cantidad_dias_1 += 1
                case 3 :
                    acumulador_kilos_3 += kilos 
                    cantidad_dias_3 += 1
                case 5 :
                    cantidad_dia_5 += 1 
                    if bandera_mas_joven == True:
                        nombre_mas_joven = nombre
                        edad_mas_joven = edad
                        peso_mas_joven = kilos
                        bandera_mas_joven = False
                    else :
                        if edad > edad_mas_joven:
                            nombre_mas_joven = nombre
                            edad_mas_joven = edad
                            peso_mas_joven = kilos



            if bandera_altura_edad == True:
                maximo_altura = altura
                edad_maxima = edad
                nombre_maximo = nombre
                bandera_altura_edad = False
            else:
                if altura > maximo_altura:
                    maximo_altura = altura
                    edad_maxima = edad
                    nombre_maximo = nombre

            bandera = question ("","Quiere ingresar mas?")

        if cantidad_dias_3 > 0:
            promedio_kilos_3 = acumulador_kilos_3 / cantidad_dias_3
        else:
            promedio_kilos_3 = 0

        total= cantidad_dias_1 + cantidad_dias_3 + cantidad_dia_5 
        pocentaje_dias_1 = (cantidad_dias_1  * 100 ) / total


        if cantidad_dias_1 > cantidad_dia_5 and cantidad_dias_1 > cantidad_dias_3:
            print("la mayoria de clientes van un dia a la semana")
        elif cantidad_dia_5 > cantidad_dias_1 and cantidad_dia_5 > cantidad_dias_3:
            print("la mayoria de clientes van solo 5 dias")
        else:
            print("la mayoria de clientes van solo 3 dias")

        print(f"el cliente mas alto se llama {nombre_maximo} y su edad es {edad_maxima}")
        print(f"la persona que levanta mas kilos y va los 5 dias se llama {nombre_mas_joven} y levanta {peso_mas_joven}kg ")
        print(f"el promedio de kilos que levantan los que asisten 3 dias es {promedio_kilos_3}")
        print(f"el porcente de clientes que asisten al dia solo 1 es {pocentaje_dias_1}%")




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()