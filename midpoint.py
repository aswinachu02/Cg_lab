from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearscreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def plot_point():
    x1 = int(input('Enter the initial x coordinate: '))
    y1 = int(input('Enter the initial y coordinate: '))
    x2 = int(input('Enter the final x coordinate: '))
    y2 = int(input('Enter the final y coordinate: '))
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    if (dy<=dx):
        d = dy - (dx/2)
    else:
        d = dx - (dy/2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    while (x<=x2):
        glVertex2f(x/100,y/100)
        x = x+1
        if (d<0):
            d = d + dy
        else:
            y = y+1
            d = d + dy - dx
    glEnd()

def plotline():
    plot_point()
    glColor3f(0.0,0.0,0.0)
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
    glutCreateWindow("Midpoint_Line")  
    glutInitWindowSize(100, 100)  
    glutInitWindowPosition(50, 50)  
    glutDisplayFunc(plotline)
    clearscreen()
    glutMainLoop()  

main()