from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Scale variables
scaleX, scaleY = 1.0, 1.0
Sx, Sy = 0.1, 0.1

# Position variables
posX, posY = 0.0, 0.0
moveStep = 10.0

# 🔹 Rotation variables (NEW)
angleZ = 0.0
stepZ = 5.0


def draw_triangle():
    glColor3f(1.0, 0.6, 0.2)  # Orange

    glBegin(GL_TRIANGLES)
    glVertex2f(250, 250)  # Top
    glVertex2f(100, 100)  # Bottom Left
    glVertex2f(400, 100)  # Bottom Right
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # 🔥 Correct transformation order

    # 1. Move object (WASD)
    glTranslatef(posX, posY, 0.0)

    # 2. Move to triangle center (pivot fix)
    glTranslatef(250, 150, 0)

    # 3. Rotate
    glRotatef(angleZ, 0, 0, 1)

    # 4. Scale
    glScalef(scaleX, scaleY, 1.0)

    # 5. Move back
    glTranslatef(-250, -150, 0)

    draw_triangle()
    glutSwapBuffers()


def keyboard(key, x, y):
    global scaleX, scaleY, posX, posY, angleZ

    if key == b'+':
        scaleX += Sx
        scaleY += Sy

    elif key == b'-':
        scaleX -= Sx
        scaleY -= Sy

    # WASD movement
    elif key == b'w':
        posY += moveStep

    elif key == b's':
        posY -= moveStep

    elif key == b'a':
        posX -= moveStep

    elif key == b'd':
        posX += moveStep

    # 🔹 Rotation
    elif key == b'z':
        angleZ += stepZ  # clockwise

    elif key == b'x':
        angleZ -= stepZ  # counter-clockwise

    glutPostRedisplay()


def initiate():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Scale + Move + Rotate Triangle")

initiate()

glutDisplayFunc(display)
glutKeyboardFunc(keyboard)

print("Controls:")
print("+ / - : Scale")
print("WASD : Move")
print("Z / X : Rotate")

glutMainLoop()