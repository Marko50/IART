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
    print("LENGTH: ", l)
    newPop = [0]*(l)
    counter = 0
    selectedForMating = list()
    for x in range(0, l):
        print(selectedPopulation[x])
        if(selectedPopulation[x].probabilityMax > cruzProb):
            print("Selected for mating ")
            selectedForMating.append(selectedPopulation[x])
        else:
            print("Not selected for mating ")
            newPop[counter] = 0
            counter = counter + 1

    lengthMating = len(selectedForMating)
    for y in range(0, lengthMating,2):
        if(y == lengthMating-1):
            print("IMpar")
            indiv = selectedForMating[y].mate(selectedForMating[y])
            newPop[counter] = indiv
        else:
            print("Mating")
            indiv = selectedForMating[y].mate(selectedForMating[y + 1])
            newPop[counter] = indiv
        counter = counter + 1

    return newPop

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
            if (population[z].probabilityMin <= r and population[z].probabilityMax >= r):
                selectedPop[a] = population[z]
                break
    return selectedPop
