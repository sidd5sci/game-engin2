

import importlib
import os,subprocess
import webbrowser as wb

# open_new_tab()
# open()
# wb.get('chrome %s').open_new_tab('http://www.google.com')

# urL='https://www.python.org'
# mozilla_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
# webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(mozilla_path))
# webbrowser.get('firefox').open_new_tab(urL)

# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")

class Server():
    
    def __init__(self,*args,**kwargs):
        self.project_root = args[0]
        self.port = args[1]
        self.address = "127.0.0.1"
        self.paths =  importlib.import_module('paths','.')
    
    def start(self):
        os.chdir(self.paths.projects_path+self.project_root)
        returned_value = subprocess.call("python -m http.server "+self.port, shell=True)
        wb.open('http://google.co.kr', new=2)
    
    def stop(self):
        os.chdir(self.paths.projects_path+self.project_root)
        returned_value = subprocess.call("python -m http.server "+self.port, shell=True)