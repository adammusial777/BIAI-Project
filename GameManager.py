import pygame
from pygame.locals import *
from DeltaTime import *
from Position import Position
from PlayerController import PlayerController
from EnemyController import EnemyController
from GameObject import GameObject
from Collider import Collider

gameObjects=[]
enemies=[]
class GameManager:
    def __init__(self):
        pass

    #grid

    def Start(self):
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode((500, 500))
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

            #deltaTime=DeltaTime()
            #print(deltaTime) 
            deltaTime.__call__()

            DISPLAY_SURFACE.fill((0,0,0))  
            player.Update(DISPLAY_SURFACE)
            player.Draw(0,0, 255)
            for enemy in enemies:
                enemy.Update(DISPLAY_SURFACE) 
                enemy.collider.OnCollision(enemy, player.collider)

            #player.Update(DISPLAY_SURFACE)
            #enemy.Update(DISPLAY_SURFACE)
            #pygame.draw.rect(DISPLAY_SURFACE,(255,0,0), (player.position.x,player.position.y,width,height))
            #pygame.draw.rect(DISPLAY_SURFACE,(0,255,0), (enemy.position.x,enemy.position.y,width,height))
            pygame.display.update()

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