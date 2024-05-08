import pygame
import random

pygame.init()

#Создаем окно и его параметры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Создаем названия окна, иконку
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/1674667984_grizly-club-p-klipart-tir-2.jpg")
pygame.display.set_icon(icon)

#Создаем целевой объект
target_img = pygame.image.load("img/target.png")
target_wiath = 80
target_heigh = 80

#Рандомный целевой объект для перемещения
target_x = random.randint(0, SCREEN_WIDTH - target_wiath)
target_y = random.randint(0, SCREEN_HEIGHT - target_heigh)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

runing = True
while runing:
    pass

pygame.quit()