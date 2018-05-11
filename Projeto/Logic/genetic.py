from random import shuffle,random
from Classes.Dinner import Dinner
import copy


def generatePop(tables, people):
    peopleCopy = people[:]
    tablesCopy = copy.deepcopy(tables)
    shuffle(peopleCopy)
    for x in range(0, len(tablesCopy)):
        size = tablesCopy[x].size
        if(size >= len(peopleCopy)):
            p = [0]*(len(peopleCopy))
            for y in range(0 , len(peopleCopy)):
                p[y] = peopleCopy.pop(0)
            tablesCopy[x].setPeople(p)
        else:
            p = [0]*(size)
            for y in range(0, size):
                p[y] = peopleCopy.pop(0)
            tablesCopy[x].setPeople(p)
    return tablesCopy

def generateDinner(tables,people):
    t = generatePop(tables,people)
    d = Dinner(t)
    return d

def evaluate(individual):
    return individual.totalAfinity()

def mate(indiv1, indiv2):
    return

def select(population):
    total = 0
    l = len(population)
    selectedPop = [0] * (l)
    for x in range(0, l):
       total += population[x].totalAfinity()
    for y in range (0, l):
        population[y].setProb(total)

    r = random()
    count = 0
    for z in range(0,l):
        if(population[z].probability > r):
            count = count + 1
            selectedPop[z] = population[z]

    ls = len(selectedPop)

    if(count < selectedPop):
        while (count < selectedPop):
            
            count = count + 1

    return
