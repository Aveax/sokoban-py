
class Game:

    moves = 0
    win = False

    def __init__(self, sok, map_obj):
        self.sok = sok
        self.map = map_obj
        self.robot_x = map_obj.get_robot_position()[0]
        self.robot_y = map_obj.get_robot_position()[1]

    def check_if_win(self):
        check = True
        for x in self.map.get_end_floors():
            if self.map.get_map()[x[1]][x[0]] != "4":
                check = False
                break
        if check:
            self.sok.level_cleared()
            self.win = True
            print(check)

    def check_win(self):
        return self.win

    def move_left(self):
        temp = self.map.get_map()[self.robot_y][self.robot_x - 1]
        # Go left
        if temp == "2" or temp == "3":
            self.map.get_map()[self.robot_y][self.robot_x - 1] = "5"
            self.map.get_map()[self.robot_y][self.robot_x] = "2"
            self.robot_x -= 1
            self.after_move()
        elif temp == "4":
            temp2 = self.map.get_map()[self.robot_y][self.robot_x - 2]
            # Go left and move box
            if temp2 == "2" or temp2 == "3":
                self.map.get_map()[self.robot_y][self.robot_x - 1] = "5"
                self.map.get_map()[self.robot_y][self.robot_x] = "2"
                self.map.get_map()[self.robot_y][self.robot_x - 2] = "4"
                self.robot_x -= 1
                self.after_move()
        else:
            print('cant move left')

    def move_right(self):
        temp = self.map.get_map()[self.robot_y][self.robot_x + 1]
        # Go right
        if temp == "2" or temp == "3":
            self.map.get_map()[self.robot_y][self.robot_x + 1] = "5"
            self.map.get_map()[self.robot_y][self.robot_x] = "2"
            self.robot_x += 1
            self.after_move()
        elif temp == "4":
            temp2 = self.map.get_map()[self.robot_y][self.robot_x + 2]
            # Go right and move box
            if temp2 == "2" or temp2 == "3":
                self.map.get_map()[self.robot_y][self.robot_x + 1] = "5"
                self.map.get_map()[self.robot_y][self.robot_x] = "2"
                self.map.get_map()[self.robot_y][self.robot_x + 2] = "4"
                self.robot_x += 1
                self.after_move()
        else:
            print('cant move right')

    def move_up(self):
        temp = self.map.get_map()[self.robot_y - 1][self.robot_x]
        # Go up
        if temp == "2" or temp == "3":
            self.map.get_map()[self.robot_y - 1][self.robot_x] = "5"
            self.map.get_map()[self.robot_y][self.robot_x] = "2"
            self.robot_y -= 1
            self.after_move()
        elif temp == "4":
            temp2 = self.map.get_map()[self.robot_y - 2][self.robot_x]
            # Go up and move box
            if temp2 == "2" or temp2 == "3":
                self.map.get_map()[self.robot_y - 1][self.robot_x] = "5"
                self.map.get_map()[self.robot_y][self.robot_x] = "2"
                self.map.get_map()[self.robot_y - 2][self.robot_x] = "4"
                self.robot_y -= 1
                self.after_move()
        else:
            print('cant move up')

    def move_down(self):
        temp = self.map.get_map()[self.robot_y + 1][self.robot_x]
        # Go down
        if temp == "2" or temp == "3":
            self.map.get_map()[self.robot_y + 1][self.robot_x] = "5"
            self.map.get_map()[self.robot_y][self.robot_x] = "2"
            self.robot_y += 1
            self.after_move()
        elif temp == "4":
            temp2 = self.map.get_map()[self.robot_y + 2][self.robot_x]
            # Go down and move box
            if temp2 == "2" or temp2 == "3":
                self.map.get_map()[self.robot_y + 1][self.robot_x] = "5"
                self.map.get_map()[self.robot_y][self.robot_x] = "2"
                self.map.get_map()[self.robot_y + 2][self.robot_x] = "4"
                self.robot_y += 1
                self.after_move()
        else:
            print('cant move down')

    def after_move(self):
        self.moves += 1
        self.sok.update_moves(self.moves)
        self.sok.draw()
        self.check_if_win()

    def restart_level(self):
        self.moves = 0
        self.sok.update_moves(self.moves)
        self.map.restart()
        self.robot_x = self.map.get_robot_position()[0]
        self.robot_y = self.map.get_robot_position()[1]
        self.sok.draw()
