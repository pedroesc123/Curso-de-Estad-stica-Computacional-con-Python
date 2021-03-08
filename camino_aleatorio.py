
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

# def caminata(campo, borracho, pasos):
#     inicio = campo.obtener_coordenada(borracho)
#     for _ in range(pasos):
#         campo.mover_borracho(borracho)

#     return inicio.distancia(campo.obtener_coordenada(borracho))


# def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
#     borracho = tipo_de_borracho(nombre = 'David')
#     origen = Coordenada(0, 0)
#     distancias = []

#     for _ in range(numero_de_intentos):
#         campo = Campo()
#         campo.añadir_borracho(borracho, origen)
#         simulacion_caminata = caminata(campo, borracho, pasos)
#         distancias.append(round(simulacion_caminata, 0))

#     return distancias

# def graficar(x, y):
#     grafica = figure(title = 'Camino aleatorio', x_axis_label = 'pasos', y_axis_label = 'distancia recorrida')
#     grafica.line(x, y, legend = 'distancia media')

#     show(grafica)


# def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
#     distancias_media_por_caminata = []
#     for pasos in distancias_de_caminata:
#         distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
#         distancia_media = round(sum(distancias)/ len(distancias), 4)
#         distancia_maxima = max(distancias)
#         distancias_media_por_caminata.append(distancia_media)
#         distancia_minima = min(distancias)
#         print(f'{tipo_de_borracho.__name__} caminata  aleatoria de {pasos} pasos')
#         print(f'Media = {distancia_media}')
#         print(f'Max = {distancia_maxima}')
#         print(f'Min = {distancia_minima}')

#     graficar(distancias_de_caminata, distancias_media_por_caminata)


# if __name__ == '__main__':
#     distancias_de_caminata = [10, 100, 1000, 10000]
#     numero_de_intentos = 100

#     main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)


def posicion(tipo_de_borracho, pasos, campo):
    x_eje = []
    y_eje = []
    tipo_de_borracho = BorrachoTradicional(nombre = 'David')
    inicio = Coordenada(0, 0)
    campo.añadir_borracho(tipo_de_borracho, inicio)

    for _ in range(pasos):
        campo.mover_borracho(tipo_de_borracho)
        a = campo.obtener_coordenada(tipo_de_borracho).x 
        b = campo.obtener_coordenada(tipo_de_borracho).y
        x_eje.append(a)
        y_eje.append(b)

    graficar(x_eje, y_eje)


def graficar(x, y):
    grafica = figure(title = 'Camino aleatorio de 1000000', x_axis_label = 'pasos', y_axis_label = 'distancia recorrida')
    grafica.line(x, y, legend = 'distancia media')

    show(grafica)


if __name__ == '__main__':

    pasos = 1000000
    campo = Campo()
    posicion(BorrachoTradicional, pasos, campo)
