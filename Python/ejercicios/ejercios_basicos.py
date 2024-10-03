import random

def filtrar_umbral(lista, umbral):
    print(lista)
    print(umbral)
    nueva_lista = [i for i in lista if i > umbral]
    print(f"La lista Filtrada por el umbral es: {nueva_lista}")

def calculo_promedio(lista):
    n_elementos = len(lista)
    notas = 0
    for i in lista:
        notas += i
    total = round(notas/n_elementos, 2)
    print(f"el promedio de las notas es: {total}")

def elementos_unicos(lista1, lista2):
    e_comunes = set(lista1) & set(lista2)
    print(f"los elementos comunes son: {list(e_comunes)}")

def diccionario_cadena(cadena):
    valores = {}
    for e in cadena:
        n_repetidas = 0
        for i in cadena:
            if e == i:
                n_repetidas += 1
        valores[e] = n_repetidas
    print(f"los valores de la cadena: {valores}")

class Persona:
    def __init__(self,nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def descripcion(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} años y mi correo es {self.correo}")

if __name__ == '__main__':

    # lista = [random.randint(1, 100) for _ in range(10)]
    # lista_flotante = [round(random.uniform(1, 100), 2) for _ in range(10)]
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [8, 3, 9, 4, 5]


    # filtrar_umbral(lista, 20)
    # calculo_promedio(lista_flotante)
    # elementos_unicos(lista1, lista2)
    # diccionario_cadena("holasseao")

    instancia = Persona("Luis", 21, "miguel.llancari12@gmail.com")
    instancia.descripcion()




