import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)


def plotting():
    print(' What line do you want to plot? ')
    print('1. Horizontal line')
    print('2. Vertical line')
    print('3. Diagonal line')
    ch = int(input('Enter your choice: '))
    if (ch==1):
        x1 = int(input('Enter the initial x coordinate: '))
        x2 = int(input('Enter the final x coordinate: '))
        y1 = int(input('Enter the y coordinate: '))
        y2 = y1
        x1 = x1/100
        x2 = x2/100
        y1 = y1/100
        y2 = y2/100

    elif (ch==2):
        x1 = int(input('Enter the x coordinate: '))
        x2 = x1
        y1 = int(input('Enter the initial y coordinate: '))
        y2 = int(input('Enter the final y coordinate: '))
        x1 = x1/100
        x2 = x2/100
        y1 = y1/100
        y2 = y2/100

    elif (ch==3):
        x1 = int(input('Enter the initial x coordinate: '))
        x2 = int(input('Enter the final x coordinate: '))
        y1 = x1
        y2 = x2
        x1 = x1/100
        x2 = x2/100
        y1 = y1/100
        y2 = y2/100
    
    else:
        print('Wrong Choice')

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(7.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(-1.0, 0.0)
    glVertex2f(1.0, 0.0)
    glEnd()
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)        
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)         
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Line")
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(100, 100)
glutDisplayFunc(plotting)
clearScreen()
glutMainLoop()