import random

from bokeh.plotting import figure, show

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []
    for _ in range(numero_de_tiros):
        tiro_1= random.choice([1, 2, 3, 4, 5, 6])
        tiro_2 = random.choice([1, 2, 3, 4, 5, 6])
        resultado = tiro_1 + tiro_2
        secuencia_de_tiros.append(resultado)

    return secuencia_de_tiros

def graficar(x, y):
    grafica = figure(title = 'Probabilidad de sumar 12', x_axis_label = 'número de intentos', y_axis_label = 'Probabilidad')
    grafica.line(x,y)

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
    graficar(list(range(numero_de_intentos)), valores_prob)

if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(input('Número de simulaciones: '))
    
    main(numero_de_tiros, numero_de_intentos)

