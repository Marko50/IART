class Person:
    def __init__(self, id = -1, name = "DEFAULT", age = "DEFAULT", group = "DEFAULT", hobie = "DEFAULT", family = "DEFAULT", job = "DEFAULT", interest = "DEFAULT"):
        self.id = id
        self.name = name
        self.age = age
        self.group = group
        self.hobie = hobie
        self.family = family
        self.job = job
        self.interest = interest

    def getAfinity(self, person):
        afinity = 0
        if(self.id != -1 and person.id != -1):
            if (person.group == self.group):
                afinity += 1.0
            if (person.interest == self.interest):
                afinity += 0.5
            if (person.family == self.family):
                afinity += 0.5
            if (person.age == self.age):
                afinity += 0.5
            if (person.job == self.job):
                afinity += 0.5
            if (person.hobie == self.hobie):
                afinity += 0.5
        return afinity

    def __cmp__(self, other):
        return self.id == other.id

    def __repr__(self):
        return "PersonID: " + str(self.id) + " name: " + self.name + " age: " + str(self.age)+ " group: " + str(self.group)+ " hobbie: " + self.hobie + " family: "+ self.family+ " job: "  + self.job + " interest: " + self.interest