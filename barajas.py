import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = [1, 2, 3 ,4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas

def obtener_mano(barajas, tamaño_de_mano):
    mano = random.sample(barajas, tamaño_de_mano)
    return mano

def sort_merge(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        # print(izquierda, '*' * 5, derecha)

        #Llamada recursiva en cada mitad
        sort_merge(izquierda)
        sort_merge(derecha)

        #Iteradores para recorrer las 2 sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        # Obs: Si modificamos la lista dentro de la función tambien
        #      lo hacemos en la lista original(se pasan por referencia)

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
    return lista

def main(tamaño_de_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamaño_de_mano)
        manos.append(mano)
    
    escalera = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        valores_sorted = sort_merge(valores)
        
        i = 0
        
        while int(valores_sorted[i+1]) - int(valores_sorted[i]) == 1:
            i +=1
            if i + 1 == len(valores):
                escalera += 1
                break

    probabi_esc = escalera / intentos
    print(probabi_esc)


    #     counter = dict(collections.Counter(valores))
    #     for val in counter.values():
    #         if val == 3:
    #             pares += 1
    #             break
    
    # probabilidad_par = pares / intentos
    # print(f'La probabilidad de obtener un trio de números iguales en una mano de {tamaño_de_mano} cartas es: {probabilidad_par}')


if __name__ == '__main__':
    tamaño_de_mano = int(input('De cuántas cartas será la mano?: '))
    intentos = int(input('Cuántos intentos quieres?: '))
    
    main(tamaño_de_mano, intentos)
