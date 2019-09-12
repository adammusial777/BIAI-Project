import random
import Position as Pos
from Chromosome import *

class GeneticAlgorithm:

    def __init__(self):
        self.chromosomeNumber=100
        self.fitnessSum=0

    def Mutate(self):
        pass



    def Fitness(self):
        for chrom in Chromosome.chromosomes:
            chrom.CalculateFitness()

    def SelectParent(self):
        rand = random.uniform(0,self.fitnessSum)
        runningSum=0
        for i in range(0, Chromosome.chromosomes.__len__(), 1):
            runningSum+=Chromosome.chromosomes[i].fitness
            if(runningSum>rand):
                return Chromosome.chromosomes[i]

    def CalculateFitnessSum(self):
        self.fitnessSum=0
        for chrom in Chromosome.chromosomes:
            self.fitnessSum=chrom.fitness
         

    def Crossover(self):
        pass

    def Selection(self):
        pass

    def TheBestSelection(self):
        pass

geneticAlgorithm=GeneticAlgorithm()

