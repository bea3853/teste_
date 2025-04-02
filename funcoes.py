import statistics

def amplitude(lista):
    menor = min(lista)
    maior =  max(lista)
    amplitude  =  maior - menor
    return amplitude 

def variancia(lista):
    variancia_  =  statistics.variance(lista)
    return variancia_

def desvio_padrao(lista):
    desvio  =  statistics.stdev(lista)
    return desvio    

    

