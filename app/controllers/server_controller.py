

import importlib
import os,subprocess
import webbrowser as wb
import threading 

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
        self.server_thread = threading.Thread(target=self.server_start,name='local_server')


    def server_start(self):
        os.chdir(self.paths.projects_path+self.project_root)
        os.system("start .")
        returned_value = subprocess.call("python -m http.server "+self.port, shell=True)
        wb.get('chrome %s').open_new_tab('localhost:8080', new=2)
        os.system("start http://localhost:8080")
        print("Task 1 assigned to thread: {}".format(threading.current_thread().name)) 
        print("ID of process running task 1: {}".format(os.getpid())) 
        # returned_value = os.system("python -m http.server")

    def start(self):
        self.server_thread.start()

    def stop(self):
        self.server_thread.join()