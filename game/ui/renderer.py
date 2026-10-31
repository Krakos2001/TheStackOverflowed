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
        self.font = pygame.font.Font(None, 28)

    def draw(self, player):
        self.screen.fill(BACKGROUND_COLOR)
        for x in range(self.world.width):
            for y in range(self.world.height):   # For every point of the map, draw the big inside rect and the outline one
                if self.world.map[x][y] == " ":
                    pygame.draw.rect(self.screen, TILE_COLOR, ((x * self.tile_size), (y * self.tile_size), self.tile_size, self.tile_size))
                    pygame.draw.rect(self.screen, GRID_COLOR, ((x * self.tile_size), (y * self.tile_size), self.tile_size, self.tile_size), 2)
                elif self.world.map[x][y] == "ore":
                    pygame.draw.rect(self.screen, ORE_COLOR, ((x * self.tile_size), (y * self.tile_size), self.tile_size, self.tile_size))
                    pygame.draw.rect(self.screen, GRID_COLOR, ((x * self.tile_size), (y * self.tile_size), self.tile_size, self.tile_size), 2)
        PLAYER_ICON_RADIUS = self.tile_size // 2 - 10
        PLAYER_ICON_CENTER_X = player.x * self.tile_size + self.tile_size // 2
        PLAYER_ICON_CENTER_Y = player.y * self.tile_size + self.tile_size //2
        pygame.draw.polygon(self.screen, PLAYER_COLOR, ((PLAYER_ICON_CENTER_X, PLAYER_ICON_CENTER_Y - PLAYER_ICON_RADIUS), (PLAYER_ICON_CENTER_X + PLAYER_ICON_RADIUS, PLAYER_ICON_CENTER_Y), (PLAYER_ICON_CENTER_X, PLAYER_ICON_CENTER_Y + PLAYER_ICON_RADIUS), (PLAYER_ICON_CENTER_X - PLAYER_ICON_RADIUS, PLAYER_ICON_CENTER_Y))) # Draws the player
        pygame.draw.rect(self.screen, GRID_COLOR, ((player.x * self.tile_size), (player.y * self.tile_size), self.tile_size, self.tile_size), 2)
        image = self.font.render(f"Inventory : {', '.join(player.inventory)}", True, (255, 255, 255))
        self.screen.blit(image, (0, 0))
        if player.mining:
            left = player.x * self.tile_size
            top = player.y * self.tile_size
            margin = self.tile_size // 8
            bar_width = self.tile_size - 2 * margin
            bar_height = 8
            bar_x = left + margin
            bar_y = top + self.tile_size - margin - bar_height
            pygame.draw.rect(self.screen, (20, 20, 25), (bar_x, bar_y, bar_width, bar_height))
            pygame.draw.rect(self.screen, (90, 200, 110), (bar_x, bar_y, int(bar_width * player.mining_fraction()), bar_height))
        pygame.display.flip()