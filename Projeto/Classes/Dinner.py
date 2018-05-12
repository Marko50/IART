from deap import creator
from random import choice

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


    def __cmp__(self, other):
        return self.totalAfinity() > other.totalAfinity()

    def totalAfinity(self):
        return self.afinity

    def calcAfinity(self):
        for x in range(0, len(self.tables)):
            self.afinity += self.tables[x].getAfinity()

    def setProb(self,total,acum):
        self.probabilityMin = acum
        inc = self.totalAfinity()/total
        self.probabilityMax = inc + acum
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

    def subs(self, firstElement, secondElement):
        for x in range(0, len(self.tables)):
            for y in range(0, len(self.tables[x].people)):
                if(self.tables[x].peole[y] == firstElement):
                    self.tables[x].peole[y] = secondElement
                elif(self.tables[x].peole[y] == secondElement):
                    self.tables[x].peole[y] = firstElement

    def mate(self, other):
        print("Mating: " ,str(self.id))
        firstTable = choice(self.tables)
        print("First Table: " ,firstTable)
        secondTable = choice(self.tables)
        print("Second Table: " ,secondTable)
        firstElement = choice(firstTable.people)
        print("First Element: " ,firstElement)
        secondElement = choice(secondTable.people)
        print("Second Element: ",secondElement)
        while(firstElement == secondElement):
            secondElement = choice(secondTable)
        self.subs(firstElement,secondElement)
        other.subs(firstElement,secondElement)