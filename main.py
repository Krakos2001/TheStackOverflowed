from game.world import World
from game.player import Player
from game.ui.renderer import Renderer

world = World(5, 5)
player = Player(2, 2)
print(player.move(1, 0, world))
print(player.move(0, 1, world))
print(player.move(4, 0, world))

renderer = Renderer(world, 96)
renderer.draw(player)