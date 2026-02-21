import random
from OpenGL.GL import *
from OpenGL.GLUT import *

points = []
for i in range(50):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    points.append((x, y))
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
    

    glColor3f(1, 1, 1)
    glPointSize(5)
    glBegin(GL_POINTS)
    for x, y in points:
        glVertex2f(x, y)
    glEnd()
    
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(550, 550)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"50 Random Points")
glutDisplayFunc(showScreen)

glutMainLoop()