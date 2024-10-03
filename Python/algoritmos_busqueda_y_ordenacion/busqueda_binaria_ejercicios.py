# Búsqueda binaria en una lista de enteros
def busqueda_binaria(lista, objetivo):
    start = 0
    end = len(lista) - 1
    while start <= end:
        middle = (start + end) // 2

        if lista[middle] == objetivo:
            return middle
        elif lista[middle] < objetivo:
            start = middle + 1
        else:
            end = middle - 1
    return -1

# Verificar la existencia de un elemento
def existe_elemento_binario(lista, objetivo):
    start = 0
    end = len(lista) - 1
    while start <= end:
        middle = (start + end) // 2

        if lista[middle] == objetivo:
            return True
        elif lista[middle] < objetivo:
            start = middle + 1
        else:
            end = middle - 1
    return False

# Índice de la cadena
def busqueda_binaria_cadenas(lista, objetivo):
    start = 0
    end = len(lista) - 1

    while start <= end:
        middle = (start + end) // 2

        if lista[middle] == objetivo:
            return middle
        elif lista[middle] < objetivo:
            start = middle + 1
        else:
            end = middle - 1
    return -1

def primer_indice(lista, objetivo):
    start = 0
    end = len(lista) - 1
    resultado = -1
    while start <= end:
        middle = (start + end) // 2
        if lista[middle] == objetivo:
            resultado = middle
            end = middle - 1
        elif lista[middle] < objetivo:
            start = middle + 1
        else:
            end = middle - 1
    return resultado

def ultimo_indice(lista, objetivo):
    start = 0
    end = len(lista) - 1
    resultado = -1
    while start <= end:
        middle = (start + end) // 2
        if lista[middle] == objetivo:
            resultado = middle
            start = middle + 1
        elif lista[middle] < objetivo:
            start = middle + 1
        else:
            end = middle - 1
    return resultado

def busqueda_binaria_tuplas(lista, objetivo):
    start = 0
    end = len(lista) - 1
    while start <= end:
        middle = (start + end) // 2

        if lista[middle][0] == objetivo:
            return middle
        elif lista[middle][0] < objetivo:
            start = middle + 1
        else:
            end = middle - 1
    return -1





if __name__ == '__main__':

    # lista = [10, 23, 45, 70, 80, 90]
    # objetivo = 23
    # resultado = busqueda_binaria(lista, objetivo)
    # print(f"El número {objetivo} está en el índice: {resultado}")

    # lista = [1, 3, 5, 7, 9, 11]
    # elemento = 12
    # resultado = existe_elemento_binario(lista, elemento)
    # print(f"¿Existe el elemento {elemento} en la lista? {resultado}")

    # lista = ["apple", "banana", "cherry", "date", "fig", "grape"]
    # objetivo = "apple"
    # resultado = busqueda_binaria_cadenas(lista, objetivo)
    # print(f"La cadena '{objetivo}' está en el índice: {resultado}")

    lista = [2, 4, 4, 4, 6, 8, 10]
    objetivo = 8
    primer_resultado = primer_indice(lista, objetivo)
    ultimo_resultado = ultimo_indice(lista, objetivo)
    print(f"El primer índice del número {objetivo} es: {primer_resultado}")
    print(f"El último índice del número {objetivo} es: {ultimo_resultado}")

    # personas = [("Ana", 25), ("Carlos", 30), ("Luis", 35), ("Maria", 40)]
    # nombre_objetivo = "Carlos"
    # resultado = busqueda_binaria_tuplas(personas, nombre_objetivo)
    # print(f"La persona con nombre '{nombre_objetivo}' está en el índice: {resultado}")