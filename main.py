import pygame
import random

# Инициализируем pygame
pygame.init()

# Создаем окно и его параметры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Создаем названия окна, иконку
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/1674667984_grizly-club-p-klipart-tir-2.jpg")
pygame.display.set_icon(icon)

# Создаем целевой объект
target_img = pygame.image.load("img/target.com.png")  # Проверьте правильность пути к файлу
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 0.2
target_speed_y = 0.2

# Цвет фона и счет
background_color = (0, 0, 0)  # Черный цвет
score = 0

# Шрифт для отображения счета
font = pygame.font.Font(None, 36)

# Запускаем игру
running = True
while running:
    screen.fill(background_color)  # Заливка экрана цветом

    # Обновляем позицию цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверяем, не выходит ли цель за пределы экрана
    if target_x + target_width > SCREEN_WIDTH or target_x < 0:
        target_speed_x *= -1
    if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
        target_speed_y *= -1

    # Рисуем целевой объект
    screen.blit(target_img, (target_x, target_y))

    # Отображаем счет
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # Белый цвет текста
    screen.blit(score_text, (10, 10))

    pygame.display.update()  # Обновляем экран

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Если мышь попала в целевой объект
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                score += 1  # Увеличиваем счет
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Меняем цвет фона на случайный
                background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Закрываем игру
pygame.quit()