
def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

def ordenamiento_burbuja_optimizado(lista):
    n = len(lista)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

def ordenamiento_burbuja_cadenas(lista):
    n = len(lista)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

def ordenamiento_burbuja_diccionarios(lista):
    n = len(lista)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j].get('edad') > lista[j + 1].get('edad'):

                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

def ordenamiento_burbuja_descendente(lista):
    n = len(lista)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista



if __name__ == '__main__':

    # lista = [64, 34, 25, 12, 22, 11, 90]
    # ordenamiento_burbuja(lista)
    # print("Lista ordenada:", lista)

    # lista = [5, 1, 4, 2, 8]
    # ordenamiento_burbuja_optimizado(lista)
    # print("Lista ordenada:", lista)

    # lista = ["banana", "apple", "cherry", "date"]
    # ordenamiento_burbuja_cadenas(lista)
    # print("Lista ordenada:", lista)

    # personas = [
    #     {"nombre": "Ana", "edad": 25},
    #     {"nombre": "Luis", "edad": 30},
    #     {"nombre": "Carlos", "edad": 35}
    # ]
    # ordenamiento_burbuja_diccionarios(personas)
    # print("Lista ordenada por edad:", personas)

    lista = [64, 34, 25, 12, 22, 11, 90]
    ordenamiento_burbuja_descendente(lista)
    print("Lista ordenada en orden descendente:", lista)