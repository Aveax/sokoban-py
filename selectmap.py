import pygame
from button import Button


class SelectMap:

    buttons = []

    def __init__(self):
        del self.buttons[:]
        self.color = (65, 105, 225)
        self.win = pygame.display.set_mode((450, 450))
        self.win.fill((70, 130, 180))
        for x in range(3):
            for y in range(3):
                self.buttons.append(Button(self.color, (x+1)*50+x*100, (y+1)*50+y*100, 50, 50, str(y*3+x+1)))

        for x in self.buttons:
            x.draw(self.win, (0, 0, 0))

    def get_buttons(self):
        return self.buttons

    def check_if_clicked(self, pos):
        for x in self.buttons:
            if x.clicked(pos):
                return x.get_text()
        return False

    def __del__(self):
        del self.buttons[:]
