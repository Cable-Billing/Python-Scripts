from random import randint
import pygame
pygame.init()

# Window
window_width = 500
window_height = 500
pygame.display.set_caption("Space Invaders")
window = pygame.display.set_mode((window_width, window_height))

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 18)

# Bullet information
bullet_width = 2
bullet_height = 20
player_bullets = []
enemy_bullets = []

# Player information
player_colour = (66, 135, 245)
player_width = 35
player_height = 35
player = pygame.Rect(
    (window_width / 2) - (player_width / 2),
    window_height - 50,
    player_width,
    player_height
)
velocity = 1

# Boundaries
player_boundary_x = window_width - player_width
player_boundary_y = window_height - player_height

# Cooldown
cooldown = 200 # Milliseconds
last = pygame.time.get_ticks()

# Enemies
enemy_colour = (235, 64, 52)
enemies = []
enemy_x = 50
for i in range(8):
    enemies.append(
        pygame.Rect(
            enemy_x + 10, 50, 30, 30
        )
    )
    enemy_x += 50

running = True
while running:
    pygame.time.delay(1)
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get all the keys that were pressed
    keys = pygame.key.get_pressed()

    # Move the player left or right
    if keys[pygame.K_LEFT]:
        player.x -= velocity
    elif keys[pygame.K_RIGHT]:
        player.x += velocity

    # Player shoot
    if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and ((now - last) >= cooldown):
        last = now
        player_bullets.append(
            pygame.Rect(
                player.x + (player_width / 2),
                player.y + (player_height / 2) - 10,
                bullet_width,
                bullet_height
            )
        )

    # Restrict player to the window
    if player.x < 0:
        player.x = 0
    elif player.x > player_boundary_x:
        player.x = player_boundary_x

    # Fill the background
    window.fill((48, 50, 54))

    # Draw player bullets
    for bullet in player_bullets:
        pygame.draw.rect(window, player_colour, bullet)
        bullet[1] -= 1
        if bullet[1] < 0 - bullet_height:
            player_bullets.remove(bullet)

    # Draw enemy bullets
    for bullet in enemy_bullets:
        pygame.draw.rect(window, enemy_colour, bullet)
        bullet[1] += 1
        if bullet[1] > window_height:
            enemy_bullets.remove(bullet)

        if player.colliderect(bullet):
            running = False

    # Draw Enemies
    for enemy in enemies:
        pygame.draw.rect(window, enemy_colour, enemy)
        # Enemy shoot
        if randint(1, 2001) == 1:
            enemy_bullets.append(
                pygame.Rect(
                    enemy.x + 15, enemy.y + 15, bullet_width, bullet_height
                )
            )

        for bullet in player_bullets:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                player_bullets.remove(bullet)
                score += 10

    # Score Text
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.x = 10
    textRect.y = 10
    window.blit(text, textRect)

    # Draw the player
    pygame.draw.rect(window, player_colour, player)

    # Update the display
    pygame.display.update()

pygame.quit()
