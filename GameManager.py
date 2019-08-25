import pygame
from pygame.locals import *
from DeltaTime import *
from Position import Position
from PlayerController import PlayerController
from PlayerComputer import PlayerComputer
from EnemyController import EnemyController
from GameObject import GameObject
from Collider import Collider
from Chromosome import Chromosome
from GeneticAlgorithm import geneticAlgorithm

gameObjects=[]
enemies=[]
class GameManager:
    def __init__(self):
        pass

    #grid

    def Start(self):
        pygame.init()
        self.LearnGame()
    """DISPLAY_SURFACE = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('The worlds hardest game GA edition')
        width=40
        height=40
        #global deltaTime
        global enemies
        self.__loadLevel(DISPLAY_SURFACE)
        player=GameObject(Position(0,0), DISPLAY_SURFACE)
        player.AddComponent(PlayerController(100, False))
        player.SetCollider(Collider(width, height, player.position))
         while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            
            #self.PlayGame()
            
            deltaTime.__call__()

            DISPLAY_SURFACE.fill((0,0,0))  
            player.Update(DISPLAY_SURFACE)
            player.Draw(0,0, 255)

            for enemy in enemies:
                enemy.Update(DISPLAY_SURFACE) 
                enemy.collider.OnCollision(enemy, player.collider)

            pygame.display.update() """

    def __loadLevel(self, DISPLAY_SURFACE):
        width=40
        height=40
        global enemies

        enemy=GameObject(Position(100,100),DISPLAY_SURFACE)
        enemy.AddComponent(EnemyController())
        enemy2=GameObject(Position(100,200),DISPLAY_SURFACE)
        enemy2.AddComponent(EnemyController())
        enemy3=GameObject(Position(100,300),DISPLAY_SURFACE)
        enemy3.AddComponent(EnemyController())
        enemy4=GameObject(Position(100,400),DISPLAY_SURFACE)
        enemy4.AddComponent(EnemyController())
        
        enemy.SetCollider(Collider(width, height, enemy.position))
        enemy2.SetCollider(Collider(width, height, enemy2.position))
        enemy3.SetCollider(Collider(width, height, enemy3.position))
        enemy4.SetCollider(Collider(width, height, enemy4.position))

        enemies.append(enemy)
        enemies.append(enemy2)
        enemies.append(enemy3)
        enemies.append(enemy4)


    def LoadPlayers(self, DISPLAY_SURFACE):
        width=40
        lenght=40
        players=[]
        for i in range(geneticAlgorithm.chromosomeNumber):
            newPlayer=GameObject(Position(0,0), DISPLAY_SURFACE)
            newPlayer.SetCollider(Collider(width, lenght, newPlayer.position))
            newPlayer.AddComponent(PlayerComputer())
            players.append(newPlayer)
        
        return players

    def LearnGame(self):
        DISPLAY_SURFACE = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('The worlds hardest game GA edition')
        global enemies
        self.LoadPlayers

        players=self.LoadPlayers(DISPLAY_SURFACE)
        self.__loadLevel(DISPLAY_SURFACE)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime.__call__()
            DISPLAY_SURFACE.fill((0,0,0))  
            for player in players:
                player.Update(DISPLAY_SURFACE)
                player.Draw(0,0, 255)
                for enemy in enemies:
                    enemy.collider.OnCollision(enemy, player.collider)

            for enemy in enemies:
                enemy.Update(DISPLAY_SURFACE) 

            Chromosome.UpdateIterator()
            pygame.display.update()

    def PlayGame(self):
        pass