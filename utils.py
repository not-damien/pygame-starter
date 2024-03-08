import pygame
def writeToScreen(msg, x, y):
        text = font.render(msg, True, (10, 10, 10))
        textpos = text.get_rect(centerx=x, y=y)
        screen.blit(text, textpos)


def load_image(name, colorkey=None, scale=1):
    #fullname = os.path.join(data_dir, name)
    image = pygame.image.load(name)
    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()