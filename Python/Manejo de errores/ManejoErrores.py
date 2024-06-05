try:
  resultado = 10/"s"
except ZeroDivisionError:
  print("¡Error! Division por cero")
except TypeError:
    print("¡Error! Tipo de dato incorrecto.")
except Exception as e:
    print("Se ha producido un error:", e)
