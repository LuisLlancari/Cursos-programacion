import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Inicialmente, no se han realizado intercambios
        swapped = False
        # Pasada desde el principio hasta el final de la porción no ordenada
        for j in range(0, n - i - 1):
            # Comparar el elemento actual con el siguiente
            if arr[j] > arr[j + 1]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Indicar que se ha realizado un intercambio
                swapped = True
        # Si no se realizaron intercambios, la lista ya está ordenada
        if not swapped:
            break
    return arr

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


if __name__ == '__main__':
    # ingresamos datos
    tamano_lista = int(input('¿De qué tamaño será la lista?: '))

    # creamos una lista aleatoria
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)