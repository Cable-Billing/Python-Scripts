import pygame
pygame.init()

# Window
window_width = 500
window_height = 500
pygame.display.set_caption("Space Invaders")
win = pygame.display.set_mode((window_width, window_height))

# Bullet information
bullet_colour = (255, 136, 0)
bullet_width = 2
bullet_height = 20
bullets = []

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

# Cooldown
cooldown = 500 # Milliseconds
last = pygame.time.get_ticks()

run = True
while run:
    pygame.time.delay(1)
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get all the keys that were pressed
    keys = pygame.key.get_pressed()

    # Move the player left or right
    if keys[pygame.K_LEFT]:
        player_x -= velocity
    elif keys[pygame.K_RIGHT]:
        player_x += velocity

    # Fire
    if keys[pygame.K_UP] and (now - last) >= cooldown:
        last = now
        bullets.append(
            [
                player_x + (player_width / 2),
                player_y + (player_height / 2) - 10,
                bullet_width,
                bullet_height
            ]
        )

    # Restrict player to the window
    if player_x < 0:
        player_x = 0
    elif player_x > player_boundry_x:
        player_x = player_boundry_x

    # Fill the background
    win.fill((48, 50, 54))

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(win, bullet_colour, bullet)
        bullet[1] -= 1
        if bullet[1] < 0 - bullet_height:
            bullets.remove(bullet)

    # Draw the player
    pygame.draw.rect(win, player_colour, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.update()

pygame.quit()
