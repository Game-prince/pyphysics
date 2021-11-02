import  pygame
from pygame.color import THECOLORS

from physics2D.components import make_box2D, make_ground, make_sun

pygame.init()

# screen parameters
screen_width = 800
screen_height = 600
caption = "My Game"
logo = pygame.image.load("Images/logo/logo.png")



# Making the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(caption)
pygame.display.set_icon(logo)

# Making ground
ground = make_ground(screen_width, 30, color=THECOLORS['green'])
ground_rect = ground.get_rect()
ground_rect.bottom = screen_height

# Making the sun
sun = make_sun(50, color=THECOLORS['yellow'])
sun_rect = sun.get_rect()
sun_rect.top = 10
sun_rect.centerx = screen_width/2

# Making a box
box = make_box2D(50, 50, color=THECOLORS['blue'])
box_rect = box.get_rect()
box_rect.center = (screen_width/2, screen_height/2)

# game loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(THECOLORS['skyblue'])

    # rendering screen
    screen.blit(ground, ground_rect)

    # rendering sun
    screen.blit(sun, sun_rect)

    # rendering the box
    screen.blit(box, box_rect)

    pygame.display.flip()

# quitting the game
pygame.quit()
quit()