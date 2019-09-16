import random
import copy
from Chromosome import *

class GeneticAlgorithm:

    def __init__(self):
        self.chromosomeNumber=100
        self.fitnessSum=0.0

    def Update(self, players):
        self.Fitness(players)
        Chromosome.chromosomes.sort(key=lambda x: x.fitness, reverse=True)
        self.CalculateFitnessSum()
        self.Selection()
        self.Mutate()
        self.NextGenerationGenes()
        
    def Fitness(self, players):
        for i in range(self.chromosomeNumber):
            Chromosome.chromosomes[i].CalculateFitness(players[i])

    def CalculateFitnessSum(self):
        self.fitnessSum=0.0
        for chrom in Chromosome.chromosomes:
            self.fitnessSum+=chrom.fitness
    
    def SelectParent(self):
        rand = random.uniform(0,self.fitnessSum)
        runningSum=0
        for i in range(0, Chromosome.chromosomes.__len__(), 1):
            runningSum+=Chromosome.chromosomes[i].fitness
            if(runningSum>=rand):
                return Chromosome.chromosomes[i]

    def Selection(self):
        newChromosomes=[]
        for chrom in Chromosome.chromosomes:
            parent=self.SelectParent()
            newChromosomes.append(copy.deepcopy(parent))

        Chromosome.chromosomes=newChromosomes
        print(Chromosome.chromosomes[0].fitness)

    def NextGenerationGenes(self):
        Chromosome.genesNumber+=10
        for chrom in Chromosome.chromosomes:
            chrom.IncreaseGenes()

    def Mutate(self):
        for chrom in Chromosome.chromosomes:
            chrom.MutateGenes()

    def TheWinnerChromosome(self):
        return next(x for x in Chromosome.chromosomes if x.winner==True )

geneticAlgorithm = GeneticAlgorithm()
