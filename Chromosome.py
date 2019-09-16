import random
import pygame

class Chromosome:
    genesIterator=0
    genesNumber=50
    chromosomes=[]
    mutationRate=0.9
    targetAreas=[]
    chromosomeNumber=100

    @staticmethod
    def UpdateIterator():
        Chromosome.genesIterator += 1

    @staticmethod
    def IsEndOfGeneration():
        if Chromosome.genesIterator == Chromosome.genesNumber:
            Chromosome.genesIterator = 0
            return True
        return False

    @staticmethod
    def CreateSetOfChromosomes():
        for i in range(Chromosome.chromosomeNumber):
            Chromosome.chromosomes.append(Chromosome())

    def __init__(self):
        self.genes=[] 
        self.fitness= 0.0 
        self.isAlive=True
        self.killed=False
        self.winner=False
        self.iteratorOfAreas=1

        self.playerEndRect= pygame.rect.Rect(0, 0, 0, 0)
        #Chromosome.chromosomes.append(self)
        self.PopulationInit(Chromosome.genesNumber)

    def GetRandomDirection(self):
        position = (0, 0)
        randomValX = random.random()
        if randomValX < 0.4:
            position = (-1, position[1])
        elif randomValX < 0.6:
            position = (0, position[1])
        else:
            position = (1, position[1])

        randomValY = random.random()
        if randomValY < 0.4:
            position = (position[0], -1)
        elif randomValY < 0.6:
            position = (position[0], 0)
        else:
            position = (position[0], 1)

        return position

    def PopulationInit(self, number):
        for i in range(number):
            position = self.GetRandomDirection()
            self.genes.append(position)

    def MutateGenes(self):
        for i in range(self.genes.__len__()):
            rand = random.random()
            if rand> Chromosome.mutationRate:
                self.genes[i]=self.GetRandomDirection()

    def  CalculateFitness(self):
        distanceToTarget=0.0
        if Chromosome.targetAreas[self.iteratorOfAreas].IsAreaReached(self.playerEndRect):
            self.iteratorOfAreas+=1
            if self.iteratorOfAreas == Chromosome.targetAreas.__len__():
                self.winner=True
            distanceToTarget=self.iteratorOfAreas/float(Chromosome.targetAreas.__len__())     #lub +=
     #   else:
        valInTargetArea=self.iteratorOfAreas/float(Chromosome.targetAreas.__len__())
        distaneValToTarget=1/float((Chromosome.targetAreas[self.iteratorOfAreas].CalculateDistance(self.playerEndRect)+1))
        distanceToTarget+= distaneValToTarget * valInTargetArea + (self.iteratorOfAreas)/float(Chromosome.targetAreas.__len__())
        # print(distaneValToTarget)
        if self.killed:
            distanceToTarget*=0.9
            self.killed=False
        self.fitness+=distanceToTarget   

    def IncreaseGenes(self):
        i=self.genes.__len__()
        for i in range(Chromosome.genesNumber):
            position = self.GetRandomDirection()
            self.genes.append(position)

