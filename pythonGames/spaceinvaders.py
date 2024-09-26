import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPACESHIP_WIDTH = 64
SPACESHIP_HEIGHT = 64
ALIEN_WIDTH = 64
ALIEN_HEIGHT = 64
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_SPEED = 5
SPACESHIP_SPEED = 15
ALIEN_SPEED = 5
ALIEN_DROP = 10
ALIEN_DELAY = 1  # Delay between alien spawns (in seconds)
ALIEN_INCREASE_INTERVAL = 10  # Time in seconds to increase aliens
FONT_SIZE = 36
MAX_ALIEN_ROWS = 4
MAX_ALIEN_COLS = 4
MIN_ALIEN_ROWS = 2
MIN_ALIEN_COLS = 2
INITIAL_ALIEN_COUNT = 4
MAX_ALIEN_SPEED = 3  # Maximum speed for aliens
SPEED_INCREMENT_INTERVAL = 20  # Time to increase speed
HIGH_SCORE_FILE = 'high_score.txt'

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
spaceship_img = pygame.image.load('spaceship.png')
spaceship_img = pygame.transform.scale(spaceship_img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
alien_img = pygame.image.load('alien.png')
alien_img = pygame.transform.scale(alien_img, (ALIEN_WIDTH, ALIEN_HEIGHT))
bullet_img = pygame.image.load('bullet.png')
bullet_img = pygame.transform.scale(bullet_img, (BULLET_WIDTH, BULLET_HEIGHT))

# Function to load high score
def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

# Function to save high score
def save_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as file:
        file.write(str(score))

# Function to draw spaceship
def draw_spaceship(x, y):
    screen.blit(spaceship_img, (x, y))

# Function to draw alien
def draw_alien(x, y):
    screen.blit(alien_img, (x, y))

# Function to draw bullet
def draw_bullet(x, y):
    screen.blit(bullet_img, (x, y))

# Function to display score
def display_score(score, high_score):
    font = pygame.font.SysFont(None, FONT_SIZE)
    text = font.render(f"Score: {score} High Score: {high_score}", True, WHITE)
    screen.blit(text, (10, 10))

# Function to display text on the screen
def display_text(text, size, color, position):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

# Function to create initial aliens
def create_initial_aliens(rows, cols):
    aliens = []
    start_x = SCREEN_WIDTH // 4
    start_y = SCREEN_HEIGHT // 8
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (ALIEN_WIDTH + 10)
            y = start_y + row * (ALIEN_HEIGHT + 10)
            aliens.append(pygame.Rect(x, y, ALIEN_WIDTH, ALIEN_HEIGHT))
    return aliens

# Function to create aliens at random positions
def create_random_aliens(num_aliens):
    aliens = []
    for _ in range(num_aliens):
        x = random.randint(0, SCREEN_WIDTH - ALIEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT // 2 - ALIEN_HEIGHT)
        aliens.append(pygame.Rect(x, y, ALIEN_WIDTH, ALIEN_HEIGHT))
    return aliens

# Game over screen
def game_over_screen(score, high_score):
    screen.fill(BLACK)
    display_text("GAME OVER", FONT_SIZE * 2, RED, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    display_text(f"Score: {score}", FONT_SIZE, WHITE, (SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 + 10))
    display_text(f"High Score: {high_score}", FONT_SIZE, WHITE, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 50))
    display_text("Press R to Restart or Q to Quit", FONT_SIZE, WHITE, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 90))
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return False
                if event.key == pygame.K_r:
                    waiting_for_input = False
                    return True


def game_loop():
    # Initialize variables
    spaceship_x = SCREEN_WIDTH // 2 - SPACESHIP_WIDTH // 2
    spaceship_y = SCREEN_HEIGHT - SPACESHIP_HEIGHT - 10
    spaceship_x_change = 0

    bullets = []
    alien_speed = ALIEN_SPEED
    alien_drop = ALIEN_DROP
    score = 0

    # Initial alien setup
    alien_rows = MIN_ALIEN_ROWS
    alien_cols = MIN_ALIEN_COLS
    aliens = create_initial_aliens(alien_rows, alien_cols)
    last_alien_spawn_time = time.time()
    last_increase_time = time.time()
    last_speed_increase_time = time.time()
    delay = ALIEN_DELAY
    alien_increasing = True

    # Load high score
    high_score = load_high_score()

    while True:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship_x -= SPACESHIP_SPEED
        if keys[pygame.K_RIGHT]:
            spaceship_x += SPACESHIP_SPEED
        if keys[pygame.K_SPACE]:
            if len(bullets) == 0 or bullets[-1].bottom < SCREEN_HEIGHT:
                bullets.append(pygame.Rect(spaceship_x + SPACESHIP_WIDTH // 2 - BULLET_WIDTH // 2, spaceship_y, BULLET_WIDTH, BULLET_HEIGHT))

        spaceship_x = max(0, min(spaceship_x, SCREEN_WIDTH - SPACESHIP_WIDTH))

        # Update bullets
        for bullet in bullets[:]:
            bullet.y -= BULLET_SPEED
            if bullet.y < 0:
                bullets.remove(bullet)

        # Update aliens
        new_aliens = []
        for alien in aliens:
            alien.x += alien_speed
            if alien.y + ALIEN_HEIGHT >= SCREEN_HEIGHT:
                game_over_screen(score, high_score)
                pygame.time.wait(2000)
                if score > high_score:
                    save_high_score(score)
                return False
            if alien.left < -ALIEN_WIDTH or alien.right > SCREEN_WIDTH:
                alien_speed = -alien_speed
                for a in aliens:
                    a.y += alien_drop
            new_aliens.append(alien)

        aliens = new_aliens

        # Check for collisions
        for bullet in bullets[:]:
            for alien in aliens[:]:
                if bullet.colliderect(alien):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    score += 10
                    break

        # Increase aliens and adjust speed
        current_time = time.time()
        if current_time - last_increase_time > ALIEN_INCREASE_INTERVAL:
            if alien_rows < MAX_ALIEN_ROWS and alien_cols < MAX_ALIEN_COLS:
                alien_rows += 1
                alien_cols += 1
                aliens = create_initial_aliens(alien_rows, alien_cols)
                last_increase_time = current_time
            else:
                # Add new aliens from random positions after reaching max grid
                if current_time - last_alien_spawn_time > delay:

                    new_aliens = create_random_aliens(3)  # Add 5 new random aliens
                    aliens.extend(new_aliens)
                    last_alien_spawn_time = current_time

        # Increase speed over time
        if current_time - last_speed_increase_time > SPEED_INCREMENT_INTERVAL:
            if alien_speed < MAX_ALIEN_SPEED:
                alien_speed += 0.5  # Increase speed
                last_speed_increase_time = current_time

        # Draw everything
        draw_spaceship(spaceship_x, spaceship_y)
        for bullet in bullets:
            draw_bullet(bullet.x, bullet.y)
        for alien in aliens:
            draw_alien(alien.x, alien.y)
        display_score(score, high_score)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    while True:
        restart = game_loop()
        if not restart:
            break

