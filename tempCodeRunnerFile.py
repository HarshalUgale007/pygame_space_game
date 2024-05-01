import pygame
import random
import time

pygame.font.init()

WIDTH, HEIGHT = 1000, 800

# Create the Pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Station")

BG = pygame.transform.scale(pygame.image.load("pexels.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

PLAYER_VEL = 5
FIREBALL_WIDTH = 32
FIREBALL_HEIGHT = 32
FIREBALL_VEL = 3

FONT = pygame.font.SysFont("roman", 30)

def draw(player, elapsed_time, fireballs):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    WIN.blit(player, (player.x, player.y))

    for fireball in fireballs:
        WIN.blit(fireball["image"], (fireball["x"], fireball["y"]))

    pygame.display.update()

def main():
    run = True

    player_img = pygame.image.load("spaceship.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    start_add_increment = 2000
    fireball_count = 0

    fireballs = []

    while run:
        fireball_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if fireball_count > start_add_increment:
            for _ in range(3):
                fireball_x = random.randint(0, WIDTH - FIREBALL_WIDTH)
                fireballs.append({"x": fireball_x, "y": -FIREBALL_HEIGHT, "image": pygame.image.load("fire-ball.png").convert_alpha()})

            start_add_increment = max(200, start_add_increment - 10)
            fireball_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL

        for fireball in fireballs[:]:
            fireball["y"] += FIREBALL_VEL
            if fireball["y"] > HEIGHT:
                fireballs.remove(fireball)
            elif player.colliderect(pygame.Rect(fireball["x"], fireball["y"], FIREBALL_WIDTH, FIREBALL_HEIGHT)):
                run = False
                break

        draw(player_img, elapsed_time, fireballs)

    pygame.quit()

if __name__ == "__main__":
    main()