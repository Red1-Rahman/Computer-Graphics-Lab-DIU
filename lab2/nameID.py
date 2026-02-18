from OpenGL.GL import *
from OpenGL.GLUT import *

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_horizontal_line(y):
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(50, y)
    glVertex2f(450, y)
    glEnd()

def draw_R(x, y, size=20):
    """Draw letter R using lines"""
    h = size
    w = size // 2
    glBegin(GL_LINES)
    # vertical stem
    glVertex2f(x, y)
    glVertex2f(x, y + h)
    # top horizontal
    glVertex2f(x, y + h)
    glVertex2f(x + w, y + h)
    # middle horizontal
    glVertex2f(x, y + h//2)
    glVertex2f(x + w, y + h//2)
    # diagonal leg
    glVertex2f(x, y + h//2)
    glVertex2f(x + w, y)
    # right vertical (top part)
    glVertex2f(x + w, y + h)
    glVertex2f(x + w, y + h//2)
    glEnd()

def draw_E(x, y, size=20):
    h = size
    w = size // 2
    glBegin(GL_LINES)
    # vertical stem
    glVertex2f(x, y)
    glVertex2f(x, y + h)
    # top horizontal
    glVertex2f(x, y + h)
    glVertex2f(x + w, y + h)
    # middle horizontal
    glVertex2f(x, y + h//2)
    glVertex2f(x + w, y + h//2)
    # bottom horizontal
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glEnd()

def draw_D(x, y, size=20):
    h = size
    w = size // 2
    glBegin(GL_LINES)
    # vertical stem
    glVertex2f(x, y)
    glVertex2f(x, y + h)
    # curved part as straight lines (approx)
    glVertex2f(x, y + h)
    glVertex2f(x + w, y + h - 5)
    glVertex2f(x + w, y + h - 5)
    glVertex2f(x + w, y + 5)
    glVertex2f(x + w, y + 5)
    glVertex2f(x, y)
    glEnd()

def draw_1(x, y, size=20):
    glBegin(GL_LINES)
    glVertex2f(x + size//2, y)
    glVertex2f(x + size//2, y + size)
    glEnd()

def draw_2(x, y, size=20):
    w = size
    h = size
    glBegin(GL_LINES)
    glVertex2f(x, y + h)
    glVertex2f(x + w, y + h)
    glVertex2f(x + w, y + h)
    glVertex2f(x + w, y + h//2)
    glVertex2f(x + w, y + h//2)
    glVertex2f(x, y)
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glEnd()

def draw_7(x, y, size=20):
    glBegin(GL_LINES)
    glVertex2f(x, y + size)
    glVertex2f(x + size, y + size)
    glVertex2f(x + size, y + size)
    glVertex2f(x + size//2, y)
    glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glColor3f(0.0, 0.0, 1.0)  # blue

    # Draw horizontal line
    draw_horizontal_line(250)

    # Draw Name "Red" above line
    draw_R(100, 280)
    draw_E(140, 280)
    draw_D(180, 280)

    # Draw ID "127" below line
    draw_1(120, 210)
    draw_2(150, 210)
    draw_7(190, 210)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
wind = glutCreateWindow(b"Name and ID with Lines")
glutDisplayFunc(showScreen)
glutMainLoop()
