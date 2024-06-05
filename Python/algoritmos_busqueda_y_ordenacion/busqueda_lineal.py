import random

def busqueda_lineal(lista, objetivo):
    match = False
    # recorre elemento de la lista
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
        # retorna un booleano
        return match


if __name__ == '__main__':

    # Ingresamos datos
    tamano_lista = int(input('De que tamaño será la lista? '))
    objetivo = int(input('Que número quieres encontrar? '))

    # creamos una lista aleatoria
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    # ejecutamos función de busqueda
    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)

    # si el return entró en el if
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
