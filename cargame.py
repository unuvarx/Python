import pygame, random, time
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((700, 700))

way = pygame.image.load('way.png')
way = pygame.transform.scale(way, (700, 700))
way2 = pygame.image.load('way.png')
way2 = pygame.transform.scale(way2, (700, 700))
redcar = pygame.image.load('redcar.png')
redcar = pygame.transform.scale(redcar, (70, 130))
greencar = pygame.image.load('greencar.png')
greencar = pygame.transform.scale(greencar, (70, 130))
bluecar = pygame.image.load('bluecar.png')
bluecar = pygame.transform.scale(bluecar, (70, 130))
yellowcar = pygame.image.load('yellowcar.png')
yellowcar = pygame.transform.scale(yellowcar, (70, 130))
truck = pygame.image.load('truck.png')
truck = pygame.transform.scale(truck, (90, 170))
transporter = pygame.image.load('transporter.png')
transporter = pygame.transform.scale(transporter, (80, 140))

fire = pygame.image.load('fire.png')
fire = pygame.transform.scale(fire, (150, 150))


red_square = pygame.Surface((50, 102))
red_square.fill((255, 0, 0))   
red_square_rect = pygame.Rect((50, 102), red_square.get_size())

green_square = pygame.Surface((50, 102))
green_square.fill((0, 255, 0))   
green_square_rect = pygame.Rect((50, 102), green_square.get_size())

blue_square = pygame.Surface((50, 102))
blue_square.fill((0, 0, 255))   
blue_square_rect = pygame.Rect((50, 102), blue_square.get_size())

yellow_square = pygame.Surface((50, 102))
yellow_square.fill((255, 255, 0))   
yellow_square_rect = pygame.Rect((50, 102), yellow_square.get_size())

truck_square = pygame.Surface((60, 165))
truck_square.fill((255, 255, 0))   
truck_square_rect = pygame.Rect((60, 165), truck_square.get_size())

transporter_square = pygame.Surface((55, 135))
transporter_square.fill((255, 255, 0))   
transporter_square_rect = pygame.Rect((55, 135), transporter_square.get_size())

wayx = 0 
wayy= 0 
way2x = 0  
way2y = -700

redx = 300
redy = 450
red_square_rect.x = 311
red_square_rect.y = 470

greenx = 150
greeny = 0
green_square_rect.x = 161
green_square_rect.y = 9

bluex = 350
bluey = 0
blue_square_rect.x = 363
blue_square_rect.y = 15

yellowx = 450
yellowy = 0
yellow_square_rect.x = 460
yellow_square_rect.y = 9

truckx = 250
trucky = 10
truck_square_rect.x = 264
truck_square_rect.y = 14

transporterx = 450
transportery = 150
transporter_square_rect.x = 464
transporter_square_rect.y = 155

local_greenx = [150, 250]
local_greeny = [-200, -1200, -2200]
local_blueandyellow_x = [360, 460]
local_blueandyellow_y = [900, 1900, 2900 ,3900]


font = pygame.font.SysFont(None, 25)
run = True
sayac = 0
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    sayac += 1
    screen.blit(red_square, red_square_rect)
    screen.blit(green_square, green_square_rect)
    screen.blit(blue_square, blue_square_rect)
    screen.blit(truck_square, truck_square_rect)
    screen.blit(transporter_square, transporter_square_rect)
    screen.blit(yellow_square, yellow_square_rect)
    screen.blit(way, (wayx, wayy))
    screen.blit(way2, (way2x, way2y))
    screen.blit(redcar, (redx, redy))  
    screen.blit(greencar, (greenx, greeny))
    screen.blit(bluecar, (bluex, bluey))
    screen.blit(yellowcar, (yellowx, yellowy))
    screen.blit(truck, (truckx, trucky))
    screen.blit(transporter, (transporterx, transportery))
    score = font.render("SCORE: {}".format(sayac), True, (255, 0, 0))
    screen.blit(score, (10, 10))
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        red_square_rect = red_square_rect.move(-2, 0)
        redx -= 2
        redcar = pygame.image.load('redcarleft.png')
        if key[pygame.K_UP]:
            red_square_rect = red_square_rect.move(0, -2)
            redy -= 2
            
    elif key[pygame.K_RIGHT]:
        red_square_rect = red_square_rect.move(2, 0)
        redx += 2
        redcar = pygame.image.load('redcarright.png')
        if key[pygame.K_UP]:
            red_square_rect = red_square_rect.move(0, -2)
            redy -= 2 
            
    elif key[pygame.K_UP]:
        red_square_rect = red_square_rect.move(0, -2)
        redy -= 2 
        
    elif key[pygame.K_DOWN]:
        red_square_rect = red_square_rect.move(0, 2)
        redy += 2

    elif key[pygame.K_z]:
        mixer.music.load('bg.ogg')
        mixer.music.play()
    elif key[pygame.K_SPACE]:
            screen.blit(fire, (redx - 55, redy + 64))
            mixer.music.load('ratata.ogg')
            mixer.music.play()
    elif key[pygame.K_x]:
            mixer.music.load('gas.ogg')
            mixer.music.play()    
    elif not key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
        redcar = pygame.image.load('redcar.png')
    
    else:   
        pass  
    wayy += 1
    way2y += 1
    
    greeny += 3
    green_square_rect.y += 3
    
    bluey += -3
    blue_square_rect.y += -3
    
    yellowy += -3
    yellow_square_rect.y += -3
    
    trucky += 3
    truck_square_rect.y += 3
    
    transportery += -3
    transporter_square_rect.y += -3
    if wayy == 700:
        way2y = 0
        wayy = -700
        screen.blit(way, (wayx, wayy))
    elif way2y == 700:
        wayy = 0
        way2y = -700
        screen.blit(way2, (way2x, way2y))
    else:
        pass    
    
    if greeny >= 700:
        greenx = random.choice(local_greenx)
        greeny = random.choice(local_greeny)
        green_square_rect.x = greenx + 11
        green_square_rect.y = greeny + 9
        screen.blit(greencar, (greenx, greeny))
        screen.blit(green_square, green_square_rect)
    elif bluey < -150:
        bluex = random.choice(local_blueandyellow_x)
        bluey = random.choice(local_blueandyellow_y)
        blue_square_rect.x = bluex + 13
        blue_square_rect.y = bluey + 15
        screen.blit(bluecar, (bluex, bluey))
        screen.blit(blue_square, blue_square_rect)
    elif yellowy < -150:
        yellowx = random.choice(local_blueandyellow_x)
        yellowy = random.choice(local_blueandyellow_y)
        yellow_square_rect.x = yellowx + 11
        yellow_square_rect.y = yellowy + 11
        screen.blit(yellowcar, (yellowx, yellowy))
        screen.blit(yellow_square, yellow_square_rect)
    elif trucky > 900:
        truckx = random.choice(local_greenx)
        trucky = random.choice(local_greeny)
        truck_square_rect.x = truckx + 14
        truck_square_rect.y = trucky + 4   
        screen.blit(truck, (truckx, trucky))
        screen.blit(truck_square, truck_square_rect)
    elif transportery < -200:
        transporterx = random.choice(local_blueandyellow_x)
        transportery = random.choice(local_blueandyellow_y)
        transporter_square_rect.x = transporterx + 14
        transporter_square_rect.y = transportery + 5
        screen.blit(transporter, (transporterx, transportery))       
        screen.blit(transporter_square, transporter_square_rect)
    else:
        pass  
    
    if truckx == greenx and trucky == greeny:
        trucky = random.choice(local_greeny)
        greeny = random.choice(local_greeny)
    elif bluex == yellowx and bluey == yellowy:
        bluey = random.choice(local_blueandyellow_y)
        yellowy = random.choice(local_blueandyellow_y)
    elif bluex == transporterx and bluey == transportery:
        bluey = random.choice(local_blueandyellow_y)
        transportery = random.choice(local_blueandyellow_y)
    elif bluex == transporterx and bluey == transportery:
        bluey = random.choice(local_blueandyellow_y)
        transportery = random.choice(local_blueandyellow_y)
    elif yellowx == transporterx and yellowy == transportery:
        yellowy = random.choice(local_blueandyellow_y)
        transportery = random.choice(local_blueandyellow_y)
    else:
        pass        
    
    if red_square_rect.colliderect(green_square_rect) or red_square_rect.colliderect(transporter_square_rect) or red_square_rect.colliderect(yellow_square_rect) or red_square_rect.colliderect(blue_square_rect) or red_square_rect.colliderect(transporter_square_rect) or red_square_rect.colliderect(truck_square_rect):
        mixer.music.load('crash.ogg')
        mixer.music.play()
        time.sleep(4)   
        break
        
    elif redx < 104 or redx > 520:
        mixer.music.load('crash.ogg')
        mixer.music.play()
    pygame.display.update()
    time.sleep(4)

