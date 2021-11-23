from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import sys
import random

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0)


def glutFunct():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Car")
    init()


def polarCircle(r, xc, yc):

    xPoints = []
    yPoints = []
    pi = math.pi

    for i in range(45):
        x = r * math.cos(pi/180*i)
        y = r * math.sin(pi/180*i)

        xPoints = xPoints + [x+xc, -x+xc, y +
                             xc, -y+xc, -y+xc, y+xc, -x+xc, x+xc]
        yPoints = yPoints + [y+yc, -y+yc, x +
                             yc, -x+yc, x+yc, -x+yc, y+yc, -y+yc]


    points = list(list())
    for i in range(len(xPoints)):
        points += [[xPoints[i], yPoints[i]]]

    return points


class Car:
    def __init__(self, point):
        self.refPoint = point       
        self.length = 100
        self.height = 75
        self.radius = self.length * 0.1

    def drawCar(self):

        vertices = [
            [self.refPoint[0], self.refPoint[1]],
            [self.refPoint[0], self.refPoint[1] + self.height],
            [self.refPoint[0] + self.length*0.9, self.refPoint[1] + self.height],
            [self.refPoint[0] + self.length, self.refPoint[1] + self.height * 0.50],
            [self.refPoint[0] + self.length, self.refPoint[1]]
        ]

        tyres = [
            [self.refPoint[0] + self.length * 0.20, self.refPoint[1]],
            [self.refPoint[0] + self.length * 0.80, self.refPoint[1]]
        ]

        glClear(GL_COLOR_BUFFER_BIT)
        glLineWidth(2.0)
        
        
        glBegin(GL_POLYGON)

        for i in vertices:
            glColor3f(1, 0, 0)
            glVertex2fv(i)

        glEnd()

        glBegin(GL_LINES)

        for i in tyres:
            points = polarCircle(self.radius, i[0], i[1])
            for p in points:
                glColor3f(1, 1, 1)
                glVertex2fv(p)

        glEnd()

        glutSwapBuffers()

    def update(self, value):
        self.refPoint[0] += 1
        glutPostRedisplay()
        glutTimerFunc(int(100/60), self.update, (0))


def main():
    car = Car([-100, -50])
    glutFunct()
    glutDisplayFunc(car.drawCar)
    glutTimerFunc(0, car.update, 0)
    glutIdleFunc(car.drawCar)
    glutMainLoop()


main()