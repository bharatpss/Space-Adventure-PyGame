# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:36:36 2019

@author: BHARAT PRATAP
"""

import pygame
import math
import random
from pygame import mixer


# Intialize the pygame
pygame.init()

# Create the Screen 
screen = pygame.display.set_mode((1000,549))

# Background
background = pygame.image.load('back_1.png')
# background scound
background_music = mixer.Sound('background.wav')
background_music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Adventures")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# Player Info
player_img = pygame.image.load('space-shuttle.png')
playerX = 500
playerY = 450
playerX_change = 0
playerY_change = 0

# Alien Info
alien_img = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
number_alien = 8
for i in range(0,8):
        alien_img.append(pygame.image.load('alien.png'))
        alienX.append(random.randint(0,935))
        alienY.append(random.randint(50,200))
        alienX_change.append(3.5)
        alienY_change.append(25)

# Bullet Info
bullet_img = pygame.image.load('bullet_2.png')
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 7
# Ready means can not see bullet it is loading.
# Fire means can see bullet.
bullet_state = 'ready'


# function player
def player(x=playerX, y=playerY):
    
    # drawing player image
    return screen.blit(player_img, (x,y))

# function alien
def alien(x, y, i):
    
    # drawing Alien image
    return screen.blit(alien_img[i], (x,y))

# function bullet fire
def fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    # drawing billet image
    return screen.blit(bullet_img, (x+16, y-30))

# function killing or distance
def kill(alienX, alienY, bulletX, bulletY):
    
    distance = math.sqrt((alienX-bulletX)**2 + (alienY-bulletY)**2)
    if distance < 32:
        return True
    else:
        return False

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

def score_func(x, y):
    score = font.render('Score : '+str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))
#Game Loop
running = True
while running:
    # RGB 
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    #playerX +=0.1
    #playerY -=0.1
    for event in pygame.event.get():
        # For existing from window
        if event.type == pygame.QUIT:
            #running = False
            pygame.quit()
            #quit()
            #break
            
        # Checking Key working or moving of space ship
        if event.type == pygame.KEYDOWN:
            #print('pressed')
            if event.key == pygame.K_LEFT:
                #print('Left key')
                playerX_change = -6
            if event.key == pygame.K_RIGHT:
                #print('Right key')
                playerX_change = 6
            if event.key == pygame.K_UP:
                #print('Right key')
                playerY_change = -6
            if event.key == pygame.K_DOWN:
                #print('Right key')
                playerY_change = 6
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # fire with current Space ship possition
                    bulletX = playerX
                    bulletY = playerY
                    fire(bulletX, bulletY)
                    
                
        if event.type == pygame.KEYUP:
            #print('released')
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                playerX_change = 0
                playerY_change = 0
            
            
    
    playerX += playerX_change
    playerY += playerY_change
    
        
    # Creating Boundary for Gamer
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936
        
    if playerY <= 0:
        playerY = 0
    elif playerY >= 485:
        playerY = 485
        
    
    # Bullet Movement
    if bulletY <=0:
        bulletY = 450
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire(bulletX, bulletY)
        bulletY -= bulletY_change
    
        
    # Alien Movement in screen
    for i in range(number_alien):
        alienX[i] += alienX_change[i]
        if alienX[i] <= 0:
            alienX_change[i] = 3.5
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 936:
            alienX_change[i] = -3.5
            alienY[i] += alienY_change[i]
            
        # Alien Killing
        collision = kill(alienX[i], alienY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bullet_state = 'ready'
            bulletX = playerX
            bulletY = playerY
            score_value += 1
            alienX[i] = random.randint(0,935)
            alienY[i] = random.randint(50,200)
            #print(score)
        
        # alien on screen
        alien(alienX[i], alienY[i], i)
    
    
    
           
    # player on screen
    player(playerX, playerY)
    # Score Display
    score_func(textX, testY)
    # what ever changes are made need to be updated in window
    pygame.display.update()
            
            