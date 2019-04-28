import wx
import wx.lib.buttons as buts

class SideMenuPanel(wx.Panel):

        def __init__(self, parent,*args):
                wx.Panel.__init__(self, parent)
                self.designer = args[0]
                self.buttons = []

                self.SetBackgroundColour("#0C1821")

                m_scrolledWindow4 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
                m_scrolledWindow4.SetScrollRate( 5, 5 )
                m_scrolledWindow4.SetMaxSize( wx.Size( 250,-1 ) )
                # Main sizer
                bSizer4 = wx.BoxSizer( wx.VERTICAL )
                # Section pointer
                m_staticText1 = wx.StaticText( m_scrolledWindow4, wx.ID_ANY, u"Pointer", wx.DefaultPosition, wx.DefaultSize, 0 )
                m_staticText1.Wrap( -1 )
                m_staticText1.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
                bSizer4.Add( m_staticText1, 0, wx.ALL, 5 )

                bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

                m_button1 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/044-cursor-2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="move")
                self.Bind(wx.EVT_BUTTON, self.pointerSelect,m_button1)
                self.buttons.append(m_button1)
                
                m_button2 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/049-cursor-3.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="draw")
                self.Bind(wx.EVT_BUTTON, self.pointerDraw,m_button2)
                self.buttons.append(m_button2)
                
                bSizer5.Add(  m_button1, 0, wx.ALL, 5 )
                bSizer5.Add(  m_button2, 0, wx.ALL, 5 )


                bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
                # Section Shapes
                m_staticText2 = wx.StaticText(  m_scrolledWindow4, wx.ID_ANY, u"Shapes", wx.DefaultPosition, wx.DefaultSize, 0 )
                m_staticText2.Wrap( -1 )
                m_staticText2.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
                bSizer4.Add(  m_staticText2, 0, wx.ALL, 5 )

                bSizer61 = wx.BoxSizer( wx.VERTICAL )

                m_button3 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/026-add.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="addRect")
                self.Bind(wx.EVT_BUTTON, self.drawRect, m_button3)
                self.buttons.append(m_button3)

                m_button4 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/037-warning.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="addCircle")
                self.Bind(wx.EVT_BUTTON, self.drawRect, m_button4)
                self.buttons.append(m_button4)

                m_button5 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/022-circle-shape-outline.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="addTriangle")
                self.Bind(wx.EVT_BUTTON, self.drawRect, m_button5)
                self.buttons.append(m_button5)

                hrSizer = wx.BoxSizer( wx.HORIZONTAL )

                hrSizer.Add(  m_button3, 0, wx.ALL, 5 )
                hrSizer.Add(  m_button4, 0, wx.ALL, 5 )
                hrSizer.Add(  m_button5, 0, wx.ALL, 5 )

                bSizer61.Add(hrSizer,0,wx.ALL,5)
                bSizer4.Add( bSizer61, 1, wx.EXPAND, 5 )
                # section dimention
                m_staticText2 = wx.StaticText(  m_scrolledWindow4, wx.ID_ANY, u"Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
                m_staticText2.Wrap( -1 )
                m_staticText2.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
                bSizer4.Add(  m_staticText2, 0, wx.ALL, 5 )

                bSizer61 = wx.BoxSizer( wx.VERTICAL )

                m_button6 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/011-add-button.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="addLayer")
                self.Bind(wx.EVT_BUTTON, self.addLayer, m_button6)
                self.buttons.append(m_button6)
                
                m_button7 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/046-sort.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="upLayer")          
                self.Bind(wx.EVT_BUTTON, self.upLayer, m_button7)
                self.buttons.append(m_button7)

                m_button8 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/046-sort.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="downLayer")
                self.Bind(wx.EVT_BUTTON, self.downLayer, m_button8)
                self.buttons.append(m_button8)

                self.m_button9 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/001-hide.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="hide")
                self.Bind(wx.EVT_BUTTON, self.hideLayer, self.m_button9)
                self.buttons.append(self.m_button9)

                # self.m_genButton4 = buts.GenBitmapButton(self, -1, bitmap=wx.Bitmap("resourses/UI/unhide.png"),style=wx.NO_BORDER)                
                # self.m_genButton4.SetBackgroundColour("#0c1821")
                # self.Bind(wx.EVT_BUTTON, self.hideLayer, self.m_genButton4)
                # pause_button = buts.GenBitmapTextButton(self, -1, bitmap=wx.Bitmap("resourses/UI/add.png"), label= "")
                # pause_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )        
                hrSizer = wx.BoxSizer( wx.HORIZONTAL )

                hrSizer.Add(  m_button6, 0, wx.ALL, 5 )
                hrSizer.Add(  m_button7, 0, wx.ALL, 5 )
                hrSizer.Add(  m_button8, 0, wx.ALL, 5 )
                hrSizer.Add(  self.m_button9, 0, wx.ALL, 5 )


                bSizer61.Add(hrSizer,0,wx.ALL,5)
                bSizer4.Add( bSizer61, 1, wx.EXPAND, 5 )
                # section dimention
                m_staticText2 = wx.StaticText(  m_scrolledWindow4, wx.ID_ANY, u"Z index", wx.DefaultPosition, wx.DefaultSize, 0 )
                m_staticText2.Wrap( -1 )
                m_staticText2.SetForegroundColour( wx.Colour( 14, 124, 123 ) )
                bSizer4.Add(  m_staticText2, 0, wx.ALL, 5 )

                bSizer61 = wx.BoxSizer( wx.VERTICAL )

                m_button10 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/003-2-squares.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="backSend")
                self.Bind(wx.EVT_BUTTON, self.sendBack, m_button10)
                self.buttons.append(m_button10)

                m_button11 = wx.BitmapButton( m_scrolledWindow4, wx.ID_ANY, wx.Bitmap( u"resourses/UI/003-2-squares.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 ,name="frontSend")
                self.Bind(wx.EVT_BUTTON, self.sendFront, m_button11)
                self.buttons.append(m_button11)

                hrSizer = wx.BoxSizer( wx.HORIZONTAL )

                hrSizer.Add(  m_button10, 0, wx.ALL, 5 )
                hrSizer.Add(  m_button11, 0, wx.ALL, 5 )

                bSizer61.Add(hrSizer,0,wx.ALL,5)
                bSizer4.Add( bSizer61, 1, wx.EXPAND, 5 )
                # Transform


                #===================================
                m_scrolledWindow4.SetSizer( bSizer4 )
                m_scrolledWindow4.Layout()
                bSizer4.Fit( m_scrolledWindow4 )
                self.initButtons()
                # #  SetSizer(bSizer4)

        def initButtons(self):
            for i in range(0,len(self.buttons)):
                buttonName = self.buttons[i].GetName()
                self.buttons[i].SetWindowStyleFlag(wx.NO_BORDER)
                self.buttons[i].SetBackgroundColour("#1B2A41")

        def checkButton(self,name):
            for i in range(0,len(self.buttons)):
                buttonName = self.buttons[i].GetName()
                if buttonName == name:
                    self.buttons[i].SetBackgroundColour("#0E7C7B")
                else:
                    self.buttons[i].SetBackgroundColour("#1B2A41")

        def drawRect(self,evt):
            parent = evt.GetEventObject().GetParent().GetName()
            name = evt.GetEventObject().GetName()
            self.checkButton(name)

        def pointerSelect(self,evt):
            parent = evt.GetEventObject().GetParent().GetName()
            name = evt.GetEventObject().GetName()
            self.checkButton(name)
            self.designer.setPointer(2)

        def pointerDraw(self,evt):
            parent = evt.GetEventObject().GetParent().GetName()
            name = evt.GetEventObject().GetName()
            self.checkButton(name)
            self.designer.setPointer(1)
        
        def addLayer(self,evt):
            parent = evt.GetEventObject().GetParent().GetName()
            name = evt.GetEventObject().GetName()
            self.checkButton(name)
            self.designer.layer("add")

        def upLayer(self,evt):
            parent = evt.GetEventObject().GetParent().GetName()
            name = evt.GetEventObject().GetName()
            self.checkButton(name)
            self.designer.layer("up")

        def downLayer(self,evt):
            parent = evt.GetEventObject().GetParent().GetName()
            name = evt.GetEventObject().GetName()
            self.checkButton(name)
            self.designer.layer("down")

        def hideLayer(self,evt):
            state = self.designer.layer("hide")
            if state == 0:
                self.m_button9.SetBitmap(bitmap=wx.Bitmap("resourses/UI/hide.png"))
            else :
                self.m_button9.SetBitmap(bitmap=wx.Bitmap("resourses/UI/unhide.png"))
       
        def sendBack(self,evt):
            parent = evt.GetEventObject().GetParent().GetName()
            name = evt.GetEventObject().GetName()
            self.checkButton(name)
            self.designer.objectZindex("back")
            print("B..")

        def sendFront(self,evt):
            parent = evt.GetEventObject().GetParent().GetName()
            name = evt.GetEventObject().GetName()
            self.checkButton(name)
            self.designer.objectZindex("front")
            print("F..")
        