import pygame
import sys
import random

pygame.init()

Colors = {
    "MintyGreen": ( 40, 210, 180 ),
    "Red": ( 255, 0, 0 ),
    "LightBlue": ( 0, 128, 255 ),
    "Black": ( 0, 0, 0 ),
}

Config = {
    "ScreenX": 800,
    "ScreenY": 600,
    "background": Colors["MintyGreen"],
    "BlockSize": 10,
    "Speed": 15,
}

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
        self.Update()
        
    def Update(self):
        pygame.display.update()

    def ChangeBackground(self, color):
        self.Background = color

    def MainMenu(self):
        self.ChangeBackground(Colors["Black"])
        self.Screen.fill(self.Background)
        ypos = 30
        for line in self.Menu:
            msg = self.MenuFont.render(line, True, self.FontColor)
            self.Screen.blit(msg, [30, ypos])
            ypos += ypos
        self.Update()
    
    def Quit(self):
        sys.exit()

class Snake():
    def __init__(self, ScreenX, ScreenY):
        self.X = ScreenX / 2
        self.Y = ScreenY / 2
        self.Direction = "none"
        self.Color = Colors["Red"]
        self.Length = 0
        self.Tail = []

class Food():
    def __init__(self, ScreenX, ScreenY):
        self.X = round(random.randrange(0,ScreenX - Config["BlockSize"]), -1)
        self.Y = round(random.randrange(0,ScreenY - Config["BlockSize"]), -1)
        self.Color = Colors["LightBlue"]


def DrawGame(screen, snake, food):
    screen.fill(Config["background"])
    pygame.draw.rect(screen, snake.Color, [ snake.X, snake.Y, Config["BlockSize"], Config["BlockSize"]])
    for tail in snake.Tail:
        pygame.draw.rect(screen, snake.Color, [ tail[0], tail[1], Config["BlockSize"], Config["BlockSize"]])
    pygame.draw.rect(screen, food.Color, [ food.X, food.Y, Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()

def main():
    display = Window()
    clock = pygame.time.Clock()
    bGame = False

    while display.MenuLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display.Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    display.Quit()
                if event.key == pygame.K_n:
                    bGame = True
                    snake = Snake(display.X, display.Y)
                    food = Food(display.X, display.Y)
                    
        display.MainMenu()

        while bGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    display.Quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if snake.Direction != "right":
                            snake.Direction = "left"
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if snake.Direction != "left":
                            snake.Direction = "right"
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if snake.Direction != "down":
                            snake.Direction = "up"
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if snake.Direction != "up":
                            snake.Direction = "down"   

            if snake.Direction == "left":
                snake.X -= Config["BlockSize"]
            if snake.Direction == "right":
                snake.X += Config["BlockSize"]
            if snake.Direction == "up":
                snake.Y -= Config["BlockSize"]
            if snake.Direction == "down":
                snake.Y += Config["BlockSize"]
                        
            DrawGame(display.Screen, snake, food)

            if snake.X < 0 or snake.X >= Config["ScreenX"] or snake.Y < 0 or snake.Y >= Config["ScreenY"]:
                print("you hit a wall")
                bGame = False

            if [snake.X, snake.Y] in snake.Tail:
                print("you hit your own tail")
                bGame = False

            if snake.X == food.X and snake.Y == food.Y:
                snake.Length += 1
                del food
                food = Food(display.X, display.Y)

            snake.Tail.append([snake.X, snake.Y])
            if len(snake.Tail) > snake.Length:
                del snake.Tail[0]

            if not bGame:
                del food
                del snake

            clock.tick(Config["Speed"])


if __name__ == "__main__":
    main()