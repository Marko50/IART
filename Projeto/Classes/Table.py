class Table:
    def __init__(self, id = -1, size = -1):
        self.size = size
        self.id = id
        self.people = list()

    def __repr__(self):
        st = ""
        if(self.size > len(self.people)):
            for x in range(0, len(self.people)):
                st += self.people[x].__repr__() + "\n"
        else:
            for x in range(0, self.size):
                st += self.people[x].__repr__() + "\n"

        return "TableID: " + str(self.id) + " SIze: " + str(self.size) + "\n" + st +"\n"

    def setPeople(self, people):
        if(len(people) > self.size):
            raise Exception("Incorrect size for table " + str(self.id))
        else:
            self.people = people

    def getAfinity(self):
        afinity = 0
        if (self.size > len(self.people)):
            for x in range(0, len(self.people)):
                if (x < len(self.people) - 1):
                    afinity += self.people[x].getAfinity(self.people[x + 1])
        else:
            for x in range(0, self.size):
                if (x < self.size - 1):
                    afinity += self.people[x].getAfinity(self.people[x + 1])

        return afinity

