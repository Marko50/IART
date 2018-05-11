from deap import creator

class Dinner(object):
    id = 0
    def __init__(self, tables):
        Dinner.id = Dinner.id + 1
        self.tables = tables
        self.fitness = creator.FitMax
        self.afinity = 0
        self.probability = 0

    def __cmp__(self, other):
        return self.totalAfinity() > other.totalAfinity()

    def totalAfinity(self):
        self.afinity = 0
        for x in range(0, len(self.tables)):
            self.afinity+= self.tables[x].getAfinity()
        return self.afinity

    def setProb(self,total):
        self.probability = self.totalAfinity()/total

    def __repr__(self):
        t = ""
        for x in range(0 , len(self.tables)):
            t += self.tables[x].__repr__() + "\n"
        return  str(Dinner.id) + " " + t + " --Afinity: " + str(self.totalAfinity()) + "\n"

    def __len__(self):
        return len(self.tables)

    def __getitem__(self, item):
        return self.tables[item]

    def __setitem__(self, key, value):
        self.tables[key] = value