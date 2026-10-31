class World:
    def __init__(self, x_length, y_length):
        MAP = []
        for i in range(y_length):
            line = []
            for j in range(x_length):
                line.append(" ")
            MAP.append(line)
        self.map = MAP
        self.width = x_length
        self.height = y_length

    def exists(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
