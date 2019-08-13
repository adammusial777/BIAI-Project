import random

class GeneticAlghoritm:
    def __init__(self):
        pass

    def PopulationInit(self):
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
    def __init__(self, genes, rating):
        self.genes=genes #jako lista genów (gen jako pozycja? zestaw genów jako trasa pozycji do celu?)
        self.rating= rating #ocena skuteczności (na podstawie odległości od pola końcowego i zebranych monet?)