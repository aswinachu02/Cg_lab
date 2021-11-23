#program to plot line using bresenhams's algorithm
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearscreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)  
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  

def plot(x1, y1, x2, y2):
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(x1/100,y1/100)
    dy=y2 - y1
    dx=(x2 - x1)
    if dx>dy:
        m = 2 * dy
        pk = m - dx
        y = y1
        for x in range(x1, x2 + 1):
            glVertex2f(x/100,y/100)
            pk = pk + m
            if pk >= 0:
                y = y + 1
                pk= pk - 2 * (dx)
        glVertex2f(x2/100,y2/100)
    else:
        m=2*dx
        pk=m-dy
        x=x1
        for y in range (y1,y2+1):
            glVertex2f(x/100,y/100)
            pk=pk+m
            if pk>=0:
                x=x+1
                pk=pk-(2*dy)
        glVertex2f(x2/100,y2/100)
    glEnd()

def plotline():
    glClear(GL_COLOR_BUFFER_BIT)
    x1 = int(input("Enter the initial x coordinate: "))
    y1 = int(input("Enter the initial y coordinate: "))
    x2 = int(input("Enter the final x coordinate: "))
    y2 = int(input("Enter the final y coordinate: "))
    plot(x1, y1, x2, y2)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glEnd()
    glFlush()  

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Bresenham_Line")  
    glutInitWindowSize(100, 100)  
    glutInitWindowPosition(100, 100)  
    glutDisplayFunc(plotline)
    clearscreen()
    glutMainLoop()  

main()