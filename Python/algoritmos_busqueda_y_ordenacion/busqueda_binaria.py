import random

def busqueda_binaria(lista, comienzo, final, objetivo):

  if comienzo > final:
    return False

  medio = (comienzo + final) // 2

  if lista[medio] == objetivo:
    return True
  elif lista[medio] < objetivo:
    return busqueda_binaria(lista, medio + 1, final, objetivo)
  else: 
    return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
  
  # ingresamos datos
  tamano_lista = int(input('¿De qué tamaño será la lista?: '))
  objetivo = int(input('Que numero quieres encontrar?: '))
  
  # creamos una lista aleatoria
  lista = sorted([random.randint(0,100) for i in range(tamano_lista)])

  # ejecutamos función de busqueda
  encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
  

  print(lista)

  # si el return entró en el if
  print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')