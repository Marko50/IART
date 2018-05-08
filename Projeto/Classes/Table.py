class Table:
    def __init__(self, id, size):
        self.size = size
        self.id = id

    def __repr__(self):
        return str(self.id) + " " + str(self.size)

    def setPeople(self, people):
        if(len(people) != self.size):
            raise Exception("Incorrect size for table " + self.id)
        else:
            self.people = people

    def getAfinity(self):
        afinity = 0
        for x in range(0, self.size):
            if(x < self.size - 1):
                afinity += self.people[x].getAfinity(self.people[x+1])

        return afinity

