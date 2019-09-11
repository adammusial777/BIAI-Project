from pygame import *
from pygame.locals import *
from DeltaTime import *
from Position import Position
from Player import Player
from PlayerComputer import PlayerComputer
from Enemy import Enemy
from Collider import Collider
from Chromosome import Chromosome
from GeneticAlgorithm import geneticAlgorithm

class GameManager:
    def __init__(self):
        pass

    #grid

    def Start(self):
        pygame.init()
        self.LearnGame()

    def LoadLevel(self):
        width=40
        height=40

        enemy1=Enemy((0,255,0), Position(100,100), Collider(width,height))
        enemy2=Enemy((0,255,0),Position(100,200), Collider(width,height))
        enemy3=Enemy((0,255,0),Position(100,300), Collider(width,height))
        enemy4=Enemy((0,255,0),Position(100,400), Collider(width,height))
        GameManager.enemies.append(enemy1)
        GameManager.enemies.append(enemy2)
        GameManager.enemies.append(enemy3)
        GameManager.enemies.append(enemy4)


    def LoadPlayers(self):
        width=40
        lenght=40
        for i in range(geneticAlgorithm.chromosomeNumber):
            newPlayer=PlayerComputer((0,0,255), Position(0,0), Collider(width, lenght))
            GameManager.players.append(newPlayer)


    

    players=[]
    gameObjects=[]
    enemies=[]
    def LearnGame(self):
        DISPLAY_SURFACE = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('The worlds hardest game GA edition')

        self.LoadPlayers()
        self.LoadLevel()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime.__call__()
            DISPLAY_SURFACE.fill((0,0,0))  


            for player in GameManager.players:
                player.OnUpdate()
                for enemy in GameManager.enemies:
                    if enemy.collider.OnCollision(enemy, player.collider):
                        player.color=(255,0,0)
                        break
                    else:
                        player.color=(0,0,255)
                pygame.draw.rect(DISPLAY_SURFACE,player.color, (player.position.x,player.position.y,40,40))

            for enemy in GameManager.enemies:
                enemy.OnUpdate() 
                pygame.draw.rect(DISPLAY_SURFACE,enemy.color, (enemy.position.x,enemy.position.y,40,40))



            Chromosome.UpdateIterator()
            pygame.display.update()

    def PlayGame(self):
        pass