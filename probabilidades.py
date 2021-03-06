import random
import collections
from bokeh.plotting import figure, show
from bokeh.layouts import row

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []
    for _ in range(numero_de_tiros):
        tiro_1= random.choice([1, 2, 3, 4, 5, 6])
        tiro_2 = random.choice([1, 2, 3, 4, 5, 6])
        resultado = tiro_1 + tiro_2
        secuencia_de_tiros.append(resultado)
    
    counter = dict(collections.Counter(secuencia_de_tiros))
    x_val = []
    y_val = []
    for x in counter.keys():
        x_val.append(x)
    for y in counter.values():
        y_val.append(y)
    
    print(x_val, y_val)
    graficar(x_val, y_val)

def graficar(x, y):
    grafica = figure(title = 'Trabajando con una muestra', x_axis_label = 'Suma de 2 dados', y_axis_label = 'Número de ocurrencias')
    grafica.vbar(x, top = y, width = 0.5, color = "#CAB2D6")

    show(grafica)

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    suma_tiros_12 = 0
    intentos = 0
    valores_prob = []
    for tiro in tiros:
        if 12 in tiro:
            suma_tiros_12 += 1
        intentos += 1
        probabilidad_parcial = suma_tiros_12 / intentos
        valores_prob.append(probabilidad_parcial)
    
    probabilidad_tiros_con_12 = suma_tiros_12 / numero_de_intentos
    print(f'Probabilidad de obtener una suma de 12 en {numero_de_tiros} tiros = {probabilidad_tiros_con_12}')
    # graficar(list(range(numero_de_intentos)), valores_prob)

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Número de simulaciones: '))
    
    # main(numero_de_tiros, numero_de_intentos)
    tirar_dado(numero_de_tiros)

