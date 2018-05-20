from Logic.simulated_annealing import *
from Logic.genetic import *
from deap import base,creator

creator.create("FitMax", base.Fitness, weights=(1.0,))

print("1. Genetic Algorithm\n2. Simulated Annealing")
try:
    r = input("Option: ")
except ValueError:
    print("Not a number")
if(r == 1):
    geneticAlgorithm()
elif(r == 2):
    simulated_annealing()
