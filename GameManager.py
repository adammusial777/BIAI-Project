import pygame
from pygame.locals import *
from DeltaTime import DeltaTime
from Player import Player
from PlayerComputer import PlayerComputer
from GeneticAlgorithm import GeneticAlgorithm
from Enemy import Enemy
from Collider import Collider
from Chromosome import Chromosome
from GeneticAlgorithm import geneticAlgorithm
from BoardReader import BoardReader
from TargetArea import TargetArea

import time


class GameManager:

    players = []
    gameObjects = []
    enemies = []
    board = []
    collidingObjects = []
    deadPlayers=[]
    tileSize = 40

    # grid

    def Start(self):
        pygame.init()
        self.LearnGame1()
        #self.PlayGame()

    def LoadLevel(self):
        # edit
        boardReader = BoardReader()
        GameManager.board = boardReader.ReadFile("Boards/Board1.txt")

    def LoadEnemies(self):
        GameManager.enemies.clear()
        enemyColliderWidth = 12
        enemyColliderHeight = 12

        enemy1 = Enemy((0, 0, 255), 5.5 * GameManager.tileSize - enemyColliderWidth, 5.5 * GameManager.tileSize, enemyColliderWidth,
                       enemyColliderHeight, False)
        enemy2 = Enemy((0, 0, 255), 14.5 * GameManager.tileSize + enemyColliderWidth, 6.5 * GameManager.tileSize, enemyColliderWidth,
                       enemyColliderHeight, False)
        enemy3 = Enemy((0, 0, 255), 5.5 * GameManager.tileSize - enemyColliderWidth, 7.5 * GameManager.tileSize, enemyColliderWidth,
                       enemyColliderHeight, False)
        enemy4 = Enemy((0, 0, 255), 14.5 * GameManager.tileSize + enemyColliderWidth, 8.5 * GameManager.tileSize, enemyColliderWidth,
                       enemyColliderHeight, False)
        GameManager.enemies.append(enemy1)
        GameManager.enemies.append(enemy2)
        GameManager.enemies.append(enemy3)
        GameManager.enemies.append(enemy4)

    def LoadPlayers(self):
        playerColliderWidth = 25
        playerColliderHeight = 25

        newPlayer = Player((255, 0, 0), 2.5 * GameManager.tileSize - playerColliderWidth/2, 5.5 * GameManager.tileSize - playerColliderHeight/2,
                           playerColliderWidth, playerColliderHeight)
        GameManager.players.append(newPlayer)
        # for i in range(geneticAlgorithm.chromosomeNumber):
        #     newPlayer = PlayerComputer((0, 0, 255), Position(
        #         0, 0), Collider(playerColliderWidth, playerColliderHeight), surface)
        #     GameManager.players.append(newPlayer)

    def LoadPlayersComputer(self):
        playerColliderWidth = 25
        playerColliderHeight = 25
        GameManager.players.clear()
        for i in range(geneticAlgorithm.chromosomeNumber):
            newPlayer = PlayerComputer((255, 0, 0), 2.5 * GameManager.tileSize - playerColliderWidth/2, 5.5 * GameManager.tileSize - playerColliderHeight/2,
                playerColliderWidth, playerColliderHeight)
            GameManager.players.append(newPlayer)

    def LoadChromosomes(self):
        for i in range(geneticAlgorithm.chromosomeNumber):
            GameManager.players[i].chromosome= Chromosome.chromosomes[i]

    def LoadTargetAreas(self):
        width = 25
        height = 25
        targetStart=TargetArea((200, 20, 200), 2.5 * GameManager.tileSize - width/2, 5.5 * GameManager.tileSize - height/2,width, height)
        target2=TargetArea((200, 20, 200), 5 * GameManager.tileSize - width/2, 9.5 * GameManager.tileSize - height/2,width, height)
        target3=TargetArea((200, 20, 200), 15 * GameManager.tileSize - width/2, 4.7 * GameManager.tileSize - height/2,width, height)
        targetEnd=TargetArea((200, 20, 200), 18 * GameManager.tileSize - width/2, 5 * GameManager.tileSize - height/2,width, height)
        Chromosome.targetAreas.append(targetStart)
        Chromosome.targetAreas.append(target2)
        Chromosome.targetAreas.append(target3)
        Chromosome.targetAreas.append(targetEnd)

    def LearnGame1(self):
        DISPLAY_SURFACE = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('The worlds hardest game GA edition')

        self.LoadPlayersComputer()
        self.LoadLevel()
        self.LoadEnemies()
        Chromosome.CreateSetOfChromosomes()
        self.LoadChromosomes()
        self.LoadTargetAreas()
        GA=GeneticAlgorithm()

        gameIsRunning = True
        while gameIsRunning:
            for event in pygame.event.get():
                if event.type == QUIT:
                    gameIsRunning = False
            DeltaTime.GetDeltaTime()
            DISPLAY_SURFACE.fill((0, 0, 0))
            #time.sleep(0.5)
            for tile in GameManager.board:
                tile.Render(DISPLAY_SURFACE)

            for player in GameManager.players:
                prevPos=(player.rect.x,player.rect.y)
                player.previousPosition=prevPos
                player.OnUpdate(GameManager.collidingObjects)
                if player.chromosome.killed:
                    GameManager.deadPlayers.append(player)
                    player.chromosome.playerEndRect=player.rect
                player.ResolveCollisions(GameManager.collidingObjects)
                player.Render(DISPLAY_SURFACE)

            for enemy in GameManager.enemies:
                enemy.OnUpdate()
                enemy.Render(DISPLAY_SURFACE)

            for dead in GameManager.deadPlayers:
                GameManager.players.remove(dead)
            GameManager.deadPlayers.clear()


            for tar in Chromosome.targetAreas:
                tar.Render(DISPLAY_SURFACE)



            Chromosome.UpdateIterator()
            if Chromosome.IsEndOfGeneration():
                for player in GameManager.players:
                    player.chromosome.playerEndRect=player.rect
                GA.Update()
                self.LoadEnemies()
                self.LoadPlayersComputer()
                self.LoadChromosomes()

            pygame.display.update()
            DeltaTime.clock.tick(DeltaTime.framerate)


    # def LearnGame(self):
    #     DISPLAY_SURFACE = pygame.display.set_mode((800, 600))
    #     pygame.display.set_caption('The worlds hardest game GA edition')

    #     self.LoadPlayers(DISPLAY_SURFACE)
    #     self.LoadLevel(DISPLAY_SURFACE)

    #     gameIsRunning = True
    #     while gameIsRunning:
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 gameIsRunning = False

    #         DeltaTime.GetDeltaTime()
    #         DISPLAY_SURFACE.fill((0, 0, 0))

    #         for tile in GameManager.board:
    #             tile.Render(DISPLAY_SURFACE)

    #         for player in GameManager.players:
    #             player.OnUpdate()
    #             for enemy in GameManager.enemies:
    #                 if enemy.collider.OnCollision(enemy, player.collider):
    #                     player.color = (255, 0, 0)
    #                     break
    #                 else:
    #                     player.color = (0, 0, 255)
    #             player.Render(DISPLAY_SURFACE)

    #         for enemy in GameManager.enemies:
    #             enemy.OnUpdate()
    #             enemy.Render(DISPLAY_SURFACE)

    #         Chromosome.UpdateIterator()
    #         pygame.display.update()

    def PlayGame(self):
        DISPLAY_SURFACE = pygame.display.set_mode((798, 600))
        pygame.display.set_caption('The worlds hardest game GA edition')

        self.LoadPlayers()
        self.LoadLevel()
        self.LoadEnemies()

        gameIsRunning = True
        while gameIsRunning:
            for event in pygame.event.get():
                if event.type == QUIT:
                    gameIsRunning = False

            DeltaTime.GetDeltaTime()
            DISPLAY_SURFACE.fill((0, 0, 0))

            for tile in GameManager.board:
                tile.Render(DISPLAY_SURFACE)

            for player in GameManager.players:
                prevPos=(player.rect.x,player.rect.y)
                player.previousPosition=prevPos
                player.OnUpdate(GameManager.collidingObjects)
                #player.ResolveCollisions(GameManager.collidingObjects)

                # for enemy in GameManager.enemies:
                #     if enemy.collider.OnCollision(enemy, player.collider):
                #         player.color = (255, 0, 0)
                #         break
                #     else:
                #         player.color = (0, 0, 255)
                player.Render(DISPLAY_SURFACE)

            for enemy in GameManager.enemies:
                enemy.OnUpdate()
                enemy.Render(DISPLAY_SURFACE)

            Chromosome.UpdateIterator()
            pygame.display.update()
            DeltaTime.clock.tick(DeltaTime.framerate)
