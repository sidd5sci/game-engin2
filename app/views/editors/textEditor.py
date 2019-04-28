import wx
import wx.lib.dialogs
import wx.stc as stc
import os


# This is the class for the main editor window
class Editor(wx.Panel):
    def __init__(self, parent):
        # Variables
        self.dirname = ''
        self.filename = ''
        self.leftMarginWidth = 25
        self.lineNumbersEnabled = True

        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.control = stc.StyledTextCtrl(self, style=wx.TE_MULTILINE | 
        wx.TE_RICH2)

        self.control.StyleSetBackground(wx.stc.STC_STYLE_DEFAULT, (40, 40, 
        40))

        # Removes the horizontal scroll bar. 0 = off & 1 = on
        self.control.SetUseHorizontalScrollBar(show=0)

        # Setting the application icon
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("icon2.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        # Making the controls to scroll with 'CTRL' + scrolling with the 
        mousewheel
        self.control.CmdKeyAssign(ord('='), stc.STC_SCMOD_CTRL, 
        stc.STC_CMD_ZOOMIN)
        self.control.CmdKeyAssign(ord('-'), stc.STC_SCMOD_CTRL, s 
        tc.STC_CMD_ZOOMOUT)

        self.control.SetViewWhiteSpace(False)
        self.control.SetMargins(5, 0)
        self.control.SetMarginType(1, stc.STC_MARGIN_NUMBER)
        self.control.SetMarginWidth(1, self.leftMarginWidth)

        # Creating the status bar
        self.CreateStatusBar()
        self.StatusBar.SetBackgroundColour((62, 62, 62))

        # The buttons for the File menu thing
        filemenu = wx.Menu()
        menuNew = filemenu.Append(wx.ID_NEW, "&New", "Create a new 
        document")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open an existing 
        document")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "Save the current 
        document")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Save &As", "Save a new 
        document")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Exit the 
        application")

        # The buttons for the Edit menu thing
        editmenu = wx.Menu()
        menuUndo = editmenu.Append(wx.ID_UNDO, "&Undo", "Undo last action")
        menuRedo = editmenu.Append(wx.ID_REDO, "&Redo", "Redo last action")
        editmenu.AppendSeparator()
        menuSelectAll = editmenu.Append(wx.ID_SELECTALL, "&Select All", 
        "Select all text in the document")
        menuCut = editmenu.Append(wx.ID_CUT, "Cu&t", "Cut the selected 
        text")
        menuCopy = editmenu.Append(wx.ID_COPY, "&Copy", "Copy the selected 
        text")
        menuPaste = editmenu.Append(wx.ID_PASTE, "&Paste", "Paste the copied 
        text")

        # The buttons for the View menu thing
        viewmenu = wx.Menu()
        menuLineNumbers = viewmenu.Append(wx.ID_ANY, "Toggle &Line Numbers", 
        "Show/Hide line numbers column")

        # The buttons for the Help menu thing
        helpmenu = wx.Menu()
        menuGettingStarted = helpmenu.Append(wx.ID_ANY, "&Getting Started", 
        "Find online documentation")
        menuTutorials = helpmenu.Append(wx.ID_ANY, "&Tutorials", "Learn how 
        to use the editor")
        helpmenu.AppendSeparator()
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About", "Read about the 
        editor and PySavier")

        # Making the menu bar show up and make the names for the dropdowns
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(editmenu, "&Edit")
        menuBar.Append(viewmenu, "&View")
        menuBar.Append(helpmenu, "&Help")
        self.SetMenuBar(menuBar)

        # Setting the button events for the File dropdown
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Setting the button events for the Edit dropdown
        self.Bind(wx.EVT_MENU, self.OnUndo, menuUndo)
        self.Bind(wx.EVT_MENU, self.OnRedo, menuRedo)
        self.Bind(wx.EVT_MENU, self.OnSelectAll, menuSelectAll)
        self.Bind(wx.EVT_MENU, self.OnCut, menuCut)
        self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
        self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)

        # Setting the button event for the View dropdown
        self.Bind(wx.EVT_MENU, self.OnToggleLineNumbers, menuLineNumbers)

        # Updating the line and column text in the status bar. This happens 
        whenever the user releases a key
        self.control.Bind(wx.EVT_KEY_UP, self.LineColumn)

        self.Show(True)
        self.LineColumn(self)

    # Menu functions
    # The function for creating a new document
    def OnNew(self, e):
        self.filename = ''
        self.control.SetValue("")

    # The function for opening an existing document
    def OnOpen(self, e):
        try:
            dlg = wx.FileDialog(self, "Choose a file to open", self.dirname, "", "*.*", wx.FD_OPEN)
            if (dlg.ShowModal() == wx.ID_OK):
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'r')
                self.control.SetValue(f.read())
                f.close()
            dlg.Destroy()
        except:
            dlg = wx.MessageDialog(self, "Couldn't open the file", "Error", wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

    # The function for saving an existing document, (If it doesn't exist already, it does the same as 'Save As')
    def OnSave(self, e):
        try:
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue())
            f.close()
        except:
            try:
                dlg = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if (dlg.ShowModal() == wx.ID_OK):
                    self.filename = dlg.GetFilename()
                    self.dirname = dlg.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
                dlg.Destroy()
            except:
                pass

    # The function for saving a new document
    def OnSaveAs(self, e):
        try:
            dlg = wx.FileDialog(self, "Save file as", self.dirname, "Untitled", "PySavior file (*.psav)|*.psav|Python file (*.py)|*.py|C# file (*.cs)|*.cs|Java file (*.java)|*.java|HTML file (*.html)|*.html|CSS file (*.css)|*.css|Other|*",
                                wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if (dlg.ShowModal() == wx.ID_OK):
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                f = open(os.path.join(self.dirname, self.filename), 'w')
                f.write(self.control.GetValue())
                f.close()
            dlg.Destroy()
        except:
            pass

    # The function for closing/exiting the editor
    def OnExit(self, e):
        if self.control.IsModified():
            try:
                dlg = wx.FileDialog(self, "Save file as", self.dirname, "Untitled",
                                    "PySavior file (*.psav)|*.psav|Python file (*.py)|*.py|C# file (*.cs)|*.cs|Java file (*.java)|*.java|HTML file (*.html)|*.html|CSS file (*.css)|*.css|Other|*",
                                    wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
                if (dlg.ShowModal() == wx.ID_OK):
                    self.filename = dlg.GetFilename()
                    self.dirname = dlg.GetDirectory()
                    f = open(os.path.join(self.dirname, self.filename), 'w')
                    f.write(self.control.GetValue())
                    f.close()
                self.Close(true)
            except:
                pass
        else:
            exit()

    # The function for undo the last action
    def OnUndo(self, e):
        self.control.Undo()

    # The function for redo the last action
    def OnRedo(self, e):
        self.control.Redo()

    # The function for selecting the whole document
    def OnSelectAll(self, e):
        self.control.SelectAll()

    # The function for cutting/deleting the selected text
    def OnCut(self, e):
        self.control.Cut()

    # The function for copying the selected text to the clipboard
    def OnCopy(self, e):
        self.control.Copy()

    # The function for pasting the copied text from the clipboard
    def OnPaste(self, e):
        self.control.Paste()

    # The function for toggling on & off the line numbers, (the numbers at the left)
    def OnToggleLineNumbers(self, e):
        if (self.lineNumbersEnabled):
            self.control.SetMarginWidth(1, 0)
            self.lineNumbersEnabled = False
        else:
            self.control.SetMarginWidth(1, self.leftMarginWidth)
            self.lineNumbersEnabled = True

    # The function for updating and finding the current line and column
    def LineColumn(self, e):
        line = self.control.GetCurrentLine() + 1
        column = self.control.GetColumn(self.control.GetCurrentPos())
        textContent = "Line %s, Column %s" % (line, column)
        self.StatusBar.SetStatusText(textContent, 0)


app = wx.App(False)
frame = Editor(None, 'Savior - Text Editor')
app.MainLoop()