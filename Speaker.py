import math

class Object3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distanceTo(self, anotherPoint):
        return math.sqrt( (self.x - anotherPoint.x)**2 + (self.y - anotherPoint.y)**2 + (self.y - anotherPoint.y)**2)

class Speaker(Object3D):
    pass