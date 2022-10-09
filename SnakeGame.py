import pygame
import sys
import random

pygame.init()

Colors = {
    "MintyGreen": (40, 210, 180 ),
    "Red": (255, 0, 0 ),
    "LightBlue": (0, 128, 255 ),
    "Black": ( 0, 0, 0 ),
}

Config = {
    "ScreenX": 800,
    "ScreenY": 600,
    "ScreenTitle": "Lexical's Snake Game",
    "background": Colors["MintyGreen"],
    "BlockSize": 10,
    "Speed": 15,
    "Menu": [ "Press N for [N]ew Game", "Press Q for [Q]uit" ],
}

Snake = {
    "X": Config["ScreenX"] / 2,
    "Y": Config["ScreenY"] / 2,
    "Direction": "none",
    "Color": Colors["Red"],
    "Length": 0,
    "Tail": [],
}

def ResetSnake():
    Snake["X"] = Config["ScreenX"] / 2
    Snake["Y"] = Config["ScreenY"] / 2
    Snake["Direction"] = "none"
    Snake["Length"] = 0
    Snake["Tail"] = []

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
    for tail in Snake["Tail"]:
        pygame.draw.rect(screen, Snake["Color"], [ tail[0], tail[1], Config["BlockSize"], Config["BlockSize"]])
    pygame.draw.rect(screen, Food["Color"], [ Food["X"], Food["Y"], Config["BlockSize"], Config["BlockSize"]])
    pygame.display.update()

def main():
    screen = pygame.display.set_mode([Config["ScreenX"], Config["ScreenY"]])
    clock = pygame.time.Clock()
    pygame.display.set_caption(Config["ScreenTitle"])
    pygame.display.update()
    menufont = pygame.font.SysFont("microsoftsansserif", 25)
    bGame = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_n:
                    bGame = True
                    ResetSnake()
                    RandomizeFoodlocation()
                    

        screen.fill(Colors["Black"])
        ypos = 30
        for line in Config["Menu"]:
            msg = menufont.render(line, True, Colors["LightBlue"])
            screen.blit(msg, [30, ypos])
            ypos += ypos
        pygame.display.update()


        while bGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if Snake["Direction"] != "right":
                            Snake["Direction"] = "left"
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if Snake["Direction"] != "left":
                            Snake["Direction"] = "right"
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if Snake["Direction"] != "down":
                            Snake["Direction"] = "up"
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if Snake["Direction"] != "up":
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
                print("you hit a wall")
                bGame = False

            if [Snake["X"], Snake["Y"]] in Snake["Tail"]:
                print("you hit your own tail")
                bGame = False

            if Snake["X"] == Food["X"] and Snake["Y"] == Food["Y"]:
                Snake["Length"] += 1
                Snake["Tail"].append([Food["X"], Food["Y"]])
                RandomizeFoodlocation()

            Snake["Tail"].append([Snake["X"], Snake["Y"]])
            if len(Snake["Tail"]) > Snake["Length"]:
                del Snake["Tail"][0]

            clock.tick(Config["Speed"])


if __name__ == "__main__":
    main()