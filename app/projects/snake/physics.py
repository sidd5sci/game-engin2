
from vector import *
'''
==========================================
    physics class
==========================================
'''
class physics(object):

    def __init__(self,pos):

        # mass
        self.mass = 1.0 # kg
        # motion physics / newton physics
        self.pos = list(pos)
        self.velocity = vector(0,0,0)
        self.acc = vector(0,0,0)
        self.force = vector(0,0,0)
        self.time = 0.0
        self.dt = 0.15
        # material physics
        self.IR = 0.0
        self.rigidity = 0.0
        self.color = []
    def applyForce(self,force):
        # adding force to object
        self.force.add(force)
        # dividing force by mass of object
        self.force.divide(self.mass)
        self.acc.add(self.force)
        # multipling the acc to delta time
        self.acc.mult(self.dt)
        self.velocity.add(self.acc)
    def realTimeForces(self,earthMass,dist):
        gravitation = (G * self.mass * earthMass)/ (dist**2)
        gForce = vector(0,-1,0)
        gForce.mult(gravitation)
        self.applyForce(gForce)
    def applyG(self):
        g = vector(0,-9.8,0)
        self.applyAcc(g)
    def applyAcc(self,acc):
        self.acc.add(acc)
        # multipling the acc to delta time
        self.acc.mult(self.dt)
        self.velocity.add(self.acc)
    def collision(self,_object_):
        print (ctype)
    def boundryCollision(self,bound):
        print (ctype)
    def updatePos(self):
        
        if self.velocity.x != 0 or self.velocity.y != 0 or self.velocity.z != 0:
            self.pos[0] += self.velocity.x*self.dt
            self.pos[1] += self.velocity.y*self.dt
            self.pos[2] += self.velocity.z*self.dt
            
            
        
'''
==========================================
    2d collision 
==========================================
'''
x,y = 100,100

# clock wise order

surface1 = [[x+0,0+y],[x+100,0+y],[x+100,100+y],[x+0,100+y]]
surface2 = [[x+0+210,0+y+10],[x+100+210,0+y+10],[x+100+210,100+y+10],[x+0+210,100+y+10]]

def IsPointInside(x,y,left,right,top,bottom):
    
    
    if x > left and x < right:
        if y > top and y < bottom:
            return True
    else:
        return False
def IsPointInside(x,y,rect,h,w):
    
    
    if x > rect[0] and x < rect[0]+w:
        if y > rect[1] and y < rect[1]+h:
            return True
    else:
        return False            

    
def IsCollied(rect1,rect2):
    # it returns true if rectangles collied each other
    
    left,right,top,bottom = rect2[0][0],rect2[1][0],rect2[1][1],rect2[3][1]
    
    for i in range(0,4):
        t = IsPointInside(rect1[i][0],rect1[i][1],left,right,top,bottom)
        if t == True:
            break
    if t == True:
        return True
    else:
        return False
    

#print IsCollied(surface1,surface2)

