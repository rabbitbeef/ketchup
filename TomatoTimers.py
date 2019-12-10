import time
import math
import win32api
import concurrent.futures

class TomatoStamp:
    executor_timer=None
    executor_reset=None
    #リセットフラグ
    reset_flag = False
    #タイマーが実行中かどうか確認する。
    timer_running = False
    
    Editbox = None
    Tkinter = None
    TextBox = None
    
    def __init__(self,Editbox,Tkinter,TextBox = None):
        self.executor_timer = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.Editbox = Editbox
        self.Tkinter = Tkinter
        self.TextBox = TextBox

    #タイマーを外部呼出しする際にはこの関数を用いる。
    def tomatoTimer(self,timer_type):
        #タイマーリセット
        if self.timer_running:
            self.resetTimer()
        #タイマーの設定をセット
        settings=self.setTimer(timer_type)
        
        self.submitTimer(*settings)
    
         
    #TODO:新しくthreadを作るので上書きは達成されるが、
    #古くなったthreadを破棄できていないので、古いthreadを破棄できるようにする。
    def resetTimer(self):
        self.Editbox.delete('1.0',self.Tkinter.END)
        self.reset_flag =  True
        self.executor_timer.shutdown()
        self.executor_timer = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.TextBox.putSelfStamp("[reset]")
    
    #タイマーの種類毎に設定を切り分ける
    #NOTE:タイマーの設定の種類を追加するときはこの関数を変更
    def setTimer(self,timer_type_submit):
        interval=1
        timelimit=0.1
        EndMsg="default"
        timer_type="default"
        
        #print(timer_type_submit +" timer has started.")
        
        if(timer_type_submit=="tomato"):
            timelimit=25
            EndMsg="Tomato End"
            timer_type="tomato"
        elif(timer_type_submit=="Short"):
            timelimit=5
            EndMsg="Short Break End"
            timer_type="ShortBreak"
        elif(timer_type_submit=="Long"):
            timelimit=15
            EndMsg="Long Break End"
            timer_type="LongBreak"
            
        return[interval,timelimit,EndMsg,timer_type]
        
    #timerをthreadPoolにsubmitする
    def submitTimer(self,interval,timelimit,EndMsg,timer_type):    
        self.executor_timer.submit(self.timer,interval,timelimit,EndMsg,timer_type,self.Editbox,self.Tkinter)
    
    #タイマー開始時の行動
    def timerBegginAction(self,timer_type):
        if(self.TextBox != None):    
            self.TextBox.putBreakLast()
            self.TextBox.putSelfStamp('['+timer_type+']')
    
    #タイマーが正常終了した時の行動
    #リセット時は発動しない
    def timerEndAction(self,timer_type):
        if(self.TextBox != None):
            self.TextBox.putSelfStamp('['+timer_type+':End]')
        
    #タイマー関数。
    def timer(self,interval, limits_min ,EndMsg ,timer_type,  Editbox = None,tkinter = None):
        
        self.timer_running=True
        
        self.timerBegginAction(timer_type)

        first = time.time()
        #NOTE:更新間隔(interval)が１秒の場合、0.005を足さないと、１秒飛ばして表示されるので違和感がある。
        #     初期の処理が僅かに１秒以上かかるためだと思われる。
        #     0.005を足して表示の時間を僅かにずらして回避。
        #     これでも計算時間の誤差によっては、たまに表示される時間が１秒飛ぶ恐れがあるので、
        #     更新間隔を短くしてもよかったが、0.005秒と途中からの１秒飛ばしは人間の間隔では誤差レベルなのと、
        #     PCとしてはすこしでも負荷が少ない方をここでは選択した。
        end = first + 60 * limits_min+0.005
        now = now = time.time()
        next = 0
        
        while end >= now and not self.reset_flag and self.timer_running:

            # NOTE:待機時間設定までの以下の処理が
            # 　　intervalの時間以上かかる場合は、
            #     threadを設定して並列処理させること。
            #     そうでなければ、時間を超えた分、処理が飛ばされる。
            #   　但し今回の場合、
            #   　１秒以上処理時間がかからないので、
            #   　threadでの処理をしていない。
            past = end-now
            time_min = math.floor(past/60)
            sec = math.floor(past % 60)
            
            #出力用の文章成形
            string = '{minutes}:{second}'.format(minutes=time_min, second=sec)
            
            #tkinterとEditboxの両方がセットされていればEditboxに出力する。そうでなければprint
            if(Editbox and tkinter):
                Editbox.delete('1.0',tkinter.END)
                Editbox.insert(tkinter.END,string)
            else:
                print(string)
                
            # １秒ごとにループするように、待機時間を処理時間分だけ補正する。
            next = ((first-time.time()) % interval) or interval
            time.sleep(next)
            
            now = time.time()
            
        if not self.reset_flag:        
            self.timerEndAction(timer_type)
            win32api.MessageBox(0,EndMsg, 'Timer End')
            print("end")
        else:
            self.reset_flag = False
            
        self.timer_running=False