from Logic.simulated_annealing import *
from Logic.genetic import *
from deap import base,creator

creator.create("FitMax", base.Fitness, weights=(1.0,))

simulated_annealing()
#geneticAlgorithm()