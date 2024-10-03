import random


def busqueda_binaria(lista, objetivo):
  inicio = 0
  fin = len(lista) - 1
  while inicio <= fin:
    medio = (inicio + fin) // 2

    if lista[medio] == objetivo:
      return medio  # Índice del objetivo buscado
    elif lista[medio] < objetivo:
      inicio = medio + 1
    else:
      fin = medio - 1
  pass

def busqueda_binaria_recursiva(lista, comienzo, final, objetivo):

  if comienzo > final:
    return False

  medio = (comienzo + final) // 2

  if lista[medio] == objetivo:
    return True
  elif lista[medio] < objetivo:
    return busqueda_binaria_recursiva(lista, medio + 1, final, objetivo)
  else: 
    return busqueda_binaria_recursiva(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
  
  # ingresamos datos
  tamano_lista = int(input('¿De qué tamaño será la lista?: '))
  objetivo = int(input('Que numero quieres encontrar?: '))
  
  # creamos una lista aleatoria
  lista = sorted([random.randint(0,100) for i in range(tamano_lista)])

  # ejecutamos función de busqueda
  encontrado = busqueda_binaria_recursiva(lista, 0, len(lista), objetivo)
  

  print(lista)

  # si el return entró en el if
  print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')