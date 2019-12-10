import datetime

class TextBox:
    Editbox = None
    Tkinter = None
    
    def __init__(self,Editbox,Tkinter):
        self.Editbox = Editbox
        self.Tkinter = Tkinter
    
    #設定したEditboxにスタンプを押す。
    def putSelfStamp(self,msg=""):
        self.putStamp(self.Editbox,msg)
    
    #Boxで指定したEditBoxにスタンプを押す。
    def putStamp(self,Box,msg=""):
        date = datetime.datetime.now()
        out = "[" + str(date.hour) + ":" + str(date.minute) + "]"+msg
        Box.insert(self.Tkinter.END,"\n")
        Box.insert(self.Tkinter.END,out)
    
    def putTodoStump(self):
        out = "\n[TODO]"
        self.Editbox.insert(self.Tkinter.END,out)
    
    #改行
    def putBreakLast(self,times = 1):
        for i in range(times):
            self.Editbox.insert(self.Tkinter.END,"\n")