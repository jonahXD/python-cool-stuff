# this game will make a moon game for me
# just like the moon buggy

# Rules for the games:
#   there will be a astronaut which will run on the moon
# and there will be some obstacle which will kill the astronaut
# and in order to save the astronaut from being dying we can make him jump .


# importing modules
import pygame
import random
from pygame import mixer



# start the mixer
mixer.init()
# loading the song
mixer.music.load("resources/background.wav")
# setting the volume
mixer.music.set_volume(0.5)
# start playing the song
mixer.music.play(-1)


# adding colours to our games
black = (0,0,0)

# important variables for our games to work
rockspeed = random.randint(3,7)
astrowidth, astroheight = 58, 50
rockwidth, rockheight = 40, 40
score = 0


# intialize our game
pygame.init()


# our window settings
screen = (500, 400)
win = pygame.display.set_mode(screen)
pygame.display.set_caption("Moon Astro")
background_image = pygame.image.load("resources/background.jpg")

# icon settings for our folder
icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)

# load the fonts 
font_30 = pygame.font.SysFont("Arial", 14)


# our class for Astronaut 
class Astro:
    def __init__(self, image):
        self.x = 400
        self.y = 352
        self.width = astrowidth
        self.height = astroheight
        self.image = image
        self.isjump = False
        self.jumpcount = 14

    def draw(self):
        win.blit(self.image, (self.x, self.y))


    def jump(self):
        # check if dino is jumping and then execute the jump
        if self.isjump:
            if self.jumpcount >= -14:
                neg = 1
                if self.jumpcount < 0:
                    neg = -1
                self.y -= self.jumpcount**2*0.1*neg
                self.jumpcount -= 1
            else:
                self.isjump = False
                self.jumpcount = 14
        

# our class for rock
class Rock:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.width = rockwidth
        self.height = rockheight
        self.image = image

    def draw(self):
        win.blit(self.image, (self.x, self.y))

    def move(self):
       self.x += rockspeed

    def check_outside_of_the_screen(self):
        global rockspeed
        if self.x > 505:
            self.x = random.randint(0, 50)
            rockspeed += 0.3

# our astro properties and declaring here
astro_img = pygame.transform.scale(pygame.image.load("resources/astronaut.png"), (astrowidth, astroheight))
astro=Astro(astro_img)


# our rock properties and declaring here
rock_img = pygame.transform.scale(pygame.image.load("resources/rock.png"),(rockwidth, rockheight))
rock = Rock(20, 370, rock_img)


# update our score or more our score
def score_():
    global score
    score += 0.2

# function for main loop 
def main():
    run = True
    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # draw rectangle for our astro in the screen
        astro_r = pygame.Rect(astro.x + 10, astro.y, astro.width - 20, astro.height-15)
        pygame.draw.rect(win, black, astro_r, 1)

        # draw rectangle for our rock in the screen
        rock_r = pygame.Rect(rock.x +5, rock.y, rock.width -10, rock.height-10)
        pygame.draw.rect(win, black, rock_r, 1)

        # stores key pressed
        keys = pygame.key.get_pressed()        
        if astro.isjump == False:
            if keys[pygame.K_SPACE]:
                astro.isjump = True

        # having a custom background
        win.blit(background_image, [0,0])

        # this increases our score
        score_()

        # draw the score
        txt_score = font_30.render("Score: "+str(round(score)), True, (255,255,255))
        win.blit(txt_score, [420, 10])

        # display our characters such as moon astro and the rock
        astro.draw()
        rock.draw()

        # move our rock 
        rock.move()

        # move our rock after disapering from the screen
        rock.check_outside_of_the_screen()
        
        # make our astro jump
        astro.jump()

        # see a collision
        if astro_r.colliderect(rock_r):
            run=False

        # updating our screen
        pygame.display.flip()

        # tick the cloack
        clock.tick(60)


    # quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
