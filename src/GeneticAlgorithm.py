import random
import copy
import time
from Chromosome import *
from ResultsSaver import ResultsSaver


class GeneticAlgorithm:

    def __init__(self, startTime):
        self.chromosomeNumber = 100
        self.fitnessSum = 0.0
        self.resultsSaver = ResultsSaver(startTime)

    def Update(self):
        self.Fitness()
        Chromosome.chromosomes.sort(key=lambda x: x.fitness, reverse=True)
        self.CalculateFitnessSum()
        self.AppendBestResult()
        self.Selection()
        self.Mutate()
        self.NextGenerationGenes()
        Chromosome.ResetChromosomes()

    def Fitness(self):
        for chrom in Chromosome.chromosomes:
            chrom.CalculateFitness()

    def CalculateFitnessSum(self):
        self.fitnessSum = 0.0
        for chrom in Chromosome.chromosomes:
            self.fitnessSum += chrom.fitness

    def SelectParent(self):
        rand = random.uniform(0, self.fitnessSum)
        rand = random.uniform(0, rand)

        runningSum = 0
        for i in range(0, Chromosome.chromosomes.__len__(), 1):
            runningSum += Chromosome.chromosomes[i].fitness
            if(runningSum >= rand):
                return Chromosome.chromosomes[i]

    def Selection(self):
        newChromosomes = []
        for chrom in Chromosome.chromosomes:
            parent = self.SelectParent()
            newChromosomes.append(copy.deepcopy(parent))

        Chromosome.chromosomes = newChromosomes

    def NextGenerationGenes(self):
        if Chromosome.genesNumber < 300:
            Chromosome.genesNumber += 10

            for chrom in Chromosome.chromosomes:
                chrom.IncreaseGenes()

    def Mutate(self):
        for chrom in Chromosome.chromosomes:
            chrom.MutateGenes()

    def AppendBestResult(self):
        best = Chromosome.chromosomes[0]
        self.resultsSaver.AppendResult(best)
