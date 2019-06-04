
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
import os,time,random,math,subprocess
import datetime 
import importlib

class Layer():
        
        def __init__(self,*args,**kwargs):
                
                self.paths =  importlib.import_module('paths','.')
                scene_id = 0
                name = ""
                code = -1
                tiles = ""
                background = ""
                created_at = ""
        
        def createNewLayer(self,sid=None,name=None,code=None,tiles=None,background=None,created_at=None):
                layer_model = importlib.import_module('models.layer_model','.')
                newLayer = layer_model.LayerModel(sid,name,code,tiles,background,created_at)
                newLayer.create()

        def updateLayer(self,sid=None,name=None,code=None,tiles=None,background=None,created_at=None):
                layer_model = importlib.import_module('models.layer_model','.')
                newLayer = layer_model.LayerModel()
                newLayer.update(sid,name,code,tiles,background,created_at)

        def loadLayer(self,sid):
                layer_model = importlib.import_module('models.layer_model','.')
                newLayer = layer_model.LayerModel()
                return newLayer.readAll(sid)
         
        def removeProject(self,name):
                pass
        
        def claseProject(self,name):
                pass
        
        def saveProject(self,name):
                pass
        
        def recentProjects(self):
                pass
