import  pygame

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



# game loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quitting the game
pygame.quit()
quit()