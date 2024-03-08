import pygame
from utils import writeToScreen, load_image
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Name Of The game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 64)



class PlayerMouse(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.image, self.rect = load_image(image,scale=.1)#adjust scale to get character sizing right
        self.target_width, self.target_height =self.image.get_size()
        self.rect.topleft = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)#adjust arugments for disired starting position
    def update(self):
        cursor_x, cursor_y = pygame.mouse.get_pos()
        bg_x = cursor_x - (self.target_width // 2)
        bg_y = cursor_y - (self.target_height // 2)
        self.rect.topleft = (bg_x,bg_y)


class asteriod(pygame.sprite.Sprite):
    
    def __init__(self,image,startingX, startingY):
        pygame.sprite.Sprite.__init__(self)
        self.direction = -1
        self.speed = 10
        self.image, self.rect = load_image(image,scale=.08)#adjust scale to get character sizing right
        self.rect.topleft = pygame.Vector2(startingX, startingY)#adjust arugments for disired starting position
    def checkCollide(self, other):
        return self.rect.colliderect(other.rect)

    def update(self):
        #get current location
        (x,y) = self.rect.topleft
        
        #causes object to turn around when it hits the top or bottom of the screen
        if y < 0 or y > screen.get_height(): 
            self.direction = -self.direction
        
        #calculate next location
        y = y + (5 * self.direction)

        #update location to next location
        self.rect.topleft = (x,y)
        
        #this causes the astroid to kill the keyboard player if they make contact
        if (self.checkCollide(p1)):
            p1.kill()

        #this makes it so the mouse controled player destorys the astroid on contact
        if(self.checkCollide(p2)):
            self.kill()




class PlayerWasd(pygame.sprite.Sprite):
    
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = 15
        self.image, self.rect = load_image(image,scale=.5)#adjust scale to get character sizing right
        self.rect.topleft = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)#adjust arugments for disired starting position
    def update(self):
        keys = pygame.key.get_pressed()
        (x,y) = self.rect.topleft
        if keys[pygame.K_w]:
            y -= self.speed
        if keys[pygame.K_s]:
            y += self.speed
        if keys[pygame.K_a]:
            x -= self.speed
        if keys[pygame.K_d]:
            x += self.speed
        self.rect.topleft = (x,y)






p1 = PlayerWasd("./exampleShroom.png")
p2 = PlayerMouse("./sprite.png")
enemy = asteriod("./asteroid.png", 200,200)



def main():
    # pygame setup    
    
    allsprites = pygame.sprite.RenderPlain((p1,p2,enemy))
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
    #################################################################
        # RENDER YOUR GAME HERE
        allsprites.update()
        allsprites.draw(screen)


    ##############################################################
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()






main()