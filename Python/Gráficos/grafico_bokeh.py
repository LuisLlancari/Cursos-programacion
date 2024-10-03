from bokeh.plotting import figure, output_file, show



if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_valores = int(input('Cuantos Valores quieres graficar?'))
    x_valores = list(range(total_valores))
    y_valores = []

    for x in x_valores:
        val = int(input(f'Valor para {x} '))
        y_valores.append(val)

    fig.line(x_valores, y_valores, line_width=2)
    show(fig)