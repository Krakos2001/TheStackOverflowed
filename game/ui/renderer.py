import pygame

BACKGROUND_COLOR = (30, 33, 40)
TILE_COLOR = (46, 51, 62)
GRID_COLOR = (60, 65, 78)
PLAYER_COLOR = (240, 190, 70)
ORE_COLOR = (150, 150, 165)

class Renderer:
    def __init__(self, world, tile_size):
        self.world = world
        self.tile_size = tile_size
        self.screen = pygame.display.set_mode((world.width * tile_size, world.height * tile_size))

    def draw(self, world, player):
        self.screen.fill(BACKGROUND_COLOR)
        for y in range(self.world.height):
            for x in range(self.world.width):   # For every point of the map, draw the big inside rect and the outline one
                if world.map[x][y] == "":
                    pygame.draw.rect(self.screen, TILE_COLOR, ((x * self.tile_size), (y * self.tile_size), self.tile_size, self.tile_size))
                    pygame.draw.rect(self.screen, GRID_COLOR, ((x * self.tile_size), (y * self.tile_size), self.tile_size, self.tile_size), 2)
                elif world.map[x][y] == "ore":
                    pygame.draw.rect(self.screen, ORE_COLOR, ((x * self.tile_size), (y * self.tile_size), self.tile_size, self.tile_size))
                    pygame.draw.rect(self.screen, GRID_COLOR, ((x * self.tile_size), (y * self.tile_size), self.tile_size, self.tile_size), 2)
        pygame.draw.rect(self.screen, PLAYER_COLOR, ((player.x * self.tile_size), (player.y * self.tile_size), self.tile_size, self.tile_size)) # Draws the player
        pygame.draw.rect(self.screen, GRID_COLOR, ((player.x * self.tile_size), (player.y * self.tile_size), self.tile_size, self.tile_size), 2)
        pygame.display.flip()