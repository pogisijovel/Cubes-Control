# Jovel Kenth Emnacin
# W = Rotate Up
# S = Rotate Down
# A = Left
# D = Right
# Space = Spin

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

pygame.display.set_caption("05 PT 1")
# Define cube vertices and quads
vertices = (
    (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5)
)
quads = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

# Function to draw a cube
def Cube():
    glBegin(GL_QUADS)
    for quad in quads:
        for vertex in quad:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main function
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)

    # Cube positions and colors
    cube_size = 0.9
    cube_positions = [i * cube_size for i in range(5)] 
    x_position = 100
    cube_colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)]
    angle = 0
    spinning = False  
    rotation_x = 0

    glEnable(GL_DEPTH_TEST)

    left_pressed = False
    right_pressed = False
    step_size = 1.1 * cube_size  

    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            rotation_x += 1  
        if keys[pygame.K_DOWN]:
            rotation_x -= 1  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spinning = not spinning  
                elif event.key == pygame.K_LEFT:
                    left_pressed = True  
                elif event.key == pygame.K_RIGHT:
                    right_pressed = True            
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_pressed = False  
                elif event.key == pygame.K_RIGHT:
                    right_pressed = False  

        if spinning:
            angle += 1  # Increment the angle for rotation

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply a rotation around the y-axis at the origin
        glPushMatrix()
        glRotatef(angle, 0, 0, 1)
        
        for position, color in zip(cube_positions, cube_colors):
            glPushMatrix()
            glTranslatef(position, 0, 0)  
            glColor3fv(color)  
            glScalef(cube_size, cube_size, cube_size) 
            glRotatef(rotation_x, 1, 0, 0)
            Cube()
            glPopMatrix()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

        # Move cubes based on key presses
        if left_pressed:
            cube_positions = [x - step_size for x in cube_positions]
            left_pressed = False 
        elif right_pressed:
            cube_positions = [x + step_size for x in cube_positions]
            right_pressed = False 

main()