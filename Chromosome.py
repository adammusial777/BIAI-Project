import random


class Chromosome:
    genesIterator=0
    genesNumber=100
    chromosomes=[]

    @staticmethod
    def UpdateIterator():
        Chromosome.genesIterator += 1
        if Chromosome.genesIterator == Chromosome.genesNumber:
            Chromosome.genesIterator = 0

    def __init__(self):
        self.genes=[] #jako lista genów (gen jako pozycja? zestaw genów jako trasa pozycji do celu?)
        self.fitness= 0.0 #ocena skuteczności (na podstawie odległości od pola końcowego i zebranych monet?)
        
        Chromosome.chromosomes.append(self)
        
        self.PopulationInit(Chromosome.genesNumber)

    def PopulationInit(self, number):

        for i in range(number):
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

            self.genes.append(position)

    def  CalculateFitness(self):
        pass

"""     def IncrementGenes(self):
        genesNumber=5
        self.PopulationInit(genesNumber) """
