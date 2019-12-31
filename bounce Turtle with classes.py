# Very easy ball/paddle game with Pyton 3 and Turtle
# J Joubert 4 November 2019
# Written on mac OS - may need to adjust speed in windows
# This code can be copied, changed, updated and if improved - please let me know how!!

import turtle
#import time # and time.sleep(0.017) windows


win = turtle.Screen()
win.setup(500,600)
win.bgcolor('white')
win.tracer(0)
win.listen()

class Ball(turtle.Turtle):
    def __init__(self, paddle): # Initialize self with atributes
        super().__init__(shape = 'circle') # Initialize parent class (turtle)
        self.color('red')
        self.dx, self.dy = 6, 5 # May need change in windows eg 0.05, etc
        self.up()
        self.paddle = paddle
             
    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        # Change x direction if at the sides
        if self.xcor()<-230 or self.xcor()>230:
            self.dx *= -1

        # Change y if at the top
        if self.ycor()>280:
            self.dy *= -1

        # Reset ball if out at the bottom
        if self.ycor()<-280:
            self.dy *= -1
            self.goto(0,0)

    def bounce(self):
        # If ball is (1)between paddle right and left on x axis and (2) moving down
        # and (3) at level of paddle on y axis
        if paddle.xcor()-50 <= self.xcor()-10 <= paddle.xcor()+50 and ball.dy<0:
            if self.ycor()<=-200:
                self.dy *= -1
        

class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__(shape = 'square')
        self.color('blue')
        self.up()
        self.goto(0,-220)
        self.shapesize(1,5)

    def right(self):
        if self.xcor()<=200:
            self.goto(self.xcor()+40, self.ycor())
                  
    def left(self):
        if self.xcor()>=-200:
            self.goto(self.xcor()-40, self.ycor())

       
paddle = Paddle()
ball = Ball(paddle)

win.onkey(paddle.right, 'Right')
win.onkey(paddle.left, 'Left')


while True:
    win.update()
    ball.move()
    ball.bounce()
    #time.sleep(0.017) # windows?
