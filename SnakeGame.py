import pygame
import sys
import random

pygame.init()

Colors = {
    "MintyGreen": (40, 210, 180),
    "Red": (255, 0, 0),
    "LightBlue": (0, 128, 255),
}

Config = {
    "ScreenX": 800,
    "ScreenY": 600,
    "ScreenTitle": "Lexical's Snake Game",
    "background": Colors["MintyGreen"],
    "BlockSize": 10,
    "Speed": 15,
}

Snake = {
    "X": Config["ScreenX"] / 2,
    "Y": Config["ScreenY"] / 2,
    "Direction": "none",
    "Color": Colors["Red"],
}

Food = {
    "X": 0,
    "Y": 0,
    "Color": Colors["LightBlue"],
}

def RandomizeFoodlocation():
    Food["X"] = round(random.randrange(0,Config["ScreenX"] - Config["BlockSize"]), -1)
    Food["Y"] = round(random.randrange(0,Config["ScreenY"] - Config["BlockSize"]), -1)

def DrawGame(screen):
    screen.fill(Config["background"])
    pygame.draw.rect(screen, Snake["Color"], [ Snake["X"], Snake["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.draw.rect(screen, Food["Color"], [ Food["X"], Food["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()

def main():
    screen = pygame.display.set_mode([Config["ScreenX"], Config["ScreenY"]])
    clock = pygame.time.Clock()
    pygame.display.set_caption(Config["ScreenTitle"])
    pygame.display.update()
    RandomizeFoodlocation()

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
                    
        DrawGame(screen)

        if Snake["X"] < 0 or Snake["X"] >= Config["ScreenX"] or Snake["Y"] < 0 or Snake["Y"] >= Config["ScreenY"]:
            break

        if Snake["X"] == Food["X"] and Snake["Y"] == Food["Y"]:
            print("You eat a Delicious Apple")
            RandomizeFoodlocation()

        clock.tick(Config["Speed"])

    print("you hit a wall")

if __name__ == "__main__":
    main()