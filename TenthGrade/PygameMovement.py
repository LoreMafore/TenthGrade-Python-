import pygame, random, sys
from pygame.color import THECOLORS


# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode([1000,800])
clock = pygame.time.Clock()
pygame.mixer.init()

class hollowknightClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def move(self,location):
        self.rect.left, self.rect.top = location


#Draw some objects on the screen
screen.fill(THECOLORS["white"])
x_pos = int(250 - (400/2))
y_pos = int(200 - (551/2))

# Load images
hollowknight = hollowknightClass('hollowknight.png',[x_pos,y_pos])
screen.blit(hollowknight.image, hollowknight.rect)

# Execute the loop
running = True

while running:
    screen.fill(THECOLORS["white"])
    clock.tick(30)
    x_pos += random.randint(-3,3)
    y_pos += random.randint(-3,3)
    hollowknight.move([x_pos,y_pos])
    screen.blit(hollowknight.image,hollowknight.rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_pos += -20
            if event.key == pygame.K_RIGHT:
                x_pos += 20
