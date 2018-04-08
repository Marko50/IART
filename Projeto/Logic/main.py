# B2: Otimização na Organização de um Jantar
#
# Objectivo
#
# Resolução do problema de optimização da distribuição de pessoas por mesas num jantar.
#
# Descrição
#
# Está a ser organizado um jantar solidário, no qual se registaram centenas de pessoas.
#
# Muitas delas estão registadas em grupo (de cônjuges, famílias, amigos), pelo que têm que ficar sentadas na mesma mesa.
# Por outro lado, pretende-se que as pessoas se sintam confortáveis com a companhia que vão ter durante o jantar,
# pelo que devem ser distribuídas de forma a terem alguma afinidade (etária, profissional, hobística, etc).
#
# Cada mesa poderá ter entre Min e Max lugares.
# A sala onde decorrerá o jantar comporta um máximo de Nt mesas de cada tamanho t (número de lugares).
# Pretende-se saber quantas mesas de cada tamanho devem ser utilizadas, e como deverão ficar distribuídas as pessoas.
#
# Na resolução deste problema pode utilizar múltiplas metodologias de optimização (Algoritmos Genéticos é uma delas).
# Estas metodologias podem ser utilizadas em conjunto de forma a obter uma solução de boa qualidade para o problema
# (por exemplo criando uma solução inicial que depois é iterativamente melhorada).
# Ou podem ser simplesmente utilizadas para efectuar uma análise comparativa do nível de desempenho de cada metodologia.
#
# É também valorizada a modelização realista do problema.
#-Representação do tema como problema de otimização: estados, função de cruzamento/mutação,
# função de vizinhança, função de avaliação, critérios de paragem.
# Algoritmos de otimização a aplicar (ilustrados para o caso concreto).


import random

from deap import base,creator,tools





def main():
    if __name__ == '__main__':
        main()

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Dinners", list, fitness=creator.FitnessMax)

    IND_SIZE = 10

