import datetime

class TextBox:
    Editbox = None
    Tkinter = None
    
    def __init__(self,Editbox,Tkinter):
        self.Editbox = Editbox
        self.Tkinter = Tkinter
    
    def putSelfStamp(self,msg=""):
        self.putStamp(self.Editbox,msg)
    
    def putStamp(self,Box,msg=""):
        date = datetime.datetime.now()
        out = "[" + str(date.hour) + ":" + str(date.minute) + "]"+msg
        Box.insert(self.Tkinter.END,"\n")
        Box.insert(self.Tkinter.END,out)
        
    def putBreakLast(self):
        self.Editbox.insert(self.Tkinter.END,"\n")