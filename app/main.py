from paths import *
import os
import importlib
debuger = importlib.import_module('lib.debuger','.')
#import tkinter as tk
#from tkinter import ttk
##import views.view_node_editor as view
#from views.test2 import *
import wx

try:
    import views.view_main1 as view
except ImportError as error:
	# Output expected ImportErrors.
	print(error.__class__.__name__ + ": " + error.message)
	view = importlib.import_module('views.view_main1', '.')
except Exception as exception:
	# Output unexpected Exceptions.
	print(exception, False)
	print(exception.__class__.__name__ + ": " + exception.message)
	view = importlib.import_module('views.view_main1', '.')


def part(str, side):
    # split the tring by '.'
    name, ext = str.split('.')

    if side == 1:
        return name
    else:
        return ext


def load_lib():
    global libs, lib_names
    names = os.listdir(libs_path)
    for l in names:
        if l != '__pycache__':
            if part(l, 0) == 'py':
                LIB_NAME = 'lib.'+part(l, 1)
                # d.log('LIBS',LIB_NAME)
                lib_names.append(part(l, 1))
                # loading the libs
                libs.append(importlib.import_module(LIB_NAME, '.'))

    # debug message
    d.log("Loader", lib_names)


def find_module(str):
    global lib_names, libs

    k = [i for i in range(len(lib_names)) if lib_names[i] == str]
    return libs[k[0]]

#######################################################
### globals
#######################################################
d = debuger.debuger()
lib_names = list()
libs = list()

 
def main():
    # loading project
    project_module = importlib.import_module('controllers.project_controller','.')
    project = project_module.Project()
    p = project.openProject('snake')
    # loading scene
    scene_module = importlib.import_module('controllers.scene_controller','.')
    scene = scene_module.Scene()
    s = scene.loadScene(p.id)
    # loading layers
    layer_module = importlib.import_module('controllers.layer_controller','.')
    layers = layer_module.Layer()
    l = layers.loadLayer(s.id)

    # loading library
    load_lib()
    designer = find_module('designer').Designer(find_module('layer'),
                                find_module('camera'),
                                find_module('pointer'),
                                find_module('rect'),
                                find_module('tile'),
                                p,s,l, path=path,objectPath=objects_path)


    app = wx.App()
    view.MainWindow(None, "PyTrack V 1.0.1 | "+p.project_name, find_module('node'), designer)
    app.MainLoop()


if __name__ == "__main__":
	main()
