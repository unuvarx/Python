import pygame, random
pygame.init()
screen = pygame.display.set_mode((700, 700))

way = pygame.image.load('way.png')
way = pygame.transform.scale(way, (700, 700))
way2 = pygame.image.load('way.png')
way2 = pygame.transform.scale(way2, (700, 700))
redcar = pygame.image.load('redcar.png')
redcar = pygame.transform.scale(redcar, (140, 130))
greencar = pygame.image.load('greencar.png')
greencar= pygame.transform.scale(greencar, (110, 130))
bluecar = pygame.image.load('bluecar.png')
bluecar = pygame.transform.scale(bluecar, (85, 130))
yellowcar = pygame.image.load('yellowcar.png')
yellowcar = pygame.transform.scale(yellowcar, (140, 120))



locationx = [450, 350, 250, 150]
locationy = [-150, -300, -450]
redx = 150
redy = 500

greenx = 150
greeny = 30

bluex = 250
bluey = 30

yellowx = 350
yellowy = 30

wayx = 0
wayy = 0

way2x = 0
way2y = -700
run = True 
while run:
    screen.fill((255, 255, 255))
    screen.blit(way, (wayx, wayy))
    screen.blit(way2, (way2x, way2y))
    screen.blit(redcar, (redx, redy))
    screen.blit(greencar, (greenx, greeny))
    screen.blit(bluecar, (bluex, bluey))
    screen.blit(yellowcar, (yellowx, yellowy))
    
    wayy += 2
    way2y += 2
    bluey += 1
    greeny += 1
    yellowy += 1
    if greeny >= 700:
        greeny = -150
        greenx = random.choice(locationx)
        greeny = random.choice(locationy)    
    elif bluey >= 700:
        bluey = -150
        bluex = random.choice(locationx)
        bluey = random.choice(locationy)
    elif yellowy >= 700:
        yellowy = -150
        yellowx = random.choice(locationx)
        yellowy = random.choice(locationy)
    elif greenx == bluex or greenx == yellowx or yellowx == bluex:
        greenx = random.choice(locationx)
        yellowx = random.choice(locationx)
        bluex = random.choice(locationx)
        
    
    
    while wayy >= 700 or way2y >= 700:
        wayy = 0
        way2y = -700
        screen.blit(way, (wayx, wayy))
        screen.blit(way2, (way2x, way2y))
        screen.blit(redcar, (redx, redy))
        screen.blit(greencar, (greenx, greeny))
        screen.blit(bluecar, (bluex, bluey))
        
        
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        redx -= 1
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        redx += 1
    elif pygame.key.get_pressed()[pygame.K_UP]:
        redy -= 1
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        redy += 1
    pygame.display.update()
