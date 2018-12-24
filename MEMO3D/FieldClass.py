from OpenGL.GL import *

COLORS = ((1,0,0),(0,1,0),(0,0,1),(1,0,1),(0,1,1),(1,1,0),(0.5,0.25,0.125),(0.25,0.125,0.5),(1,1,1))


class FieldClass():


    def __init__(self, id_row, id_col, color_index, offset):

        self.rotation = 0
        self.rotation_change = 0
        self.rotation_current = 0

        self.x = (-2*offset + id_col*offset)
        self.y = (2*offset - id_row*offset)
        self.z = 0

        self.color_factor = 0.5
        self.color_index = color_index
        self.color = (COLORS[self.color_index][0] * self.color_factor,
                      COLORS[self.color_index][1] * self.color_factor,
                      COLORS[self.color_index][2] * self.color_factor)

        self.vertices = (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
        )

        self.faces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (4, 5, 1, 0),
            (6, 7, 5, 4),
            (1, 5, 7, 2),
            (4, 0 , 3, 6)
        )

    def getColorIndex(self):
        return self.color_index

    def setPointer(self):
        self.color_factor = 1
        self.color = COLORS[self.color_index]

    def unsetPointer(self):
        self.color_factor = 0.5
        self.color = (COLORS[self.color_index][0] * self.color_factor,
                      COLORS[self.color_index][1] * self.color_factor,
                      COLORS[self.color_index][2] * self.color_factor)

    def rotate(self):
        self.rotation = (self.rotation + 180)%360
        self.rotation_change = 10

    def draw(self):
        glPushMatrix()
        glTranslate(self.x,self.y, self.z)
        if self.rotation_current != self.rotation:
            self.rotation_current = (self.rotation_current + self.rotation_change)%360
        glRotatef(self.rotation_current, 0, 1, 0)
        glBegin(GL_TRIANGLES)
        for i in range(self.faces.__len__()):
            face = self.faces[i]
            if i == 0:
                glColor3fv(self.color)
            else:
                temp = (COLORS[8][0] * self.color_factor,
                      COLORS[8][1] * self.color_factor,
                      COLORS[8][2] * self.color_factor)
                glColor3fv(temp)
            glVertex3fv(self.vertices[face[0]])
            glVertex3fv(self.vertices[face[1]])
            glVertex3fv(self.vertices[face[3]])
            glVertex3fv(self.vertices[face[2]])
            glVertex3fv(self.vertices[face[3]])
            glVertex3fv(self.vertices[face[1]])
        glEnd()
        glPopMatrix()
