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
import random
import sys
from Logic.genetic import *
sys.path.append("..")
from FileParser import ParseFile


filename = 'input'
tuple = ParseFile.parseFile(filename)
people = tuple[0]
tables = tuple[1]

IND_SIZE = 10

creator.create("FitMax", base.Fitness, weights=(1.0,))

toolbox = base.Toolbox()
toolbox.register("individual", generateDinner, tables, people)
toolbox.register("population", tools.initRepeat, list, toolbox.individual, n = IND_SIZE)

# toolbox.register("mate", tools.cxTwoPoint)
# toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
toolbox.register("evaluate",evaluate)
toolbox.register("select", tools.selBest)



pop = toolbox.population()

selected = toolbox.select(pop,2,fit_attr='afinity')

print(pop)

print('----------------------------------------------------------------')

print(selected)

# CXPB, MUTPB, NGEN = 0.5, 0.2, 40
#
# # Evaluate the entire population
# fitnesses = map(toolbox.evaluate, pop)
# for ind, fit in zip(pop, fitnesses):
#    ind.fitness.values = fit
#
# # for g in range(NGEN):
# #    # Select the next generation individuals
# #    offspring = toolbox.select(pop, len(pop))
# #    # Clone the selected individuals
# #    offspring = map(toolbox.clone, offspring)
# #
#    # Apply crossover and mutation on the offspring
#    for child1, child2 in zip(offspring[::2], offspring[1::2]):
#       print(child1)
#       print(child2)
#       if random.random() < CXPB:
#          toolbox.mate(child1, child2)
#          del child1.fitness.values
#          del child2.fitness.values
#
#    for mutant in offspring:
#       if random.random() < MUTPB:
#          toolbox.mutate(mutant)
#          del mutant.fitness.values
#
#    # Evaluate the individuals with an invalid fitness
#    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
#    fitnesses = map(toolbox.evaluate, invalid_ind)
#    for ind, fit in zip(invalid_ind, fitnesses):
#       ind.fitness.values = fit
#
#    # The population is entirely replaced by the offspring
#    pop[:] = offspring
#
# print(pop)





