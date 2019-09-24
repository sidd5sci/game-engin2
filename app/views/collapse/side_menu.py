
import wx
import wx.xrc
#----------------------------------------------------------------------

class SideMenu(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1,size = wx.Size( 250,600 ))

        self.cp = cp = wx.CollapsiblePane(self, label="Pointer",
                                          style=wx.CP_DEFAULT_STYLE|wx.CP_NO_TLW_RESIZE)
        self.pointerMenuContent(self.cp.GetPane())
        self.cp1 = cp1 = wx.CollapsiblePane(self, label="Object",
                                          style=wx.CP_DEFAULT_STYLE|wx.CP_NO_TLW_RESIZE)
        self.objectMenuContent(self.cp1.GetPane())

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(cp, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 25)
        sizer.Add(cp1, 0, wx.RIGHT|wx.LEFT|wx.EXPAND, 25)
        self.SetSizer(sizer)
        self.Layout()
    def pointerMenuContent(self, pane):
        '''Just make a few controls to put on the collapsible pane'''

        m_button2 = wx.Button( pane, wx.ID_ANY, u"X", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        m_button2.SetBackgroundColour( wx.Colour( 50, 74, 95 ) )
        
        m_button1 = wx.Button( pane, wx.ID_ANY, u"Move", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        m_button1.SetBackgroundColour( wx.Colour( 50, 74, 95 ) )

        addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        addrSizer.AddGrowableCol(1)
        
        addrSizer.Add(m_button1, 0,wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(m_button2, 0,wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)

        pane.SetSizer(addrSizer)
        # pane.Layout()

    def objectMenuContent(self, pane):
        '''Just make a few controls to put on the collapsible pane'''

       
        m_scrolledWindow4 = wx.ScrolledWindow(pane, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
        m_scrolledWindow4.SetScrollRate(5, 5)
        m_scrolledWindow4.SetMaxSize(wx.Size(250, -1))

        m_bpButton1 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/landscape.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        pane.Bind(wx.EVT_BUTTON, self.OnClickObject1, m_bpButton1)
        m_bpButton1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
            
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        bSizer1.Add(m_bpButton1)

        
        pane.SetSizer(bSizer1)
        # pane.Layout()
    def OnClickObject1(self,evt):
        pass
