from random import shuffle,random
from Classes.Dinner import Dinner
from Classes.Person import Person
import copy


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

    for a in range(0, l):
        r = random()

        for z in range(0, l):
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

