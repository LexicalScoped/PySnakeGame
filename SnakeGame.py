import pygame
import sys

pygame.init()

Config = {
    "ScreenX": 800,
    "ScreenY": 600,
    "ScreenTitle": "Lexical's Snake Game",
    "MintyGreen": (40, 210, 180),
    "Red": (255, 0, 0),
    "BlockSize": 10,
    "Speed": 20,
}

Snake = {
    "X": Config["ScreenX"] / 2,
    "Y": Config["ScreenY"] / 2,
    "Direction": "none"
}

screen = pygame.display.set_mode([Config["ScreenX"], Config["ScreenY"]])
clock = pygame.time.Clock()
pygame.display.set_caption(Config["ScreenTitle"])
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Snake["Direction"] = "left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Snake["Direction"] = "right"
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Snake["Direction"] = "up"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Snake["Direction"] = "down"    

    if Snake["Direction"] == "left":
        Snake["X"] -= Config["BlockSize"]
    if Snake["Direction"] == "right":
        Snake["X"] += Config["BlockSize"]
    if Snake["Direction"] == "up":
        Snake["Y"] -= Config["BlockSize"]
    if Snake["Direction"] == "down":
        Snake["Y"] += Config["BlockSize"]
                
    screen.fill(Config["MintyGreen"])
    pygame.draw.rect(screen, Config["Red"], [ Snake["X"], Snake["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()

    if Snake["X"] < 0 or Snake["X"] >= Config["ScreenX"] or Snake["Y"] < 0 or Snake["Y"] >= Config["ScreenY"]:
        break

    clock.tick(Config["Speed"])

print("you hit a wall")