import pygame
import sys
import random
from enum import Enum

pygame.init()

Colors = {
    "MintyGreen": ( 40, 210, 180 ),
    "Red": ( 255, 0, 0 ),
    "LightBlue": ( 0, 128, 255 ),
    "Black": ( 0, 0, 0 ),
}

class DIRECTIONS(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

class Window():
    def __init__(self, ScreenX = 800, ScreenY = 600):
        self.X = ScreenX
        self.Y = ScreenY
        self.Title = "Lexical's Snake Game"
        self.Screen = pygame.display.set_mode([self.X, self.Y])
        pygame.display.set_caption(self.Title)
        self.Background = Colors["Black"]
        self.FontColor = Colors["LightBlue"]
        self.Menu = [ "Press N for [N]ew Game", "Press Q for [Q]uit" ]
        self.MenuFont = pygame.font.SysFont("microsoftsansserif", 25)
        self.MenuLoop = True
        self.GameState = False
        self.BlockSize = 10
        self.RefreshRate = 15
        self.Update()
        
    def Update(self):
        pygame.display.update()

    def GetBackground(self):
        if self.GameState:
            return Colors["MintyGreen"]
        else:
            return Colors["Black"]

    def MainMenu(self):
        self.Screen.fill(self.GetBackground())
        ypos = 30
        for line in self.Menu:
            msg = self.MenuFont.render(line, True, self.FontColor)
            self.Screen.blit(msg, [30, ypos])
            ypos += ypos
        self.Update()
    
    def DrawGame(self, snake, food):
        self.Screen.fill(self.GetBackground())
        pygame.draw.rect(self.Screen, snake.Color, [ snake.X, snake.Y, self.BlockSize, self.BlockSize])
        for tail in snake.Tail:
            pygame.draw.rect(self.Screen, snake.Color, [ tail[0], tail[1], self.BlockSize, self.BlockSize])
        pygame.draw.rect(self.Screen, food.Color, [ food.X, food.Y, self.BlockSize, self.BlockSize])
        pygame.display.update()
    
    def Quit(self):
        sys.exit()

class Snake():
    def __init__(self, ScreenX, ScreenY):
        self.X = ScreenX / 2
        self.Y = ScreenY / 2
        self.Direction = DIRECTIONS.NONE
        self.Color = Colors["Red"]
        self.Length = 0
        self.Tail = []

    def Move(self, Blocksize):
        if self.Direction == DIRECTIONS.LEFT:
            self.X -= Blocksize
        if self.Direction == DIRECTIONS.RIGHT:
            self.X += Blocksize
        if self.Direction == DIRECTIONS.UP:
            self.Y -= Blocksize
        if self.Direction == DIRECTIONS.DOWN:
            self.Y += Blocksize

class Food():
    def __init__(self, display):
        self.X = round(random.randrange(0,display.X - display.BlockSize), -1)
        self.Y = round(random.randrange(0,display.Y - display.BlockSize), -1)
        self.Color = Colors["LightBlue"]




def main():
    display = Window()
    clock = pygame.time.Clock()

    while display.MenuLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    display.Quit()
                if event.key == pygame.K_n:
                    display.GameState = True
                    snake = Snake(display.X, display.Y)
                    food = Food(display)
                    
        display.MainMenu()

        while display.GameState:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    display.Quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if snake.Direction != DIRECTIONS.RIGHT:
                            snake.Direction = DIRECTIONS.LEFT
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if snake.Direction != DIRECTIONS.LEFT:
                            snake.Direction = DIRECTIONS.RIGHT
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if snake.Direction != DIRECTIONS.DOWN:
                            snake.Direction = DIRECTIONS.UP
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if snake.Direction != DIRECTIONS.UP:
                            snake.Direction = DIRECTIONS.DOWN   

            snake.Move(display.BlockSize)
                        
            display.DrawGame(snake, food)

            if snake.X < 0 or snake.X >= display.X or snake.Y < 0 or snake.Y >= display.Y:
                print("you hit a wall")
                display.GameState = False

            if [snake.X, snake.Y] in snake.Tail:
                print("you hit your own tail")
                display.GameState = False

            if snake.X == food.X and snake.Y == food.Y:
                snake.Length += 1
                del food
                food = Food(display)

            snake.Tail.append([snake.X, snake.Y])
            if len(snake.Tail) > snake.Length:
                del snake.Tail[0]

            if not display.GameState:
                del food
                del snake

            clock.tick(display.RefreshRate)


if __name__ == "__main__":
    main()