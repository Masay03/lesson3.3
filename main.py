#Импортируем pygame
import pygame
#Импортируем рандом
import random

#Инициализируем pygame
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
target_img = pygame.image.load("img/target.com.png")
target_wiath = 80
target_heigh = 80

#Рандомный целевой объект для перемещения
target_x = random.randint(0, SCREEN_WIDTH - target_wiath)
target_y = random.randint(0, SCREEN_HEIGHT - target_heigh)

#Цвет целевого объекта
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#Запускаем игру
runing = True
while runing:
    screen.fill(color)#Заливка экрана цветом
    screen.blit(target_img, (target_x, target_y))#Рисуем целевой объект
    pygame.display.update()#Обновляем экран

    #Обработка событий
    for event in pygame.event.get():
        # Если нажали на крестик
        if event.type == pygame.QUIT:
            runing = False
            # Если нажали на мышь
        if event.type == pygame.MOUSEBUTTONDOWN:#Если нажали мышь
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Если мышь попал в целевой объект
            if target_x < mouse_x < target_x + target_wiath and target_y < mouse_y < target_y + target_heigh:
                target_x = random.randint(0, SCREEN_WIDTH - target_wiath)
                target_y = random.randint(0, SCREEN_HEIGHT - target_heigh)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #Обновляем экран
    pygame.display.update()

#Закрываем игру
pygame.quit()