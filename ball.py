import turtle
import random
class Ball:
    def __init__(self, xpos, ypos, vx, vy, ball_color, size, width, height) -> None:
        self.__xpos = xpos
        self.__ypos = ypos
        self.__vx = vx
        self.__vy = vy
        self.__ball_color = ball_color
        self.__size = size
        self.__canvas_width = width
        self.__canvas_height = height

    def draw_circle(self, i):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.__ball_color[i])
        turtle.fillcolor(self.__ball_color[i])
        turtle.goto(self.__xpos[i], self.__ypos[i])
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.__size)
        turtle.end_fill()

    def move_circle(self, i):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.__xpos[i] += self.__vx[i]
        self.__ypos[i] += self.__vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.__xpos[i] + self.__vx[i]) > (self.__canvas_width - self.__size):
            self.__vx[i] = -self.__vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.__ypos[i] + self.__vy[i]) > (self.__canvas_height - self.__size):
            self.__vy[i] = -self.__vy[i]
