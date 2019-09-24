
'''
MIT License

Copyright (c) 2018 siddhartha singh <sidd5sci@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from PIL import Image
import pygame,math,time,os
import importlib
import json




class game():
    def __init__(self,*args,**kwargs):

        self.Camera_module = args[0]
        self.ABSPATH = args[1]
        self.Color_module = args[2]
        self.Layer_module = args[3]
        self.Player_module = args[4]
        self.Sprite_module = args[5]

        # screen height and width
        self.width ,self.height = 1000,640
        # center of the screen | environment cooords
        self.cx,self.cy,self.cz = self.width/2,self.height/2, -5
        
        # color object
        self.color = self.Color_module.colors()

        # initilise the main camera
        self.cam = self.Camera_module.camera((-50,-50,100))
        # world screen scales
        self.pixelFactor = 200/self.cam.pos[2]
        self.scalex,self.scaley = -self.width/self.pixelFactor,-self.height/self.pixelFactor

        # game basics
        self.gameOver = False
        
        # layers
        self.Layers = []
    
        self.init()

    def init(self):
        # initilize the pygame
        pygame.init()
        # loading the icon  
        #pygame.display.set_icon(pygame.image.load('Icon.png'))
        # init the name of the window
        pygame.display.set_caption("PyTrack | v1.0.1")
        # initilise the clock
        self.clock = pygame.time.Clock()
        # initilize the screen 
        # ,pygame.DOUBLEBUF,pygame.SRCALPHA
        #give me the biggest 16-bit display available
        modes = pygame.display.list_modes(16)
        if not modes:
            print ('16-bit not supported')
            self.screen = pygame.display.set_mode((self.width,self.height),pygame.SRCALPHA, 32)
        else:
            print ('Found Resolution:', modes[0])
            self.screen = pygame.display.set_mode(modes[0], pygame.FULLSCREEN, 16)
            #self.screen = pygame.display.set_mode((self.width,self.height),pygame.SRCALPHA, 32)
        #self.screen.set_alpha(254)
        #print(self.screen.get_alpha())
        self.screen.fill(pygame.Color(255,255,255))
        pygame.display.init()
        pygame.display.update()
        # graphics mode
    
    def screenToWorld(self,cords):
        x,y,z = cords[0],cords[1],0
        #x,y = x/pixelFactor,y/pixelFactor
        #x,y = scalex/2+x,scaley/2+y
        x,y = x+self.cam.pos[0],y+self.cam.pos[1]
        return [x,y,z]

    def worldToScreen(self,cords):
        x,y,z = cords[0],cords[1],cords[2]
        
        x,y,z = x-self.cam.pos[0],y-self.cam.pos[1],z+self.cam.pos[2]
        #pixelFactor = (pixelFactor*cam.pos[2])/z
        #f = 200/z
        #x,y = x*pixelFactor,y*pixelFactor
        #x,y = x*f,y*f
        #x,y = cx+int(x),cy+int(y)
        #x,y = scalex/2+x,scaley/2+y
        return [int(x),int(y)]

    def part(self,str, side):
        # split the tring by '.'
        name, ext = str.split('.')
        if side == 1:
            return name
        else:
            return ext

    def create(self):
        self.screen.fill(self.color.BLACK)
        tile_module = importlib.import_module('core.tile','.')
        
        names = os.listdir(self.ABSPATH+"\\resources\scenes")
        for s in names :
            a=self.part(s,1)
            sl = a.split('_')
            try:
                file_ = open(self.ABSPATH+"\\resources\scenes\\"+s,"r")
            except FileNotFoundError:
                print("filenotfound")
            
            l = self.Layer_module.Layer(sl[3],tile_module,self.ABSPATH) 
            f_data = file_.read()
            l.loadLayer(f_data)

            self.Layers.append(l)
        print(self.Layers)

        
    
    def draw(self):
        for layer in self.Layers:
            for t in layer.tiles:
                x,y = self.worldToScreen([t.x,t.y,50])
                if t.textureEnabled:
                    pic = t.texture.resize((t.width,t.height),Image.BILINEAR)
                    self.screen.blit(self.convertPILtoPygame(pic),(int(x),int(y)))
                else:
                    pygame.draw.rect(self.screen,self.color.RED,(int(x),int(y),int(t.width),int(t.height)))
            
    
    def update(self):
        # setting the smallest time variation
        dt = float(self.clock.tick(60))/10
        self.clock.tick(60)
    
    def input(self):

        mouse_rel = pygame.mouse.get_rel()
        mouse_buttons = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            #check if the event is the x button
            if event.type == pygame.QUIT:
                #if it is quit the game
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_RCTRL:
                    pass
    
    def main(self):
        
        self.create()
        while(self.gameOver != True):
            self.draw()
            self.input()
            self.update()
            pygame.display.update()
            # self.score()
    

if __name__ == "__main__":

    camera_module = importlib.import_module('core.camera','.')
    color_module = importlib.import_module('core.color','.')
    layer_module = importlib.import_module('core.layer','.')
    player_module = importlib.import_module('core.player','.')
    sprite_module = importlib.import_module('core.sprite','.')

    path = os.getcwd()
    
    g = game(camera_module,path,color_module,layer_module,player_module,sprite_module)
    g.main()




