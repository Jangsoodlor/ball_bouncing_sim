import turtle
from ball import Ball
import random
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
        self.__xpos = []
        self.__ypos = []
        self.__vx = []
        self.__vy = []
        self.__ball_color = []
        for _ in range(self.__num_balls):
            self.__xpos.append(random.randint(-1*self.__canvas_width + self.__ball_radius,
                                              self.__canvas_width - self.__ball_radius))
            self.__ypos.append(random.randint(-1*self.__canvas_height + self.__ball_radius,
                                              self.__canvas_height - self.__ball_radius))
            self.__vx.append(random.randint(1, 0.01*self.__canvas_width))
            self.__vy.append(random.randint(1, 0.01*self.__canvas_height))
            self.__ball_color.append((random.randint(0, 255), random.randint(0, 255),
                                      random.randint(0, 255)))


    def animate(self):
        ball = Ball(self.__xpos, self.__ypos, self.__vx, self.__vy, self.__ball_color,
                    self.__ball_radius, self.__canvas_width, self.__canvas_height)
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
