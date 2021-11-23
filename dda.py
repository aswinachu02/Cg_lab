import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def plotting():
    print('Enter coordinates for initial point:')
    x1 = int(input('x coordinate: '))
    y1 = int(input('y coordinate: '))
    print('Enter coordinates for final point:')
    x2 = int(input('x coordinate: '))
    y2 = int(input('y coordinate: '))
    if abs(x2-x1) > abs(y2-y1):
        l = abs(x2-x1)
    else:
        l = abs(y2-y1)
    dx = (x2-x1)/l
    dy = (y2-y1)/l
    x = x1
    y = y1
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x1/100, y1/100)
    for i in range(l):
        x = x + dx
        y = y + dy
        glVertex2f(x/100, y/100)
    glVertex2f(x2/100, y2/100)
    glEnd()

def plot():
    plotting()
    glColor3f(0.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)        
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Line_DDA")
glutInitWindowSize(100, 100)
glutInitWindowPosition(100, 100)
glutDisplayFunc(plot)
clearScreen()
glutMainLoop()