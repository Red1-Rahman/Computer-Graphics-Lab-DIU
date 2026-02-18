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
    glColor3f(10, 0.0, 0.0)
    glPointSize(13)
    glBegin(GL_POINTS)
    glVertex2f(250, 250)
    glEnd()

    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(30,30)
    glVertex2f(250,250)
    glEnd()


    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(550, 550)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Drawing Pixels")
glutDisplayFunc(showScreen)

glutMainLoop()
