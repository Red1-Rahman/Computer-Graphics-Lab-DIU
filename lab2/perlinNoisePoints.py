import math
from OpenGL.GL import *
from OpenGL.GLUT import *

# Perlin Noise implementation
def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(t, a, b):
    return a + t * (b - a)

def grad(hash, x, y):
    h = hash & 15
    u = x if h < 8 else y
    v = y if h < 8 else x
    return ((-u) if (h & 1) else u) + ((-v) if (h & 2) else v)

def perlin(x, y):
    # Grid cell coordinates
    xi = int(x) & 255
    yi = int(y) & 255
    
    # Relative coordinates within cell
    xf = x - int(x)
    yf = y - int(y)
    
    # Fade curves
    u = fade(xf)
    v = fade(yf)
    
    # Hash values for gradients
    n00 = grad((xi + yi * 256) % 256, xf, yf)
    n10 = grad((xi + 1 + yi * 256) % 256, xf - 1, yf)
    n01 = grad((xi + (yi + 1) * 256) % 256, xf, yf - 1)
    n11 = grad((xi + 1 + (yi + 1) * 256) % 256, xf - 1, yf - 1)
    
    # Interpolate
    nx0 = lerp(u, n00, n10)
    nx1 = lerp(u, n01, n11)
    return lerp(v, nx0, nx1)

# Generate 50 points using Perlin noise
points = []
for i in range(50):
    # Use different offsets for x and y
    x_noise = perlin(i * 0.1, 0) * 250 + 250
    y_noise = perlin(i * 0.1, 100) * 250 + 250
    
    x = max(0, min(500, x_noise))
    y = max(0, min(500, y_noise))
    
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
    
    # Draw 50 points generated with Perlin noise
    glColor3f(0, 1, 0)  # Green color
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
wind = glutCreateWindow(b"50 Points with Perlin Noise")
glutDisplayFunc(showScreen)

glutMainLoop()