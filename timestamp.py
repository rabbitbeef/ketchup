import sys
import tkinter as tkinter
import datetime

#スタンプボタンを押した時の動作
def push_stamp(event):
    date = datetime.datetime.now()
    out = "[" + str(date.hour) + ":" + str(date.minute) + "]"
    Editbox.insert(tkinter.END,"\n")
    Editbox.insert(tkinter.END,out)

#保存ボタンを押した時の動作
def save_text(event):
    text = Editbox.get('1.0','end-1c')

    f = open(file_url,"w")
    f.write(text)
    f.close()

#今日
today = datetime.date.today()

#ファイルのurl
default = "./stamps/"
file_url = default + str(today)+".txt"

#GUI処理開始 + タイトル、サイズ
root = tkinter.Tk()
root.title("timestamp")
root.geometry("400x400")

#編集テキストボタン
Editbox = tkinter.Text(width=50,height=23)
Editbox.pack(pady = 5)

#テキストの読み込み
try:
    f = open(file_url,"r")
    content = f.read()
    f.close()
    text = content
except:
    text = str(today) + "\n"

Editbox.insert(tkinter.END,text)

#ボタン用のフレーム
Button_Frame = tkinter.Frame(root)
Button_Frame.pack(fill = "both",padx = 20)
Button_Frame.pack(pady =5 )

#スタンプ作成ボタン
Button = tkinter.Button(Button_Frame,text = 'スタンプ',width=10)
Button.bind("<Button-1>",push_stamp)
Button.pack(side = 'left')

#セーブボタン
Button2 = tkinter.Button(Button_Frame,text = '保存',width=10)
Button2.bind("<Button-1>",save_text)
Button2.pack(side = 'right')

root.mainloop()