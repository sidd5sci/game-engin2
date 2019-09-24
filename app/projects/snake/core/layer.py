
'''
MIT License

Copyright (c) 2018 sidd5sci

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
from PIL import Image, ImageDraw
import json,os,importlib

class Layer(object):

    def __init__(self,*args):
        self.tiles = []
        self.background = Image
        self.layerCode = args[0]
        self.Tile_module = args[1]
        self.ABSPATH = args[2]
        self.name = ""
    
    def createLayer(self,layer,type):
        if type == '.json':
            pass
        if type == '.xml':
            pass
    def translate(self,tx,ty):
        for t in self.tiles:
            if t.selected == True:
                t.x = t.x + tx
                t.y = t.y + ty
    def moveTo(self,x,y):
        # self.checkCollision(self,x,y)
        for t in self.tiles:
            if t.selected == True:
                    cx,cy = self.getCenter(t)
                    tx,ty = x-cx ,y-cy
                    print("<t.x,t.y>",t.x,t.y,"Diff>",x,y)
                    t.x = t.x + x
                    t.y = t.y + y
    def getCenter(self,tile):
        cx,cy = tile.x+tile.width/2,tile.y+tile.height/2
        return cx,cy
    def deSelectAll(self):
        for t in self.tiles:
            t.selected = False
    def deleteSelected(self):
        for t in self.tiles:
            if t.selected == True :
                self.tiles.remove(t)
    def deleteAll(self):
        for t in self.tiles:
                self.tiles.remove(t)
    
    def isInside(self,x,y):
        FlagedTile = False 
        for t in self.tiles:
            if x > t.x and x < t.x+t.width:
                if y > t.y and y < t.y+t.height:
                    FlagedTile = True
                    #t.textureEnabled = False
                    t.selected = True
        return FlagedTile
    def checkCollision(self,x,y):
        FlagedTiles = []
        for t in self.tiles:
            if x > t.x and x < t.x+t.width:
                if y > t.y and y < t.y+t.height:
                    FlagedTiles.append(t)
                    #t.textureEnabled = False
                    t.selected = True
        print ("Flaged : ",FlagedTiles)
        print ("Total :",len(self.tiles))
        return FlagedTiles
    def editText(self,text):
        for t in self.tiles:
            if t.selected == True:
                t.text = text
    def optimise(self):
        for t in self.tiles:
            for t1 in self.tiles:
                if t.equal(t1):
                    if id(t) != id(t1): 
                        print ("Removed :" ,t1, "| ",id(t1))
                        self.tiles.remove(t1)
                        print ("Total :",len(self.tiles))
                        break
    def transform(self,w=0,h=0):
        for t in self.tiles:
            if t.selected == True:
                t.width += w
                t.height += h
    def addTile(self,tile):
        self.tiles.append(tile)
    
    def addTileAtStart(self,tile):
        self.tiles.reverse()
        self.tiles.append(tile)
        self.tiles.reverse()
    def removeRecentTile(self):
        del self.tiles[-1]

    def _export(self,path,sid):

        print("Optamizing ...")
        self.optimise()
        # preset = input("Enter the preset : ")
        # file_ = open(self.ABSPATH+"data\l"+str(preset)+"_layer_"+str(self.layerCode)+".json","w+")
        
        # if not os.path.exists(path+"\\resources\scenes"):
        #     os.chdir(path+"\\resources")
        #     os.mkdir("scenes")

        try:
            file_ = open(self.ABSPATH+"\\projects\\"+path+"\\resources\scenes\s_"+str(sid)+"_l_"+str(self.layerCode)+".json","w+")
        except FileNotFoundError:
            file_ = open(self.ABSPATH+"\\projects\\"+path+"\\resources\scenes\s_"+str(sid)+"_l_"+str(self.layerCode)+".json","w")

        string_ = '{"tiles":['
        for t in self.tiles:
            s = '{"x":'+str(t.x)+',"y":'+str(t.y)+',"w":'+str(t.width)+',"h":'+str(t.height)+',"text":"'+str(t.text)+'"'
            s += ',"color":[254,'+str(t.color[0])+','+str(t.color[1])+','+str(t.color[2])+'],"collision":"'+str(t.collision)+'","display":"'+str(t.display)+'"'
            s += ',"spriteEnabled":"'+str(t.textureEnabled)+'"'
            s += ',"sprite":"'+str(t.textureName)+'","bitx":'+str(t.fx)+',"bity":'+str(t.fy)+',"bitw":'+str(t.fWidth)+',"bith":'+str(t.fHeight)+',"widthRatio":1,"heightRatio":1}'
            string_ += s+','
        
        string_ += ']}'

        print (string_)
        file_.write(string_)
        file_.close()
        return string_
    def _import(self):
        
        path = os.getcwd()
        preset = input("Enter the preset : ")
        #path = os.path.join(path,"data")
        #path = os.path.join(path,"layer_"+str(self.layerCode)"+".json")
        file_ = open(self.ABSPATH+"\data\l"+str(preset)+"_layer_"+str(self.layerCode)+".json","r+") 
        #file_ = open("data\\text.txt","r") 

        # reading the file 
        f_data = file_.read()
        # parsing the json file 
        fd = json.loads(f_data)
        # deleting all other tiles of the layer
        self.deleteAll()

        for t in fd['tiles']:
            tile = self.Tile_module.Tile(t['x'],t['y'],t['w'],t['h'])
            #t.setImage(pointer.image)
            tile.setFrame(t['bitx'],t['bity'],t['bitw'],t['bith'])
            tile.textureName = t['sprite']
            if t['spriteEnabled'] == "True":
                tile.textureEnabled = True
            else:
                tile.textureEnabled = False
            print(tile.textureEnabled,tile.textureName,t['spriteEnabled'])
            tile.color = [254,t['color'][1],t['color'][2],t['color'][3]]         
            self.tiles.append(tile)
    
    def loadLayer(self,layerData):

        # parsing the json file 
        fd = json.loads(layerData)
        # deleting all other tiles of the layer
        self.deleteAll()

        for t in fd['tiles']:
            tile = self.Tile_module.Tile(t['x'],t['y'],t['w'],t['h'])
            #t.setImage(pointer.image)
            tile.setFrame(t['bitx'],t['bity'],t['bitw'],t['bith'])
            tile.textureName = t['sprite']
            if t['spriteEnabled'] == "True":
                tile.textureEnabled = True
            else:
                tile.textureEnabled = False
            print(tile.textureEnabled,tile.textureName,t['spriteEnabled'])
            tile.color = [254,t['color'][1],t['color'][2],t['color'][3]]         
            self.tiles.append(tile)
            
            
    


                   
        
