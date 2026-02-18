from OpenGL.GL import *
from OpenGL.GLUT import *

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_line(x1, y1, x2, y2):
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    glColor3f(0.2, 0.4, 1.0)
    glLineWidth(2.5)

    # --- HOUSE LINES ---
    glBegin(GL_LINES)

    # Front wall
    draw_line(175, 145, 175, 350)   # Left vertical
    draw_line(175, 350, 420, 350)   # Top horizontal
    draw_line(420, 350, 420, 145)   # Right vertical
    draw_line(175, 145, 420, 145)   # Bottom horizontal

    # Roof
    draw_line(175, 350, 300, 450)   # Left slope
    draw_line(300, 450, 420, 350)   # Right slope

    # Door
    draw_line(270, 145, 270, 220)   # Left
    draw_line(330, 145, 330, 220)   # Right
    draw_line(270, 220, 330, 220)   # Top

    # Windows
    # Left window
    draw_line(200, 200, 230, 200)   # Top
    draw_line(200, 200, 200, 250)   # Left
    draw_line(200, 250, 230, 250)   # Bottom
    draw_line(230, 200, 230, 250)   # Right

    # Right window
    draw_line(365, 200, 395, 200)   # Top
    draw_line(365, 200, 365, 250)   # Left
    draw_line(365, 250, 395, 250)   # Bottom
    draw_line(395, 200, 395, 250)   # Right

    glEnd()

    # --- CORNER POINTS ---
    glPointSize(4)
    glBegin(GL_POINTS)
    points = [
        (175, 145), (420, 145), (175, 350), (420, 350), (300, 450),
        (270, 145), (330, 145), (270, 220), (330, 220)
    ]
    for pt in points:
        glVertex2f(*pt)
    glEnd()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(550, 550)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"House Drawing")
glutDisplayFunc(showScreen)
glutMainLoop()
