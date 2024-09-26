import pygame
from pygame.locals import *
import random
pygame.init()

width = 600
height = 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Car Game')

gray = (100, 100, 100)
green = (76,208,56)
red = (200,0,0)
white = (255,255,255)
yellow = (255,232,0)
gameover= False
speed = 2
score = 0
marker_width = 10
marker_height = 50
road = (100,0,300,height)
left_edge_marker = (95,0,marker_width,height)
right_edge_marker = (395,0,marker_width,height)

# x coordinates
left_lane= 150
right_lane= 350
center_lane= 250
lanes = [left_lane,right_lane]
lane_marker_move_y = 0
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image,x,y):
        pygame.sprite.Sprite.__init__(self)
#         scale image
        image_scale = 45/ image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))
        self.rect = self.image.get_rect()

        self.rect.center = [x,y]
class PlayerVehicle(Vehicle):
    def __init__(self, x,y):
        image = pygame.image.load('car1.jpg')
        super().__init__(image,x,y)
player_x = 250
player_y = 400

player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x,player_y)
player_group.add(player)

image_filenames = ['car2.jpg','car3.jpg','car4.jpg','car5.jpg']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load(image_filename)
    vehicle_images.append(image)

vehicle_group = pygame.sprite.Group()
crash = pygame.image.load ('car3.jpg')
crash_rect = crash.get_rect()
clock = pygame.time.Clock()
fps = 60
running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center [0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center [0] < right_lane:
                player.rect.x += 100
            for vehicle in vehicle_group:
                if player.rect.colliderect(player,vehicle):
                    gameover = True
                    if event.type == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect, (player.rect.center[1]+ vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1]+ vehicle.rect.center[1]) / 2]
    screen.fill(green)

    pygame.draw.rect(screen, gray, road)
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    #  draw lane markers
    lane_marker_move_y += speed *2
    if lane_marker_move_y >= marker_height *2:
        lane_marker_move_y = 0

    for y in range(marker_height * 2, height, marker_height * 2):
        pygame.draw.rect(screen, white,(left_lane + 45,y + lane_marker_move_y,marker_width,marker_height) )
        pygame.draw.rect(screen, white,(center_lane + 45 , y + lane_marker_move_y,marker_width,marker_height))

    player_group.draw(screen)

    if len(vehicle_group) <2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        if add_vehicle:
            lane = random.choice(lanes)

            image = random.choice(vehicle_images)

            vehicle = Vehicle(image,lane,height / -2)
            vehicle_group.add(vehicle)

    for vehicle in vehicle_group:
        vehicle.rect.y += speed

        if vehicle.rect.top >= height:
            vehicle.kill()

            score += 1

            if score >0 and screen % 5 ==0:
                speed += 1

    vehicle_group.draw(screen)

    font = pygame.font.SysFont('Arial', 20)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50,450)
    screen.blit(text,text_rect)
    if pygame.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center =[player.rect.center[0],player.rect.top]
    if gameover:
        screen.blit(crash, crash_rect)

        pygame.draw.rect(screen,red, (0,50, width,100))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('Game Over.Play again? ( Enter Y or N )',True, white)
        text_rect = text.get_rect()
        text_rect.center = (width/ 2, 100)
        screen.blit(text,text_rect)
    pygame.display.update()
pygame.quit()

