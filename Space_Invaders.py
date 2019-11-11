import pygame
pygame.init()

# Window
window_width = 500
window_height = 500
pygame.display.set_caption("Caleb\'s Game")
win = pygame.display.set_mode((window_width, window_height))

# Player information
player_colour = (66, 135, 245)
player_width = 40
player_height = 40
player_x = (window_width / 2) - (player_width / 2)
player_y = window_height - 50
velocity = 1

# Boundaries
player_boundry_x = window_width - player_width
player_boundry_y = window_height - player_height

run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= velocity
    if keys[pygame.K_RIGHT]:
        player_x += velocity

    if player_x < 0:
        player_x = 0
    elif player_x > player_boundry_x:
        player_x = player_boundry_x

    # Update the display
    win.fill((48, 50, 54))
    pygame.draw.rect(win, player_colour, (player_x, player_y, player_width, player_height))
    pygame.display.update()

pygame.quit()
