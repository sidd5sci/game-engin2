import wx,json
import importlib
# import Image 
class SideMenuPanel2(wx.Panel):

        def __init__(self, parent,*args):
                wx.Panel.__init__(self, parent)
                self.designer = args[0]


                self.SetBackgroundColour("#0C1821")

                m_scrolledWindow4 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
                m_scrolledWindow4.SetScrollRate( 5, 5 )
                m_scrolledWindow4.SetMaxSize( wx.Size( 250,620 ) )

                bSizer4 = wx.BoxSizer( wx.VERTICAL )
                
                objectLoader = importlib.import_module('controllers.object_load_controller','.')
                ol = objectLoader.ObjectLoader()
                object_list = ol.loadObjects()
                
                for o in object_list:
                    # print(o.name)
                    rs = json.loads(o.resources)
                    # png = wx.Image("resourses/"+rs["path"]+rs['sprites'][0], wx.BITMAP_TYPE_ANY).ConvertToBitmap()
                    m_bpButton1 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/"+rs["path"]+rs['sprites'][0], wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
                    m_bpButton1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
                    self.Bind(wx.EVT_BUTTON, lambda evt,temp=o.id: self.onObjectClick(evt,temp), m_bpButton1,o.id)
                    m_staticText1 = wx.StaticText( m_scrolledWindow4, wx.ID_ANY, u""+o.name, wx.DefaultPosition, wx.DefaultSize, 0 )
                    m_staticText1.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
                    m_staticText2 = wx.StaticText( m_scrolledWindow4, wx.ID_ANY, u"             ", wx.DefaultPosition, wx.DefaultSize, 0 )
                    
                    singleObjectSizer = wx.BoxSizer( wx.HORIZONTAL )
                    singleObjectSizer.Add(m_bpButton1,0, wx.ALL, 5 )
                    singleObjectSizer.Add(m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
                    singleObjectSizer.Add(m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


                    bSizer4.Add(singleObjectSizer, 1, wx.EXPAND | wx.ALL, 5)
               
                m_scrolledWindow4.SetSizer( bSizer4 )
                m_scrolledWindow4.Layout()
                bSizer4.Fit( m_scrolledWindow4 )
                # #  SetSizer(bSizer4)

        def onObjectClick(self,evt,id):
            # print(help(evt))
            self.designer.setObject(id)
            print("Button clicked",id)