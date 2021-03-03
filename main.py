from pydraw import *
import random

screen = Screen(800,600,"ya yeet")
screen.color(Color("black"))

sheeeeesh = []


class Bouncy():
    def __init__(self,x,y,direc_x,direc_y,size):
        self.x = x
        self.y = y
        self.direc_x = direc_x
        self.direc_y = direc_y

        self.text = Text(screen,"DVD",x,y,Color.random(),size=size)
        self.width = self.text.width()
        self.height = self.text.height()

    def move(self):
        self.text.move(self.direc_x*5,self.direc_y*5)
        self.x+=self.direc_x*5
        self.y+=self.direc_y*5
        # self.text.color(Color.random())

    def check(self):
        if 0>self.x or self.x+self.width>screen.width():
            self.text.color(Color.random())
            self.direc_x *=-1
        elif 0>self.y or self.y+self.height>screen.height():
            self.text.color(Color.random())
            self.direc_y *=-1

def mousedown(button,location):
    global sheeeeesh
    bounce = Bouncy(location.x(),location.y(),random.randrange(-1,2,2),random.randrange(-1,2,2),50)
    sheeeeesh.append(bounce)


screen.listen()

running = True
while running:
    # screen.color(Color.random())
    for bounce in sheeeeesh:
        bounce.move()
        bounce.check()
    screen.sleep(1/120)
    screen.update()
