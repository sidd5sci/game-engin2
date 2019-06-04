

import math,random

class level():

    def __init__(self,_type_):

        self.row = 12
        self.col = 16
        self._type_ = _type_
        if self._type_ == 'redBrick':
            self.health = 100
            self.damage = 25
        elif self._type_ == 'whiteWall':
            self.health == 200
            self.damage = 25
        self.level = list()
    def fillSequence(self):

        for i in range(0,12):
            levelSequene = []
            for j in range(0,16):
                
                x,y,z,wallType,wallDisplay,wallCollision,health,damage = 0,0,0,self._type_,True,  True,self.health,self.damage

                if random.uniform(0,20) <= 10 :
                    wallDisplay,wallCollision = True,True
                else:
                    wallDisplay,wallCollision = False,False
                    
                levelSequene.append([x,y,z,wallType,wallDisplay,wallCollision,health,damage])
           
            self.level.append(levelSequene)    
    
