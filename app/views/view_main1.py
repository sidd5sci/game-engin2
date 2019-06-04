
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
import sys
from pygame.locals import *
import wx
import wx.xrc
import wx.aui
import wx.richtext
import wx.dataview
import wx.propgrid as pg
import os
import threading
import importlib
global pygame  # when we import it, let's keep its proper name!
global pygame_init_flag
pygame_init_flag = False

sys.path.insert(0, "..")
# from lxml import etree, objectify


class MainWindow(wx.Frame):
    def __init__(self, parent, title, *args):
        super(MainWindow, self).__init__(parent, title=title, size=(550, 550))

        self.node_module = args[0]
        self.designer = args[1]
        self.count = 0

        self.initEditor()

    def initEditor(self):

        #draw_button = wx.Button(self, label="Press Me")
        #self.Bind(wx.EVT_BUTTON, self.OnButtonPressed, draw_button)
        mb = self.MakeMenuBar()
        self.SetMenuBar(mb)
        self.CreateStatusBar()
        self.Maximize(True)
        self.Centre()
        self.Show()
        self.SetBackgroundColour(wx.Colour(12, 24, 33))

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_panel1 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        # side menu notebook
        self.side_menu = wx.Notebook(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        sideMenu1 = importlib.import_module('views.panels.side_menu','.')
        page1_menu = sideMenu1.SideMenuPanel(self.side_menu,self.designer)
        sideMenu2 = importlib.import_module('views.panels.side_menu2','.')
        page2_menu = sideMenu2.SideMenuPanel2(self.side_menu,self.designer)
        sideMenu3 = importlib.import_module('views.panels.side_menu3','.')
        page3_menu = sideMenu3.SideMenuPanel3(self.side_menu,self.designer)
        self.side_menu.AddPage(page1_menu,"Edit")
        self.side_menu.AddPage(page2_menu,"Objects")
        self.side_menu.AddPage(page3_menu,"Nodes")

        bSizer2.Add(self.side_menu, 1, wx.EXPAND | wx.ALL, 5)
        # notebook
        self.m_notebook1 = wx.Notebook(
            self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        page1 = PageOne(self.m_notebook1)
        page2 = PageTwo(self.m_notebook1, self.designer)
        page3 = PageThree(self.m_notebook1, self.node_module)
        page4 = PageFour(self.m_notebook1)

        self.m_notebook1.AddPage(page1, " Start ")
        self.m_notebook1.AddPage(page2, " Design ")
        self.m_notebook1.AddPage(page3, " Nodes ")
        self.m_notebook1.AddPage(page4, " Script Editor ")


        bSizer2.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)
        # panel for data tree and properties
        self.m_panel3 = wx.Panel(self.m_panel1, wx.ID_ANY,
                                 wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_treeCtrl1 = wx.TreeCtrl(
                self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)
        self.m_treeCtrl1.SetMinSize(wx.Size(200, 400))
        self.m_treeCtrl1.SetMaxSize(wx.Size(200, -1))

        self.root = self.m_treeCtrl1.AddRoot('Root')
        self.m_treeCtrl1.SetPyData(self.root, ('key', 'value'))
        self.m_treeCtrl1.AppendItem(self.root, 'Core')
        self.m_treeCtrl1.AppendItem(self.root, 'Objects')
        self.m_treeCtrl1.AppendItem(self.root, 'Events')
        self.m_treeCtrl1.AppendItem(self.root, 'Nodes')

        self.m_treeCtrl1.Expand(self.root)

        bSizer3.Add(self.m_treeCtrl1, 0, wx.ALL, 5)

        self.m_panel3.SetSizer(bSizer3)
        self.m_panel3.Layout()
        bSizer3.Fit(self.m_panel3)

        bSizer2.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)
        # adding sizers
        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        

        self.SetSizer(bSizer1)
        self.Layout()

    def onNewChild(self, evt):
        self.count += 1
        # try:
        #     child = ChildFrameSDL(self, self.count, "sdl", self.designer)
        #     # child = ChildFrameSDL(self.m_auinotebook1, self.count, "sdl", self.designer)
        # except Exception as data:
        #     print (data)

        # child.Show()

    def onDoClose(self, evt):
        self.Close()

    def onNewNode(self, evt):
        self.count += 1
        # child = ChildFrameSDL(self, self.count, "node", self.node_module)
        # child.Show()

    def onNewProject(self, evt):
        # child = MyDialog(self, "New Project").ShowModal()
        dialog = importlib.import_module('views.dialog.dialog_new_project', '.')
        dialog.MyDialog(self).ShowModal()

    def onOpenProject(self, evt):

        dialog = importlib.import_module('views.dialog.dialog_open_project', '.')
        dialog.MyDialog(self).ShowModal()

    def onSaveAsProject(self, evt):

        dialog = importlib.import_module('views.dialog.dialog_save_project', '.')
        dialog.MyDialog(self).ShowModal()
    
    def onRun(self, evt):
        server = importlib.import_module('controllers.server_controller','.')
        s = server.Server("snake","8000")
        s.start()

    def onStop(self, evt):
        server = importlib.import_module('controllers.server_controller','.')
        s = server.Server("snake","8000")
        s.stop()

    def MakeMenuBar(self):
        m_menubar1 = wx.MenuBar(0)
        m_menubar1.SetForegroundColour(
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
        m_menubar1.SetBackgroundColour(
                wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))

        m_File = wx.Menu()
        item = m_File.Append(-1, u"New Project\tCtrl-N")
        self.Bind(wx.EVT_MENU, self.onNewProject, item)
        item = m_File.Append(-1, u"Open Project\tCtrl-O")
        self.Bind(wx.EVT_MENU, self.onOpenProject, item)
        item = m_File.Append(-1, u"Close Project")
        m_File.AppendSeparator()
        item = m_File.Append(-1, u"Save ..\tCtrl-S")
        item = m_File.Append(-1, u"Save As ..\tCtrl-Shift-S")
        self.Bind(wx.EVT_MENU, self.onSaveAsProject, item)
        m_File.AppendSeparator()
        item = m_File.Append(-1, u"Import\tCtrl-M")
        item = m_File.Append(-1, u"Export\tCtrl-E")
        m_File.AppendSeparator()
        item = m_File.Append(-1, u"Close All")
        self.Bind(wx.EVT_MENU, self.onDoClose, item)

        m_menubar1.Append(m_File, u"File")

        m_Edit = wx.Menu()
        item = m_Edit.Append(-1, u"Undo\tCtrl-Z")
        item = m_Edit.Append(-1, u"Redo\tCtrl-Shift-Z")
        m_Edit.AppendSeparator()
        item = m_Edit.Append(-1, u"Cut\tCtrl-X")
        item = m_Edit.Append(-1, u"Copy\tCtrl-C")
        item = m_Edit.Append(-1, u"Paste\tCtrl-V")

        m_menubar1.Append(m_Edit, u"Edit")

        m_View = wx.Menu()
        item = m_View.Append(-1, u"Designer\tCtrl-D")
        self.Bind(wx.EVT_MENU, self.onNewChild, item)
        item = m_View.Append(-1, u"Node Editor\tCtrl-E")
        self.Bind(wx.EVT_MENU, self.onNewNode, item)

        m_menubar1.Append(m_View, u"View")

        m_Run = wx.Menu()
        item = m_Run.Append(-1, u"Run\tCtrl-shift-R")
        self.Bind(wx.EVT_MENU, self.onRun, item)
        item = m_Run.Append(-1, u"Stop\tCtrl-shift-S")
        self.Bind(wx.EVT_MENU, self.onStop, item)

        m_menubar1.Append(m_Run, u"Run")

        # mb = wx.MenuBar()
        # menu = wx.Menu()
        # item = menu.Append(-1, "New SDL child window\tCtrl-N")
        # self.Bind(wx.EVT_MENU, self.onNewChild, item)
        # item = menu.Append(-1, "New node window\tCtrl-N")
        # self.Bind(wx.EVT_MENU, self.onNewNode, item)
        # item = menu.Append(-1, "Close parent")
        # self.Bind(wx.EVT_MENU, self.onDoClose, item)
        # mb.Append(menu, "&View")

        self.SetMenuBar(m_menubar1)
        # return mb
        self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
        self.m_toolBar1.SetBackgroundColour("#1B2A41")

        self.m_toolBar1.AddSeparator()
        self.m_tool1 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"resourses\\UI\\document_add.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        self.m_tool2 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"resourses\\UI\\folder.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        self.m_tool3 = self.m_toolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"resourses\\UI\\Save_24x24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
        self.m_toolBar1.AddSeparator()

        self.m_toolBar1.Realize()
        self.Bind( wx.EVT_TOOL, self.onNewProject, id = self.m_tool1.GetId() )
        self.Bind( wx.EVT_TOOL, self.onOpenProject, id = self.m_tool2.GetId() )



        return m_menubar1


class XmlTree(wx.TreeCtrl):

        def __init__(self, parent, id, pos, size, style):
                wx.TreeCtrl.__init__(self, parent, id, pos, size, style)

                try:
                        with open(parent.xml_path) as f:
                                xml = f.read()
                except IOError:
                        print('Bad file')
                        return
                except Exception as e:
                        print('Really bad error')
                        print(e)
                        return

                self.xml_root = objectify.fromstring(xml)

                root = self.AddRoot(self.xml_root.tag)
                self.SetPyData(root, ('key', 'value'))

                for top_level_item in self.xml_root.getchildren():
                        child = self.AppendItem(root, top_level_item.tag)
                        self.SetItemHasChildren(child)
                        if top_level_item.attrib:
                                self.SetPyData(child, top_level_item.attrib)

                self.Expand(root)
                self.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.onItemExpanding)

        def onItemExpanding(self, event):
                item = event.GetItem()
                book_id = self.GetPyData(item)

                for top_level_item in self.xml_root.getchildren():
                        if top_level_item.attrib == book_id:
                                book = top_level_item
                                self.SetPyData(item, top_level_item)
                                self.add_book_elements(item, book)
                                break

        def add_book_elements(self, item, book):
                for element in book.getchildren():
                        child = self.AppendItem(item, element.tag)
                        if element.getchildren():
                                self.SetItemHasChildren(child)

                        if element.attrib:
                                self.SetPyData(child, element.attrib)


class TreePanel(wx.Panel):

        def __init__(self, parent):
                wx.Panel.__init__(self, parent)

                self.tree = MyTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                wx.TR_HAS_BUTTONS)

                sizer = wx.BoxSizer(wx.VERTICAL)
                sizer.Add(self.tree, 0, wx.EXPAND)
                self.SetSizer(sizer)


class PageOne(wx.Panel):
        def __init__(self, parent):
                wx.Panel.__init__(self, parent)
                self.SetBackgroundColour("#0C1821")
                font = wx.Font(pointSize=20, family=wx.MODERN, style=wx.NORMAL, weight=wx.FONTWEIGHT_BOLD)
                t = wx.StaticText(self, -1, " PyTrack \n Version 1.0.1", (20, 20))
                t.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
                t.SetFont(font)

class PageTwo(wx.Panel):
        def __init__(self, parent, *args):
                wx.Panel.__init__(self, parent)
                # t = wx.StaticText(self, -1, "This is a PageTwo object", (40, 40))
                p = SDLPanel(self, -1, (800, 680), args[0])


class PageThree(wx.Panel):
        def __init__(self, parent, *args):
                wx.Panel.__init__(self, parent)
                # t = wx.StaticText(self, -1, "This is a PageThree object", (60, 60))
                nde = importlib.import_module('views.node_app.nodeEditor', '.')
                p = nde.NodeEditor(self, -1, (800, 680), args[0])

class PageFour(wx.Panel):
        def __init__(self, parent):
                wx.Panel.__init__(self, parent)
                t = wx.StaticText(self, -1, "This is a Script Editor", (20, 20))
                # editor = importlib.import_module('views.editors.textEditor')
                # editor.Editor()
                self.SetBackgroundColour("#0C1821")
                bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
                self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
                bSizer7.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )
                self.SetSizer( bSizer7 )
                self.Layout()
                self.Centre( wx.BOTH )


class SDLThread:
        def __init__(self, designer):
                self.m_bKeepGoing = self.m_bRunning = False
                self.designer = designer
                self.color = (255, 0, 0)
                self.rect = (10, 10, 100, 100)
                self.thread = None
                self.init = True

        def Start(self):
                #I rewrote this to use the higherlevel threading module
                self.m_bKeepGoing = self.m_bRunning = True
                self.thread = threading.Thread(group=None, target=self.Run, name=None,
                                        args=(), kwargs={})
                self.thread.start()

        def Stop(self):
                self.m_bKeepGoing = False
                #this important line make sure that the draw thread exits before
                #pygame.quit() is called so there is no errors
                self.thread.join()

        def IsRunning(self):
                return self.m_bRunning

        def Run(self):
                while self.m_bKeepGoing:
                        # pygame logics
                        self.designer.main()
                self.m_bRunning = False
                print("pygame draw loop exited")


class SDLPanel(wx.Panel):
        def __init__(self, parent, ID, tplSize, *args):
                global pygame
                global pygame_init_flag
                wx.Panel.__init__(self, parent, ID, size=tplSize)
                self.Fit()
                os.environ['SDL_WINDOWID'] = str(self.GetHandle())
                os.environ['SDL_VIDEODRIVER'] = 'windib'
                #here is where things change if pygame has already been initialized
                #we need to do so again
                n = args[0]
                if pygame_init_flag:
                        #call pygame.init() on subsaquent windows
                        #pygame.init()
                        n.initPygame()
                else:
                        #import if this is the first time
                        import pygame

                n.initPygame()
                pygame_init_flag = True  # make sure we know that pygame has been imported
                #pygame.display.init()
                #window = pygame.display.set_mode(tplSize)
                self.thread = SDLThread(n)
                self.thread.Start()

        def __del__(self):
                self.thread.Stop()
                print("thread stoped")
                #very important line, this makes sure that pygame exits before we
                #reinitialize it other wise we get errors
                pygame.quit()


if __name__ == '__main__':
        app = wx.App()
        NodeEditor(None, 'PyTrack - V 1.0.1')
        app.MainLoop()
