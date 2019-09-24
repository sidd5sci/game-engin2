
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

class Project():
        
        def __init__(self,*args,**kwargs):
                
                self.paths =  importlib.import_module('paths','.')
                self.size = ""
                self.oriantation = ""
                self.name = ""
                self.created_at = ""
                self.project_dir = "" # absolute path
        
        def createNewProject(self,name,oriantation):
                os.chdir(self.paths.projects_path)
                self.oriantation = oriantation
                if oriantation == 'landscape':
                    self.size = "800x480"
                else :
                    self.size = "480x800"
                self.created_at = datetime.datetime.now()
                self.project_dir = self.paths.projects_path+name
                # Create target Directory if don't exist
                if not os.path.exists(name):
                        os.mkdir(name)
                        os.chdir(self.paths.projects_path+name)
                        os.mkdir("core")
                        os.mkdir("resources")
                        os.chdir(self.paths.projects_path+name+"\\resources")
                        os.mkdir("music")
                        os.mkdir("nodes")
                        os.mkdir("objects")
                        os.mkdir("sounds")
                        os.mkdir("sprites")
                        os.mkdir("scenes")
 
                        print("Directory " , name ,  " Created ")

                else:    
                        print("Directory " , name ,  " already exists")
                # store the new project to database
                project_model = importlib.import_module('models.project_model','.')
                newProject = project_model.ProjectModel(name,oriantation,self.size,created_at=self.created_at,dir=self.project_dir)
                newProject.create()
                
        def openProject(self,name):
                # store the new project to database
                project_model = importlib.import_module('models.project_model','.')
                openProject = project_model.ProjectModel()
                allProjects = openProject.readAll()
                for p in allProjects:
                    if p.project_name == name:
                        return p
        def removeProject(self,name):
                pass
        
        def claseProject(self,name):
                pass
        
        def saveProject(self,name):
                pass
        
        def recentProjects(self):
                pass
        
