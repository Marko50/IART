from deap import creator
from random import choice
import copy

class Dinner(object):
    id = 0
    def __init__(self, tables):
        Dinner.id = Dinner.id + 1
        self.tables = tables
        self.fitness = creator.FitMax
        self.afinity = 0
        self.calcAfinity()
        self.probabilityMin = 0
        self.probabilityMax = 0
        self.probability = 0

    def __cmp__(self, other):
        return self.totalAfinity() > other.totalAfinity()

    def totalAfinity(self):
        return self.afinity

    def calcAfinity(self):
        self.afinity = 0
        for x in range(0, len(self.tables)):
            self.afinity += self.tables[x].getAfinity()

    def setProb(self,total,acum):
        self.probabilityMin = acum
        inc = self.totalAfinity()/total
        self.probability = inc
        self.probabilityMax = (inc + acum)
        return inc

    def __repr__(self):
        t = ""
        for x in range(0 , len(self.tables)):
            t += self.tables[x].__repr__() + "\n"
        return  "\n" + " Dinner \n" + t + " Afinity: " + str(self.totalAfinity()) + "\n"

    def __len__(self):
        return len(self.tables)

    def __getitem__(self, item):
        return self.tables[item]

    def __setitem__(self, key, value):
        self.tables[key] = value

    def subs(self, tableIndex, elementIndex, subs):
        ti = 0
        ei = 0
        for x in range(0, len(self.tables)):
            for y in range(0, len(self.tables[x].people)):
                if(self.tables[x].people[y].id == subs.id):
                    ti = x
                    ei = y


        original = copy.deepcopy(self.tables[tableIndex].people[elementIndex])
        self.tables[tableIndex].people[elementIndex] = subs
        self.tables[ti].people[ei] = original
        self.calcAfinity()
        return

    def mate(self, other):
        firstTableChoiceIndex = choice(range(0,len(self.tables)))
        secondTableChoiceIndex = choice(range(0,len(other.tables)))

        firstPersonChoiceIndex = choice(range(0,len(self.tables[firstTableChoiceIndex].people)))
        secondPersonChoiceIndex = choice(range(0,len(other.tables[secondTableChoiceIndex].people)))

        ownSubs = self.tables[firstTableChoiceIndex].people[firstPersonChoiceIndex]
        otherSubs = other.tables[secondTableChoiceIndex].people[secondPersonChoiceIndex]

        self.subs(firstTableChoiceIndex,firstPersonChoiceIndex,otherSubs)
        other.subs(secondTableChoiceIndex,secondPersonChoiceIndex,ownSubs)

    def mutate(self):
        firstTableChoiceIndex = choice(range(0, len(self.tables)))
        secondTableChoiceIndex = choice(range(0, len(self.tables)))

        firstPersonChoiceIndex = choice(range(0, len(self.tables[firstTableChoiceIndex].people)))
        secondPersonChoiceIndex = choice(range(0, len(self.tables[secondTableChoiceIndex].people)))

        ownSubs = self.tables[firstTableChoiceIndex].people[firstPersonChoiceIndex]
        self.subs(secondTableChoiceIndex,secondPersonChoiceIndex, ownSubs)

