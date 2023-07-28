# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Electrico)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) NOMBRE TIPO PODER ATAQUE
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Electrico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo electrico con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex 🎮", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.image = tk.PhotoImage(file='Logo_UTN_App.png')
        
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = 'Banner')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Psyduck", "Eevee", "Gengar", "Mewtwo", "Vaporeon"]
        self.lista_poder_pokemones = [80, 150, 70, 90, 60, 100, 75, 120, 180, 95]
        self.lista_tipo_pokemones = ["eléctrico", "fuego", "planta", "agua", "normal", "agua", "normal", "fantasma", "psíquico", "agua"]
# B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
# y mostrar los informe del punto C.

    

    def btn_mostrar_informe_1(self):
        #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
        i = 0
        contador_fuego = 0


        for pokemon in self.lista_nombre_pokemones:
            print(f"Indice: {i} - Nombre: {pokemon} - Poder: {self.lista_poder_pokemones[i]} - Tipo: {self.lista_tipo_pokemones[i]}")
            i += 1

        for tipo in self.lista_tipo_pokemones:
            if tipo == "fuego":
                poder = self.lista_poder_pokemones[self.lista_tipo_pokemones.index(tipo)]
                poder = poder + (poder * 10 / 100)
                if poder > 100:
                    contador_fuego += 1
                    
        # for i, tipo in enumerate(self.lista_tipo_pokemones):
        #     if tipo == "fuego":
        #         poder = self.lista_poder_pokemones[i] * 1.1
        #         if poder > 100:
        #             contador_fuego += 1

        
        print(f"Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos: {contador_fuego} ")


    def btn_mostrar_informe_2(self):
        #! 9) - el promedio de poder de todos los pokemones de tipo Electrico.

        i = 0
        contador = 0
        acumulador_poder = 0
        for tipo in self.lista_tipo_pokemones:
            if tipo == "eléctrico":
                contador += 1
                poder = self.lista_poder_pokemones[i]
                acumulador_poder += poder
            i += 1

        if contador == 0:
            txt = "No hay pokemones de tipo electrico"
        else:
            txt = f"El promedio de poder de todos los pokemones de tipo electrico es: {acumulador_poder / contador}"

        print(txt)

    def btn_mostrar_informe_3(self):
        #! 3) - Nombre y Poder del pokemon de tipo psiquico con el poder mas bajo.
        i = 0
        flag = True
        for tipo in self.lista_tipo_pokemones:
            if tipo == "psíquico":
                if flag == True:
                    pokemon = self.lista_nombre_pokemones[i]
                    poder_mas_bajo = self.lista_poder_pokemones[i]
                    flag = False
                elif self.lista_poder_pokemones[i] < poder_mas_bajo:
                    pokemon = self.lista_nombre_pokemones[i]
                    poder_mas_bajo = self.lista_poder_pokemones[i]

            i+= 1

        print(f"Nombre: {pokemon} - Poder: {poder_mas_bajo}")





    def btn_cargar_pokedex_on_click(self):
        for _ in range(10):

            pokemon = prompt("Carga de datos", "Ingrese Pokemon")
            while not pokemon or not pokemon.isalpha():
                pokemon = prompt("Carga de datos", "Rengrese Pokemon")

            tipo = prompt("Carga de datos", "Ingrese Tipo de pokemon")
            while tipo != "Agua" and tipo != "Psiquico" and tipo != "Electrico":
                tipo = prompt("Carga de datos", "Reingrese Tipo de pokemon")
            poder_ataque = prompt("Carga de datos", "Ingres el poder del pokemon")
            while (poder_ataque == None or not poder_ataque.isdigit()) or int(poder_ataque) < 50 or int(poder_ataque) > 200:
                poder_ataque = prompt("Carga de datos", "Reingrees el poder del pokemon")


            self.lista_nombre_pokemones.append(pokemon)
            self.lista_poder_pokemones.append(poder_ataque)
            self.lista_tipo_pokemones.append(tipo)
            
            
                

if __name__ == "__main__":
    app = App()
    app.mainloop()