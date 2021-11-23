from OpenGL.GL import *
from OpenGL.GLU import * 
from OpenGL.GLUT import * 
import sys
import math

def init():
    glClearColor (0.0,0.0,149.0,0.0) 
    gluOrtho2D (-1.0,1.0,-1.0,1.0) 

def plotting():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(1.0,1.0,1.0) 
    glPointSize(5.0) 
    glBegin(GL_POINTS)
    glVertex2f(0.0,0.0) 
    glEnd()
    glFlush() 

def main():
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB) 
    glutInitWindowSize(1000,1000) 
    glutInitWindowPosition(200,200) 
    glutCreateWindow("Plotting Origin")
    glutDisplayFunc(plotting) 
    init() 
    glutMainLoop() 

main()