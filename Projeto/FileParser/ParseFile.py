# Typical file organization
#  NoTables
#  TablesSize
# Person1Name : age - group - hobie - family - job - interest
# Person2Name : age - group - hobie - family - job - interest
# Person3Name : age - group - hobie - family - job - interest
# Person4Name : age - group - hobie - family - job - interest
# Person5Name : age - group - hobie - family - job - interest
# (..)

from Classes.Person import Person
from Classes.Table import Table


def parseFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    numberTables = int(lines[0])
    tablesSize = int(lines[1])
    length = len(lines)
    people = [0] * (length - 2)
    tables = [numberTables]
    for x in range(2, length):
        splitedSemiColumn = lines[x].split(':')
        name = splitedSemiColumn[0]
        caracteristics = splitedSemiColumn[1].split('-')
        age = caracteristics[0]
        group = caracteristics[1]
        hobbie = caracteristics[2]
        family = caracteristics[3]
        job = caracteristics[4]
        interest = caracteristics[5]
        person = Person(x - 1, name, age, group, hobbie, family, job, interest)
        people[x - 2] = person

    for y in range(0, numberTables):
        table = Table(y, tablesSize)
        tables[y] = table

    file.close()

    return people, tables
