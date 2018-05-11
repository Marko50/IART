from random import shuffle
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
    d = Dinner(0, t)
    return d
