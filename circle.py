
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def clearScreen():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)


def plot_line():
    d = 100
    print(' How do you want to draw a circle? ')
    print('1. using Mid point circle drawing algorithm')
    print('2. using Polar circle generation algorithm')
    print('3. using Non-Polar circle generation algorithm')
    ch = int(input('Enter your choice: '))
    xc = int(input('Enter the x coordinate of centre: '))
    yc = int(input('Enter the y coordinate of centre: '))
    r = int(input('Enter the radius of circle: '))

    if (ch==1):

        p = 1-r
        x = 0
        y = r
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)
        glColor3f(0.0,0.0,0.0)  
        glBegin(GL_POINTS)
        while(x<=y):
            glVertex2f((xc+x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc-y)/d)
            glVertex2f((xc+x)/d,(yc-y)/d)
            glVertex2f((xc+y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc-x)/d)
            glVertex2f((xc+y)/d,(yc-x)/d)
            x+=1
            if(p<=0):
                p = p + (2*x) + 1
            else:
                y = y - 1
                p = p + (2*(x-y)) + 1
        glEnd()
        glFlush()




    elif (ch==2):
        
        dtheta = 1/500
        theta = 0
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)
        glColor3f(0.0,0.0,0.0)
        glBegin(GL_POINTS)
        while(theta <= 22/28):
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f((xc+x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc+y)/d)
            glVertex2f((xc-x)/d,(yc-y)/d)
            glVertex2f((xc+x)/d,(yc-y)/d)
            glVertex2f((xc+y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc+x)/d)
            glVertex2f((xc-y)/d,(yc-x)/d)
            glVertex2f((xc+y)/d,(yc-x)/d)
            theta = theta + dtheta
        glEnd()
        glFlush()


    elif (ch==3):
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)
        glColor3f(0.0,0.0,0.0)
        glBegin(GL_POINTS)
        x=xc-r
        t=xc+r
        glVertex2f(x/d,yc/d)
        glVertex2f(t/d,yc/d)
        i=1/7500
        x=x+i
        while x<t:
            ad=math.sqrt(r*r - (x-xc)*(x-xc))
            glVertex2f(x/d,(yc+ad)/d)
            glVertex2f(x/d,(yc-ad)/d)
            x+=i
        glEnd()
        glFlush()

    else:
        print('Invalid Choice')

def plot():
    plot_line()
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
glutCreateWindow("Circle")
glutInitWindowSize(100, 100)
glutInitWindowPosition(100, 100)
glutDisplayFunc(plot)
clearScreen()
glutMainLoop()