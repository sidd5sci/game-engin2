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
from PIL import Image
import importlib


class Asset(object):
    def __init__(self):

        self.static = True
        self.dynamic = False
        # asset package path
        self.paths = importlib.import_module('paths','.')

    def loadAsset(self,package):
        config_file = self.paths.asset_package_path + package
        self.config = path + "config.json"
        self.readConfig(config_file)


    def readConfig(self,config_file):
        
        #path = os.path.join(path,"data")
        #path = os.path.join(path,"layer_"+str(self.layerCode)"+".json")
        file_ = open(config_file,"r+") 
        #file_ = open("data\\text.txt","r") 

        # reading the file 
        f_data = file_.read()
        # parsing the json file 
        fd = json.loads(f_data)

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

