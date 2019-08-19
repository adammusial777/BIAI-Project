import random
import Position as Pos

class GeneticAlghoritm:
    def __init__(self):
        pass

    def Mutate(self):
        pass

    def Crossover(self):
        pass

    def Selection(self):
        pass

    def TheBestSelection(self):
        pass

class Chromosome:
    def __init__(self):
        self.genes=[] #jako lista genów (gen jako pozycja? zestaw genów jako trasa pozycji do celu?)
        self.genesNumber=20
        self.rating= 0.0 #ocena skuteczności (na podstawie odległości od pola końcowego i zebranych monet?)
        self.PopulationInit(self.genesNumber)

    def PopulationInit(self, number):
        position=Pos.Position(0,0)
        for i in range(number):
            randomValX=random.random()
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

    def IncrementGenes(self):
        genesNumber=5
        self.PopulationInit(genesNumber)