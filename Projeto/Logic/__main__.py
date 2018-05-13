# coding=utf-8
# B2: Otimizacao na Organizacao de um Jantar
#
# Objectivo
#
# Resolucao do problema de optimizacao da distribuicao de pessoas por mesas num jantar.
#
# Descricao
#
# Esta a ser organizado um jantar solidario, no qual se registaram centenas de pessoas.
#
# Muitas delas estao registadas em grupo (de cônjuges, famílias, amigos), pelo que têm que ficar sentadas na mesma mesa.
# Por outro lado, pretende-se que as pessoas se sintam confortaveis com a companhia que vao ter durante o jantar,
# pelo que devem ser distribuídas de forma a terem alguma afinidade (etaria, profissional, hobística, etc).
#
# Cada mesa podera ter entre Min e Max lugares.
# A sala onde decorrera o jantar comporta um maximo de Nt mesas de cada tamanho t (número de lugares).
# Pretende-se saber quantas mesas de cada tamanho devem ser utilizadas, e como deverao ficar distribuídas as pessoas.
#
# Na resolucao deste problema pode utilizar múltiplas metodologias de optimizacao (Algoritmos Geneticos e uma delas).
# Estas metodologias podem ser utilizadas em conjunto de forma a obter uma solucao de boa qualidade para o problema
# (por exemplo criando uma solucao inicial que depois e iterativamente melhorada).
# Ou podem ser simplesmente utilizadas para efectuar uma analise comparativa do nível de desempenho de cada metodologia.
#
# e tambem valorizada a modelizacao realista do problema.
#-Representacao do tema como problema de otimizacao: estados, funcao de cruzamento/mutacao,
# funcao de vizinhanca, funcao de avaliacao, criterios de paragem.
# Algoritmos de otimizacao a aplicar (ilustrados para o caso concreto).



from deap import base,tools,creator
import sys
from Logic.genetic import *
sys.path.append("..")
from FileParser import ParseFile


filename = 'input'
tuple = ParseFile.parseFile(filename)
people = tuple[0]
tables = tuple[1]



IND_SIZE = 50

creator.create("FitMax", base.Fitness, weights=(1.0,))

toolbox = base.Toolbox()
toolbox.register("individual", generateDinner, tables, people)
toolbox.register("population", tools.initRepeat, list, toolbox.individual, n = IND_SIZE)

toolbox.register("mate", mate)
toolbox.register("mutate", mutate)
toolbox.register("select", select)



pop = toolbox.population()
counter = 0
old_d = 0
response = 0
while (counter < 1000):
    selected = toolbox.select(pop)
    toolbox.mate(selected)
    toolbox.mutate(selected)
    pop = selected
    d = max(pop)
    counter = counter +1
    if(d.totalAfinity() > old_d):
        response = d
        old_d = d.totalAfinity()

print(response)



