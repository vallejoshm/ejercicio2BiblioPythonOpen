from functools import reduce

def filtroYSuma(numeros):

    sumaImpares = reduce(lambda x, y: x+y, list(filter(lambda x: x % 2 != 0, numeros)))

    return  sumaImpares
