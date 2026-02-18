from OpenGL.GL import *
from OpenGL.GLUT import *

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(13)

    glBegin(GL_TRIANGLES) 
    glVertex2f(250, 250)
    glVertex2f(30, 30)
    glVertex2f(480, 450)
    glEnd()

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(550, 550)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Drawing triangle")
glutDisplayFunc(showScreen)
glutMainLoop()
