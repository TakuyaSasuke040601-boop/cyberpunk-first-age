import pygame, sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cyberpunk: First Age")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)
font_s = pygame.font.Font(None, 24)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
    screen.fill((0,0,0))
    screen.blit(font.render("CYBERPUNK", True, (255,20,147)), (280, 200))
    screen.blit(font.render("FIRST AGE", True, (0,255,255)), (300, 260))
    screen.blit(font_s.render("[dyshinzou@CyberPunk ~]$ _", True, (0,255,0)), (250, 320))
    pygame.display.flip()
    clock.tick(60)