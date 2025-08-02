import pygame
from settings import *
from src.clearCache import clear_cache
from src.App import App

clear_cache()
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("I Dont Want Corona X")
clock = pygame.time.Clock()
running = True
app = App()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    state = app.app_state
    if state == "START":
        app.start()
    elif state == "UPDATE":
        app.update(screen)
    elif state == "END":
        app.end()
        running = False
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()