import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions for drawing the car image
IMAGE_WIDTH = 60
IMAGE_HEIGHT = 80

# Colors
CAR_BODY_COLOR = (255, 0, 0)  # Red
CAR_WINDOW_COLOR = (0, 0, 255)  # Blue
CAR_WHEEL_COLOR = (0, 0, 0)  # Black

# Create an image surface
car_surface = pygame.Surface((IMAGE_WIDTH, IMAGE_HEIGHT))
car_surface.fill((255, 255, 255))  # Fill with white background

# Draw car body
pygame.draw.rect(car_surface, CAR_BODY_COLOR, pygame.Rect(0, 20, IMAGE_WIDTH, IMAGE_HEIGHT - 20))

# Draw car windows
pygame.draw.rect(car_surface, CAR_WINDOW_COLOR, pygame.Rect(10, 10, IMAGE_WIDTH - 20, 10))

# Draw wheels
pygame.draw.circle(car_surface, CAR_WHEEL_COLOR, (15, IMAGE_HEIGHT - 10), 10)
pygame.draw.circle(car_surface, CAR_WHEEL_COLOR, (IMAGE_WIDTH - 15, IMAGE_HEIGHT - 10), 10)

# Save the image
pygame.image.save(car_surface, 'car_image.png')

# Quit Pygame
pygame.quit()
sys.exit()
