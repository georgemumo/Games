import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Klondike Solitaire")

# Load card images
CARD_WIDTH, CARD_HEIGHT = 72, 96
cards = []
for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
    for rank in range(1, 14):
        filename = f'{rank}_of_{suit}.png'
        image = pygame.image.load(os.path.join('cards', filename))
        image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
        cards.append((rank, suit, image))

# Card back image
card_back = pygame.image.load(os.path.join('cards', 'card_back.png'))
card_back = pygame.transform.scale(card_back, (CARD_WIDTH, CARD_HEIGHT))

# Piles
stock_pile = cards[:]
random.shuffle(stock_pile)
waste_pile = []
foundation_piles = {suit: [] for suit in ['hearts', 'diamonds', 'clubs', 'spades']}
tableau_piles = [[] for _ in range(7)]

# Deal cards to tableau piles
for i in range(7):
    for j in range(i + 1):
        card = stock_pile.pop()
        tableau_piles[i].append((card, j == i))

def draw_pile(pile, x, y):
    if pile:
        card, face_up = pile[-1]
        if face_up:
            screen.blit(card[2], (x, y))
        else:
            screen.blit(card_back, (x, y))
    else:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, CARD_WIDTH, CARD_HEIGHT), 2)

def draw_game():
    screen.fill((0, 128, 0))
    draw_pile(stock_pile, 10, 10)
    draw_pile(waste_pile, 100, 10)
    for i, suit in enumerate(foundation_piles):
        draw_pile(foundation_piles[suit], 200 + i * 90, 10)
    for i, pile in enumerate(tableau_piles):
        for j, (card, face_up) in enumerate(pile):
            y_offset = j * 20
            if face_up:
                screen.blit(card[2], (10 + i * 90, 130 + y_offset))
            else:
                screen.blit(card_back, (10 + i * 90, 130 + y_offset))
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Add game logic here

        draw_game()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
