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

from random import shuffle,random
from Classes.Dinner import Dinner
from Classes.Person import Person
import copy
import operator




def geneticAlgorithm():
    filename = 'input'
    tuple = ParseFile.parseFile(filename)
    people = tuple[0]
    tables = tuple[1]
    IND_SIZE = 50


    toolbox = base.Toolbox()
    toolbox.register("individual", generateDinner, tables, people)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual, n=IND_SIZE)

    toolbox.register("mate", mate)
    toolbox.register("mutate", mutate)
    toolbox.register("select", select)

    pop = toolbox.population()
    counter = 0
    old_d = 0
    d = 0
    next_it = 1
    while (next_it):
        selected = toolbox.select(pop)
        toolbox.mate(selected)
        toolbox.mutate(selected)
        pop = selected
        d = max(pop)
        if (d.totalAfinity() > old_d):
            next_it = 1
            counter = 0
            old_d = d.totalAfinity()
        else:
            old_d = d.totalAfinity()
            counter = counter + 1
            if (counter == 10):
                next_it = 0

    print(d)

def generatePop(tables, people):
    peopleCopy = people[:]
    tablesCopy = copy.deepcopy(tables)
    shuffle(peopleCopy)
    for x in range(0, len(tablesCopy)):
        size = tablesCopy[x].size
        if(size >= len(peopleCopy)):
            p = [Person()]*(len(peopleCopy))
            for y in range(0 , len(peopleCopy)):
                p[y] = peopleCopy.pop(0)
            tablesCopy[x].setPeople(p)
        else:
            p = [Person()]*(size)
            for y in range(0, size):
                p[y] = peopleCopy.pop(0)
            tablesCopy[x].setPeople(p)
    return tablesCopy

def generateDinner(tables,people):
    t = generatePop(tables,people)
    d = Dinner(t)
    return d


def mate(selectedPopulation):
    cruzProb = 0.5
    l = len(selectedPopulation)
    selectedForMating = list()
    for x in range(0, l):
        r = random()
        if (r < cruzProb):
            selectedForMating.append(selectedPopulation[x])

    l2 = len(selectedForMating)
    for y in range(0, l2,2):
        if(y == l2-1):
            selectedPopulation[y].mate(selectedPopulation[y])
        else:
            selectedPopulation[y].mate(selectedPopulation[y + 1])

def select(population):
    total = 0
    l = len(population)
    selectedPop = [0] * (l)
    for x in range(0, l):
        total += population[x].totalAfinity()
    acum = 0
    for y in range (0, l):
        inc = population[y].setProb(total,acum)
        acum += inc

    #elitist selection
    sorted_x = sorted(population, key=operator.attrgetter('afinity'))
    selectedPop[0] = sorted_x[len(sorted_x) - 1]
    selectedPop[1] = sorted_x[len(sorted_x) - 2]

    for a in range(2, l):
        r = random()
        for z in range(0, l): ##probabilistic selection
            if (population[z].probabilityMin < r and population[z].probabilityMax >= r):
                selectedPop[a] = copy.copy(population[z])
                break


    return selectedPop


def mutate(population):
    probMut = 0.2
    for x in range(0, len(population)):
        r = random()
        if(r < probMut):
            population[x].mutate()

