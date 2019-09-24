
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

class ObjectLoader():
        
        def __init__(self,*args,**kwargs):
            self.objects = []
            self.objectsPath = []
            self.paths =  importlib.import_module('paths','.')
            self.loadObjects()
        
        def loadObjects(self):
            # store the new project to database
            object_model = importlib.import_module('models.object_model','.')
            object_ = object_model.ObjectModel()
            return object_.readAll()
            
        def find_module(str):
            k = [i for i in range(len(lib_names)) if lib_names[i] == str]
            return libs[k[0]]
        
        def part(self,str, side):
            # split the string by '.'
            name, ext = str.split('.')

            if side == 1:
                return name
            else:
                return ext