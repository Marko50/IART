class Person:
    def __init__(self, id, name, age, group, hobie, family, job, interest):
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
        if(person.group == self.group):
            afinity += 0.5
        if(person.interest == self.interest):
            afinity+= 0.1
        if(person.family == self.family):
            afinity+= 0.1
        if(person.age == self.age):
            afinity += 0.1
        if(person.job == self.job):
            afinity += 0.1
        if(person.hobie == self.hobie):
            afinity +=0.1
        return afinity

    def __repr__(self):
        return str(self.id) + " " + self.name + " " + str(self.age)+ " " + str(self.group)+ " " + self.hobie + " "+ self.family+ " "  + self.job + " " + self.interest