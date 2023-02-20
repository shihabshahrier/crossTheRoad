import pygame
import random

# initialize pygame
pygame.init()

# set the screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cross The Road")

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# set up the player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - 70
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# set up the car obstacles
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(-500, -50)
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT + 50:
            self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
            self.rect.y = random.randint(-500, -50)
            self.speed = random.randint(1, 5)

# set up the game
def main():
    # create the player
    player = Player()

    # create a sprite group for the cars
    cars = pygame.sprite.Group()
    for i in range(10):
        car = Car()
        cars.add(car)

    # set up the game clock
    clock = pygame.time.Clock()

    # run the game loop
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # update the player
        keys = pygame.key.get_pressed()
        player.update(keys)

        # update the cars
        cars.update()

        # check for collisions
        if pygame.sprite.spritecollide(player, cars, False):
            print("You lose!")
            pygame.quit()
            quit()

        # fill the screen with white
        screen.fill(WHITE)

        # draw the player and cars
        screen.blit(player.image, player.rect)
        for car in cars:
            screen.blit(car.image, car.rect)

        # update the screen
        pygame.display.flip()

        # set the game's frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
