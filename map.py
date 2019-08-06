
class Map:
    map = []
    default_map = []
    end_floors = []

    def __init__(self, level):
        with open('maps/level' + level + '.txt', 'r') as f:
            for x in f.read().splitlines():
                self.map.append(list(x))
                self.default_map.append(list(x))
        self.save_end_floors()

    def get_map(self):
        return self.map

    def get_robot_position(self):
        for x in range(0, len(self.map)):
            for y in range(0, len(self.map[x]) - 1):
                if self.map[x][y] == "5":
                    return [y, x]

    def save_end_floors(self):
        for x in range(0, len(self.map)):
            for y in range(0, len(self.map[x]) - 1):
                if self.map[x][y] == "3":
                    self.end_floors.append([y, x])

    def get_end_floors(self):
        return self.end_floors

    def get_size(self):
        return [len(self.map[0]), len(self.map)]

    def restart(self):
        for x in range(0, len(self.default_map)):
            for y in range(0, len(self.default_map[x]) - 1):
                self.map[x][y] = self.default_map[x][y]

    def __del__(self):
        del self.map[:]
        del self.default_map[:]
        del self.end_floors[:]
