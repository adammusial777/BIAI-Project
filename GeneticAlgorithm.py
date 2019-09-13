import random
import copy
from Chromosome import *

class GeneticAlgorithm:

    def __init__(self):
        self.chromosomeNumber=100
        self.fitnessSum=0

    def Update(self):
        self.Fitness()
        self.CalculateFitnessSum()
        self.Selection()
        
    def Fitness(self):
        for chrom in Chromosome.chromosomes:
            chrom.CalculateFitness()

    def CalculateFitnessSum(self):
        self.fitnessSum=0
        for chrom in Chromosome.chromosomes:
            self.fitnessSum=chrom.fitness
    
    def SelectParent(self):
        rand = random.uniform(0,self.fitnessSum)
        runningSum=0
        for i in range(0, Chromosome.chromosomes.__len__(), 1):
            runningSum+=Chromosome.chromosomes[i].fitness
            if(runningSum>rand):
                return Chromosome.chromosomes[i]

    def Selection(self):
        newChromosomes=[]
        for chrom in Chromosome.chromosomes:
            parent=self.SelectParent()
            newChromosomes.append(copy.deepcopy(parent))

        Chromosome.chromosomes=newChromosomes

    def Mutate(self):
        pass

    def Crossover(self):
        pass

    def TheBestSelection(self):
        pass

    def TheBestChromosome(self):
        pass


geneticAlgorithm = GeneticAlgorithm()
