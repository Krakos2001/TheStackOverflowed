from game.world import World
from game.player import Player
from game.ui.renderer import Renderer
import pygame

pygame.init()
world = World(5, 5)
player = Player(2, 2)
renderer = Renderer(world, 96)
clock = pygame.time.Clock()
running = True

world.map[0][0] = "iron_ore"

while running:
    for event in pygame.event.get():   # Receive everything that happened (keypresses, etc...)
        if event.type == pygame.QUIT:  # If the event received is closing the window
            running = False
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_UP:
                player.move(0, -1, world)
            elif key == pygame.K_DOWN:
                player.move(0, 1, world)
            elif key == pygame.K_LEFT:
                player.move(-1, 0, world)
            elif key == pygame.K_RIGHT:
                player.move(1, 0, world)
            elif key == pygame.K_SPACE:
                player.start_mining()
        elif event.type == pygame.KEYUP:
            key = event.key
            if key == pygame.K_SPACE:
                player.stop_mining()
    dt = clock.tick(60) / 1000
    player.mine(world, dt)
    renderer.draw(player)

pygame.quit()