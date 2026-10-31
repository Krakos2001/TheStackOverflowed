class Player:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.inventory = []
        self.inv_capacity = 1
        self.mining = False
        self.mining_time = 2
        self.mining_progress = 0

    def move(self, dx, dy, world):
        new_x, new_y = self.x + dx, self.y + dy
        if world.exists(new_x, new_y): # Checks that the square exists
            self.x, self.y = new_x, new_y
            return True
        return False

    def mine(self, world):
        if len(self.inventory) >= self.inv_capacity:
            return False
        
