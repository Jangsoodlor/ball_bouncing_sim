import turtle
import random
class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls) -> None:
        self.__xpos = []
        self.__ypos = []
        self.__vx = []
        self.__vy = []
        self.__ball_color = []
        self.__canvas_width = canvas_width
        self.__canvas_height = canvas_height
        self.__size = ball_radius
        self.__balls = num_balls
        for _ in range(self.__balls):
            self.__xpos.append(random.randint(-1*canvas_width + ball_radius, canvas_width - ball_radius))
            self.__ypos.append(random.randint(-1*canvas_height + ball_radius, canvas_height - ball_radius))
            self.__vx.append(random.randint(1, 0.01*canvas_width))
            self.__vy.append(random.randint(1, 0.01*canvas_height))
            self.__ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

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

    def move_circle(self, i,):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.__xpos[i] += self.__vx[i]
        self.__ypos[i] += self.__vy[i]

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.__xpos[i] + self.__vx[i]) > (self.__canvas_width - self.__size):
            self.__vx[i] = -self.__vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.__ypos[i] + self.__vy[i]) > (self.__canvas_height - self.__size):
            self.__vy[i] = -self.__vy[i]
