import turtle
from ball import Ball
class Main:
    def __init__(self) -> None:
        self.__num_balls = int(input("Number of balls to simulate: "))
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.__canvas_width = turtle.screensize()[0]
        self.__canvas_height = turtle.screensize()[1]
        self.__ball_radius = 0.05 * self.__canvas_width
        turtle.colormode(255)


    def animate(self):
        ball = Ball(self.__canvas_width, self.__canvas_height, self.__ball_radius, self.__num_balls)
        while True:
            turtle.clear()
            for i in range(self.__num_balls):
                ball.draw_circle(i)
                ball.move_circle(i)
            turtle.update()
        turtle.done()

if __name__ == '__main__':
    t = Main()
    t.animate()
