class Dinner:
    def __init__(self, id, tables):
        self.id = id
        self.tables = tables

    def totalAfinity(self):
        afinity = 0
        for x in range(0, len(self.tables)):
            afinity+= self.tables[x].getAfinity()
        return afinity

    def __repr__(self):
        t = ""
        for x in range(0 , len(self.tables)):
            t += self.tables[x].__repr__() + "\n"
        return  str(self.id) + " " + t