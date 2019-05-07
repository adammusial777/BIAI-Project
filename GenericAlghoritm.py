import random

def PopulationInit():
    pass

def Mutate():
    pass

def Crossover():
    pass

def Selection():
    pass

def TheBestSelection():
    pass

class Chromosome:
    def __init__(self, genes, rating):
        self.genes=genes #jako lista genów (gen jako pozycja? zestaw genów jako trasa pozycji do celu?)
        self.rating= rating #ocena skuteczności (na podstawie odległości od pola końcowego i zebranych monet?)