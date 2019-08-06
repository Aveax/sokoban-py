import pygame


class Sok:

    size = None
    screen = None
    box_size = None

    wall = None
    floor = None
    end_floor = None
    box = None
    robot = None

    moves = 0

    def __init__(self, map_obj):
        self.map = map_obj
        self.end_floors = self.map.get_end_floors()
        self.load_images()

    def load_images(self):
        self.wall = pygame.image.load('graphics/wall.png').convert()
        self.floor = pygame.image.load('graphics/floor.png').convert()
        self.end_floor = pygame.image.load('graphics/endfloor.png').convert()
        self.box = pygame.image.load('graphics/box.png').convert()
        self.robot = pygame.image.load('graphics/robot.png').convert()
        self.box_size = self.wall.get_width()

        map_size = self.map.get_size()
        self.size = (map_size[0] * self.box_size, map_size[1] * self.box_size)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.update()

    def get_map(self):
        return self.map

    def draw(self):
        images = {'0': self.floor, '1': self.wall, '2': self.floor, '3': self.end_floor, '4': self.box, '5': self.robot}

        map_size = self.map.get_size()

        for x in range(0, map_size[1]):
            for y in range(0, map_size[0]):
                self.screen.blit(images[self.map.get_map()[x][y]], (y * self.box_size, x * self.box_size))

        self.redraw_end_floor()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Moves: ' + str(self.moves), True, (0, 0, 0))
        self.screen.blit(text, (10, 10))

        pygame.display.update()

    def redraw_end_floor(self):
        for x in self.end_floors:
            if self.map.get_map()[x[1]][x[0]] == "2":
                images = {'0': self.floor, '1': self.wall, '2': self.floor, '3': self.end_floor, '4': self.box,
                          '5': self.robot}
                self.screen.blit(images["3"], (x[0] * self.box_size, x[1] * self.box_size))

    def update_moves(self, moves):
        self.moves = moves

    def level_cleared(self):
        font = pygame.font.SysFont('comicsansms', 32, bold=True)
        text = font.render('Congratulations', True, (0, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.size[0] // 2, self.size[1] // 2)
        self.screen.blit(text, text_rect)
        pygame.display.update()
