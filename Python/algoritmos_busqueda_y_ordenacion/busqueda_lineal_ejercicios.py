# Devuelve el índice del elemento
def busqueda_lineal(lista, objetivo):
    index = 0
    for element in lista:
        if element == objetivo:
            return index
        else:
            index += 1
    return -1

# Devuelve las ocurrencias de un elemento en una lista
def contar_ocurrencias(lista, elemento):
    ocurrencias = 0
    for valor in lista:
        if valor == elemento:
            ocurrencias += 1

    return ocurrencias

# Devuelve el índice de un elemento
def busqueda_lineal_cadenas(lista, objeto):
    index = 0
    for elemento in lista:
        if elemento == objeto:
            return index
        else:
            index += 1
    return -1

# Devuelve un Booleano si el elemento existe
def existe_elemento(lista, elemento):
    match = False
    for valor in lista:
        if valor == elemento:
            match = True
            break
    return match

# Devuelve el índice de un objeto dentro de una lista
def busqueda_lineal_diccionarios(lista, nombre_objetivo):
    index = 0
    for elemento in lista:
        if elemento.get("nombre") == nombre_objetivo:
            return index
        else:
            index += 1
    return -1


if __name__ == '__main__':

    # lista = [10, 23, 45, 70, 11, 15]
    # objetivo = 70
    # resultado = busqueda_lineal(lista, objetivo)
    # print(f"el número {objetivo} está en el índice: {resultado}")

    # lista = [1, 2, 3, 4, 2, 2, 5, 2, 6]
    # elemento = 2
    # respuesta = contar_ocurrencias(lista, elemento)
    # print(f"El número {elemento} aparece {respuesta} veces en la lista")

    # lista = ["manzana", "banana", "cereza", "durazno"]
    # objetivo = "cereza"
    # resultado = busqueda_lineal_cadenas(lista, objetivo)
    # print(f"La cadena '{objetivo}' está en el índice: {resultado}")

    # lista = [3, 8, 12, 20, 25]
    # elemento = 50
    # resultado = existe_elemento(lista, elemento)
    # print(f"¿Existe el elemento {elemento} en la lista? {resultado}")

    personas = [
        {"nombre": "Ana", "edad": 25},
        {"nombre": "Luis", "edad": 30},
        {"nombre": "Carlos", "edad": 35}
    ]
    nombre_objetivo = "Luis"
    resultado = busqueda_lineal_diccionarios(personas, nombre_objetivo)
    print(f"La persona con nombre '{nombre_objetivo}' está en el índice: {resultado}")
