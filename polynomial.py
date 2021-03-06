#Python program to draw polygon for given vertices.
#polygon has been drawn by using 
'''GL_LINE_LOOP
Draws a connected group of line segments from the first vertexto the last,then back to the first.Vertices n and n+1 define line n.
The last line, however, is defined by vertices N and 1. N lines are drawn.
  '''
# @MKchaudhary 13sept 2018
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)


def drawpolygon():
	n=input("Enter no of vertices: ")
	glBegin(GL_LINE_LOOP)
	for i in range(n):
		x=input("enter x-coordinate: ")
		y=input("enter y-coordinate: ")
		glVertex2i(x,y)
	glEnd()
	glFlush()

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	drawpolygon()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Polygon Drawing")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
