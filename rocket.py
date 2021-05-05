class Rocket:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self): # will increment y position by 1
        self.y = self.y + 1
    def move_right(self): # will increment x position by 1
        self.x = self.x + 1
    def move_down(self): # will decrement y position by 1
        self.y = self.y - 1
    def move_left(self): # will decrement x position by 1
        self.x = self.x - 1
    def current(self): # print the  current position of the Rocket
        print("X=", self.x, ", ", "Y=", self.y, sep="")

go = Rocket()
go.move_up()
go.move_right()
go.move_right()
go.move_right()
go.current()