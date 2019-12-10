import sys
import tkinter as tkinter
import tkinter.font as font
import datetime
import TextBox
import TomatoTimers

#スタンプボタンを押した時の動作
def push_stamp(event):
    text_box.putSelfStamp()

#保存ボタンを押した時の動作
def save_text(event):
    text = Editbox.get('1.0','end-1c')

    f = open(file_url,"w")
    f.write(text)
    f.close()

#TODO:TextBoxへの関数移行
def todo_stamp(event):
    date = datetime.datetime.now()
    out = "[TODO]\n"
    Editbox.insert('2.0',out)
    

#NOTE:外部変数のtomato(class TomatoStampのインスタンス)を参照している。
#     内部から引数で参照できるようにした方が疎結合になるが
#     方法が面倒くさそうなのでこれで実装しておく。
def tomato_stamp(event):
    tomato.tomatoTimer("tomato")

def short_stamp(event):
    tomato.tomatoTimer("Short")
    
def long_stamp(event):
    tomato.tomatoTimer("Long")

def reset_stamp(event):
    tomato.resetTimer()

#今日の日付を代入
today = datetime.date.today()

#読み込むファイルのurl
default = "./stamps/"
file_url = default + str(today)+".txt"

#GUI処理開始 + タイトル、サイズの設定
root = tkinter.Tk()
root.title("timestamp")
root.geometry("400x500")

#編集テキストボタンの設定
Editbox = tkinter.Text(width=50,height=23)
Editbox.pack(pady = 5)

#テキストの読み込み。失敗時は文章の先頭部分を記述する。
try:
    f = open(file_url,"r")
    content = f.read()
    f.close()
    text = content
except:
    text = str(today) + "\n"

Editbox.insert(tkinter.END,text)

#Editbox操作用のクラスのインスタンス化
text_box = TextBox.TextBox(Editbox,tkinter)

#スタンプ、保存用のボタンのフレーム
Button_Frame = tkinter.Frame(root)
Button_Frame.pack(fill = "both",padx = 20)
Button_Frame.pack(pady =5 )

#スタンプ作成ボタン
Button = tkinter.Button(Button_Frame,text = 'スタンプ',width=10)
Button.bind("<Button-1>",push_stamp)
Button.pack(side = 'left')

#TODO作成ボタン
Button = tkinter.Button(Button_Frame,text = 'TODO',width=10)
Button.bind("<Button-1>",todo_stamp)
Button.pack(side = 'left')

#セーブボタン
Button2 = tkinter.Button(Button_Frame,text = '保存',width=10)
Button2.bind("<Button-1>",save_text)
Button2.pack(side = 'right')

#
#トマトボタン
#

#スタンプ、保存用のボタンのフレーム
Button_Frame2 = tkinter.Frame(root)
Button_Frame2.pack(fill = "both",padx = 20)
Button_Frame2.pack(pady =5 )

#タイマー用のフレーム
Timer_Frame = tkinter.Frame(root)
Timer_Frame.pack(fill = "both",padx = 20,pady=20)
Timer_Frame.pack(pady =5 )
#タイマー用のfont
my_font = font.Font(root,family="System",size=90,weight="bold")


#トマトのタイマー用の窓
Editbox2 = tkinter.Text(Timer_Frame,width=50,height=10,font=my_font)
#トマトのタイマーを管理するクラスのインスタンス化
tomato = TomatoTimers.TomatoStamp(Editbox2,tkinter,text_box)

Button = tkinter.Button(Button_Frame2,text = 'Tomato',width=8)
Button.bind("<Button-1>",tomato_stamp)
Button.pack(fill='x',side = 'left')

Button = tkinter.Button(Button_Frame2,text = 'LongBreak',width=8)
Button.bind("<Button-1>",long_stamp)
Button.pack(fill='x',side = 'left')

Button = tkinter.Button(Button_Frame2,text = 'ShortBreak',width=8)
Button.bind("<Button-1>",short_stamp)
Button.pack(fill='x',side = 'left')

Button = tkinter.Button(Button_Frame2,text = 'Reset',width=8)
Button.bind("<Button-1>",reset_stamp)
Button.pack(fill='x',side = 'right')

Editbox2.pack(side='bottom',padx=20)



root.mainloop()