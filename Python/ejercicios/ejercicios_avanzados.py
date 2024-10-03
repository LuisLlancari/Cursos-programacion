import re

def leer_archivo(url):
    with open(url, 'r', encoding="utf-8") as archivo:
        contenido = archivo.read()
        texto_formateado = re.sub(r'[¡!./,]', '', contenido).lower().split()

        contador = dict()
        for p in texto_formateado:
            repeticiones = texto_formateado.count(p)
            contador[p] = repeticiones

        archivo.close()
        return contador

def fibonacci():
    ant_numero = 0
    sig_numero = 1
    while 1 == 1:

        yield sig_numero

        sig_numero = ant_numero + sig_numero
        ant_numero = sig_numero - ant_numero

def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper()



if __name__ == '__main__':

    respuesta = leer_archivo('../archivos/test.txt')
