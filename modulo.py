

import statistics 


def variance_(dados):
    vari = statistics.variance(dados)
    return vari



def desvio(dados):
    d = statistics.stdev(dados)
    return d



def mode_(dados):
    m = statistics.mode(dados)
    return m



def mean_(dados):
    media = statistics.mean(dados)
    return media


def max_(dados):
    maior = max(dados)
    return maior



def min_(dados):
    menor = min(dados)
    return menor
    