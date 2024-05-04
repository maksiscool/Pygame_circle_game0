import pygame 
import math
from random import randint
from time import time
from random import choice
pygame.init()
pygame.display.set_caption('Space Invaders Rip-off')
class Player():
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  
        self.rotated_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.width = width 
        self.height = height 
        self.x = x
        self.y = y
    def move(self, angle, length):
        self.x += length * math.sin(math.radians(angle))
        self.y -= length * math.cos(math.radians(angle))
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
        self.rotated_image = pygame.transform.rotate(self.image, -angle-90)
class PlayerBullet():
    def __init__(self, dir, spawnposx, spawnposy):
        self.height = 10
        self.width = 10
        self.x = spawnposx - 5
        self.y = spawnposy - 5
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.direction = dir
    def move(self, length):
        self.x += length * math.sin(math.radians(self.direction))
        self.y -= length * math.cos(math.radians(self.direction))
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
class EnemyBullet():
    def __init__(self, dir, spawnposx, spawnposy):
        self.height = 20
        self.width = 20
        self.x = spawnposx
        self.y = spawnposy
        self.rect = pygame.rect.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)
        self.direction = dir
    def move(self, length):
        self.x += length * math.sin(math.radians(self.direction))
        self.y -= length * math.cos(math.radians(self.direction))
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
class Alien():
    def __init__(self,x,y,width,height,image):
        self.health = 20
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.width = width 
        self.height = height 
    def randombulletattack(self):
        for i in range(10):
            enemybulletlist.append(EnemyBullet(randint(0, 359), self.rect.x + self.width/2, self.rect.y + self.height/2))


    




window = pygame.display.set_mode((750, 750))


player = Player(375, 630, 40, 48, 'player.png')
dir = None
cangle = -90
start = time() - 1

alien = Alien(336, 310.5, 78, 66, 'enemy.png')
enemybulletlist = []
playerbulletlist = []

clock = pygame.time.Clock()
done = False
frame = 0
difficulty = 1
while not done:
    frame += 1
    window.fill((0,0,0))
    if frame % int((180/difficulty)+1) == 0:
        alien.randombulletattack()
        difficulty += 0.05
    window.blit(pygame.font.SysFont('Arial', 20).render(f'Health: {alien.health}', False, 'white'), (336, 280.5))

    # circle = pygame.draw.circle(window, (255,255,255), (375, 343.5), 286.5, 1)

    window.blit(player.rotated_image, (player.rect.x - player.rect.width/2, player.rect.y-player.rect.height/2))  
    window.blit(alien.image, (alien.rect.x, alien.rect.y))

    for i in enemybulletlist:
        i.move(5)
        pygame.draw.rect(window, (255,255,255), i)
        if player.rect.colliderect(i):
            done = True
        if not window.get_rect().colliderect(i):
            enemybulletlist.remove(i)
    for i in playerbulletlist:
        i.move(5)
        pygame.draw.rect(window, (0,255,0), i)
        if alien.rect.colliderect(i):
            playerbulletlist.remove(i)
            alien.health -= 1
        if not window.get_rect().colliderect(i):
            playerbulletlist.remove(i)
    if dir:
        player.move(cangle, dir * 5)
        cangle += dir
    if alien.health < 1:
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if dir == 1:
                    dir = -1
                elif dir == -1:
                    dir = 1
                else:
                    dir = 1
            if event.button == 1:

                if time() - start > 1:
                    start = time()
                    playerbulletlist.append(PlayerBullet(cangle+90, player.rect.x, player.rect.y))


    clock.tick(60)
    pygame.display.update()
if alien.health < 1:
    start = time()
    letters = list('ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890')
    while time() - start < 5:
        pygame.display.set_caption(f'{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}    YOU WON!    {choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}{choice(letters)}')
pygame.quit()
