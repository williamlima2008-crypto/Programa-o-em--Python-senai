import modulo


def escola_notas():
    notas  =  []
    q  =  int(input('Quantidade de notas >> '))
    for i in range(q):
        nota = float(input(f'nota - > '))
        notas.append(nota)
    else:
        print(notas)
        media_ =  modulo.media(notas)
        moda_ =  modulo.moda(notas)
        desvio_ =  modulo.desvio(notas)
        score_ =  modulo.score(notas)
        print(f'''
             
          Media - {media_}
          Moda - {moda_}
          Desvio  -  {desvio_}
          Maior e Menor notas  - {score_}

         ''')


escola_notas()   