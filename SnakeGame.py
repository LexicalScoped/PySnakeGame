import pygame
import sys

pygame.init()

Config = {
    "ScreenX": 800,
    "ScreenY": 600,
    "ScreenTitle": "Lexical's Snake Game",
    "MintyGreen": (40, 210, 180),
    "Red": (255, 0, 0),
    "BlockSize": 10
}

Snake = {
    "X": Config["ScreenX"] / 2,
    "Y": Config["ScreenY"] / 2
}

screen = pygame.display.set_mode([Config["ScreenX"], Config["ScreenY"]])
screen.fill(Config["MintyGreen"])
pygame.display.set_caption(Config["ScreenTitle"])
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Snake["X"] -= Config["BlockSize"]
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Snake["X"] += Config["BlockSize"]
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Snake["Y"] -= Config["BlockSize"]
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Snake["Y"] += Config["BlockSize"]
                
    screen.fill(Config["MintyGreen"])
    pygame.draw.rect(screen, Config["Red"], [ Snake["X"], Snake["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()
