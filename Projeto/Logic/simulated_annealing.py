from random import shuffle,random
from FileParser import ParseFile
import copy
from Classes.Dinner import Dinner
from Classes.Person import Person
from math import exp

def simulated_annealing():
    filename = 'input'
    tuple = ParseFile.parseFile(filename)
    people = tuple[0]
    tables = tuple[1]
    temperature = 100
    solution = 0
    old_state = 0
    actual_state = generateDinner(tables, people)
    while(temperature > 0):
        actual_state.mutate()
        if(actual_state.totalAfinity() > old_state):
            old_state = actual_state.totalAfinity()
            solution = actual_state
        else:
            r = calcProbability(old_state, actual_state.totalAfinity(), temperature)
            if(measureProbability(r)):
                old_state = actual_state.totalAfinity()
                solution = actual_state
        temperature = updateTemperature(temperature)

    print(solution)

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


def updateTemperature(temperature):
    t = temperature - 1
    return t

def calcProbability(old_afinity, new_afinity,temperature):
    diff = new_afinity - old_afinity
    return exp(-(abs((diff)/temperature)))

def measureProbability(r):
    ra = random()
    return ra > r
