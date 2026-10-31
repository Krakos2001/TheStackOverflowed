from game.economy import RESOURCES

class Player:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.inventory = []
        self.inv_capacity = 1
        self.mining = False
        self.mining_progress = 0
        self.mining_duration = 1

    def move(self, dx, dy, world):
        new_x, new_y = self.x + dx, self.y + dy
        if world.exists(new_x, new_y): # Checks that the square exists
            self.x, self.y = new_x, new_y
            self.stop_mining()
            return True
        return False


    def start_mining(self):
        self.mining = True

    def stop_mining(self):
        self.mining_progress = 0
        self.mining = False

    def mine(self, world, dt):
        tile = world.tile_state(self.x, self.y)
        if self.mining is False:
            self.mining_progress = 0
            return
        if tile in RESOURCES:
            self.mining_duration = RESOURCES[tile]["time"]
            if len(self.inventory) < self.inv_capacity:
                self.mining_progress += dt
                if self.mining_progress >= RESOURCES[tile]["time"]:
                    self.inventory.append(RESOURCES[tile]["item"])
                    self.mining_progress = 0
            else:
                self.mining_progress = 0
        else:
            self.mining_progress = 0
        
    def mining_fraction(self):
        return min(self.mining_progress / self.mining_duration, 1)
        
