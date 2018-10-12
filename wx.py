import wx
class App(wx.App):
	def onInit(self):
		frame = wx.Frame(parent=None,title='wx')
		frame =Show()
		return True

app = App()
app.MainLoop()
