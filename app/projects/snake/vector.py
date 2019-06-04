import math

'''
==========================================
    vector class
==========================================
'''
class vector(object):
    def __init__(self,x,y,z):
        # vector components
        self.x,self.y,self.z = x,y,z
        # some usefull quantities
        self.mag = 0.0
        self.alpha = 0.0
        self.beta = 0.0
        self.gama = 0.0
        self.cal_mag()
    def asign(self,x,y,z):
        self.x,self.y,self.z = x,y,z
        self.cal_mag()
    def cal_mag(self):
        return  math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
    def add(self,vctr):
        self.x += vctr.x; self.y += vctr.y; self.z += vctr.z
    def sub(self,vctr):
        self.x += vctr.x; self.y += vctr.y; self.z += vctr.z
    def multS(self,vctr):
        self.x *= vctr.x; self.y *= vctr.y; self.z *= vctr.z
    def multV(self,vctr):
        self.x *= (self.y*vctr.z - self.z*vctr.y)
        self.z *= (self.x*vctr.z - self.z*vctr.x)
        self.z *= (self.x*vctr.z - self.y*vctr.x)
    def divide(self,qt):# dividing vector by scaler quantity
        self.x /= qt; self.y /= qt; self.z /= qt
    def mult(self,qt): # multiply the vector with scaler quantity
        self.x *= qt; self.y *= qt; self.z *= qt
    def isnull(self):
        # check the vector is null/zero or not
        if self.x == 0 and self.y == 0 and self.z == 0:
            return True
        else:
            return False
    def reverseDir(self,axis):
        if axis == "x":
            self.x = -self.x
        if axis == "y":
            self.y = -self.y
        if axis == "z":
            self.z = -self.z
    def get(self):
        return self.x,self.y,self.z
