import tkinter
import tkinter.font as font
import datetime
import TextBox
import TomatoTimers

#スタンプボタンを押した時の動作
def push_stamp(event):
    text_box.putSelfStamp()

#保存ボタンを押した時の動作
def save_text(event):
    text = Editbox_text.get('1.0','end-1c')

    f = open(file_url,"w")
    f.write(text)
    f.close()

#TODO:TextBoxへの関数移行
def todo_stamp(event):
    text_box.putTodoStump()

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

#GUI処理開始 + タイトル、サイズの設定 +　ファビコン設定
root = tkinter.Tk()
root.title("Ketchup")
root.geometry("400x530")
iconfile = 'favicon.ico'
root.iconbitmap(default=iconfile)

#編集テキスト用のフレーム
text_frame = tkinter.Frame(root,)
text_frame.pack(fill="both",side="top",padx=5,pady=5,ipadx=2,expand=1)

#編集テキストの設定
Editbox_text = tkinter.Text(text_frame,padx=10,pady=10)

#スクロールバーの設定
#scrollbar→Editboxの関連付け
scrollbar = tkinter.Scrollbar(
   text_frame,
   orient=tkinter.VERTICAL,
   command=Editbox_text.yview
)
#Editbox→scrollbarの関連付け
Editbox_text["yscrollcommand"]=scrollbar.set
scrollbar.pack(side="right",fill='y',expand=0,padx=0)

#Editboxのpack. scrollbarの後にpackしなければ,scrollbarが隠れてしまう.
Editbox_text.pack(padx=0,pady = 5,side="right",fill='both',expand=1)

#テキストの読み込み。失敗時は文章の先頭部分を記述する。
try:
    f = open(file_url,"r")
    content = f.read()
    f.close()
    text = content
except:
    text = str(today) + "\n"

Editbox_text.insert(tkinter.END,text)

#Editbox操作用のクラスのインスタンス化
text_box = TextBox.TextBox(Editbox_text,tkinter)

#スタンプ、保存用のボタンのフレーム
textbox_button_frame = tkinter.Frame(root)
textbox_button_frame.pack(fill='x',padx = 20,pady=5,expand=0)

#スタンプ作成ボタン
Button = tkinter.Button(textbox_button_frame,text = 'TimeStamp',width=10)
Button.bind("<Button-1>",push_stamp)
Button.pack(side = 'left',padx=1)

#TODO作成ボタン
Button = tkinter.Button(textbox_button_frame,text = 'TODO',width=10)
Button.bind("<Button-1>",todo_stamp)
Button.pack(side = 'left',padx=1)

#セーブボタン
Button2 = tkinter.Button(textbox_button_frame,text = 'save',width=10)
Button2.bind("<Button-1>",save_text)
Button2.pack(side = 'right',padx=1)

#
#タイマー
#
#タイマー全体のフレーム
timer_frame = tkinter.Frame(root,relief="sunken",border=4)
timer_frame.pack(fill="x",side="top",pady =3,padx=5,expand=0)

#タイマー用のボタンのフレーム
timer_button_frame = tkinter.Frame(timer_frame)
timer_button_frame.pack(fill="x",padx = 20,pady=2)

#タイマー用のテキスト用のフレーム
timer_text_frame = tkinter.Frame(timer_frame)
timer_text_frame.pack(fill='x',pady=1)

#タイマー用のfont
my_font = font.Font(timer_frame,family="System",size=70,weight="bold")


#トマトのタイマー用の窓
#Editbox_text = tkinter.Text(text_frame,padx=10,pady=10)
#Editbox_text.pack(pady = 5,side="left",fill='both',expand=1)
Editbox_timer = tkinter.Text(timer_text_frame,width=50,height=1,font=my_font)
Editbox_timer.pack(padx=5,side="top",fill='x',expand=0)
#トマトのタイマーを管理するクラスのインスタンス化
tomato = TomatoTimers.TomatoStamp(Editbox_timer,tkinter,text_box)

Button = tkinter.Button(timer_button_frame,text = 'Tomato',width=8)
Button.bind("<Button-1>",tomato_stamp)
Button.pack(side = 'left',padx=1)

Button = tkinter.Button(timer_button_frame,text = 'LongBreak',width=8)
Button.bind("<Button-1>",long_stamp)
Button.pack(side = 'left',padx=1)

Button = tkinter.Button(timer_button_frame,text = 'ShortBreak',width=8)
Button.bind("<Button-1>",short_stamp)
Button.pack(side = 'left',padx=1)

Button = tkinter.Button(timer_button_frame,text = 'Reset',width=8)
Button.bind("<Button-1>",reset_stamp)
Button.pack(side = 'right',padx=1)

root.mainloop()