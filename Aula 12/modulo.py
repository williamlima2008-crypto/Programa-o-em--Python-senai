import statistics

def moda(notas):
    r =  statistics.mode(notas)
    return r

def desvio(notas):
    r =  statistics.stdev(notas)
    return r

def media(notas):
    r =  statistics.mean(notas)
    return r

def score(notas):
    rmaior =  max(notas)
    rmenor = min(notas)
    return rmaior , rmenor