
def generador_fibonacci():
    ant_numero = 0
    sig_numero = 1
    while 1 == 1:

        yield sig_numero

        sig_numero = ant_numero + sig_numero
        ant_numero = sig_numero - ant_numero



rpta = generador_fibonacci()
