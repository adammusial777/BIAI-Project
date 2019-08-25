import random
import Position as Pos

class Chromosome:
    genesIterator=0
    genesNumber=100

    @staticmethod
    def UpdateIterator():
        Chromosome.genesIterator+=1
        if Chromosome.genesIterator == Chromosome.genesNumber:
            Chromosome.genesIterator=0

    def __init__(self):
        self.genes=[] #jako lista genów (gen jako pozycja? zestaw genów jako trasa pozycji do celu?)
        self.rating= 0.0 #ocena skuteczności (na podstawie odległości od pola końcowego i zebranych monet?)
        self.PopulationInit(Chromosome.genesNumber)

    def PopulationInit(self, number):
        
        for i in range(number):
            position=Pos.Position(0,0)
            randomValX=random.random()
            #print(randomValX)
            if randomValX<0.4:
                position.x=-1
            elif randomValX<0.6:
                position.x=0
            else:
                position.x=1

            randomValY=random.random()
            if randomValY<0.4:
                position.y=-1
            elif randomValY<0.6:
                 position.y=0
            else:
                position.y=1

            self.genes.append(position)

"""     def IncrementGenes(self):
        genesNumber=5
        self.PopulationInit(genesNumber) """