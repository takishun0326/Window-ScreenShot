import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *

import threading
import subprocess

from Window import Screenshot


class Frame:
    
    def pushed_execute_screenshot(self):
        thread1 = threading.Thread(target=self.execute_screenshot)  
        thread1.start()

    def execute_screenshot(self):
        try:
            res = subprocess.check_call('python Window/Screenshot.py ' + str(self.set_interval_second_label.get()) + ' ' + str(self.current_window_name))
        except:
            print ('Error')


    def __init__(self, main_win):
        
        # make Frames
        self.frame = ttk.Frame(main_win, padding=10)
        

        ###################         Frame 1         #####################
        
        # 「保存先」ラベルの作成
        self.IDirLabel = ttk.Label(self.frame, text="保存先>>")

        # 「フォルダ参照」エントリーの作成
        self.entry1 = StringVar()
        self.IDirEntry = ttk.Entry(self.frame, textvariable=self.entry1, width=30)

        # 「フォルダ参照」ボタンの作成
        self.IDirButton = ttk.Button(self.frame, text="参照", )#command=dirdialog_clicked)


        ###################         Frame 2         #####################

        # n秒間にp回スクリーンショットをとるか
        self.set_interval_second = tk.DoubleVar(value=3.0)
        self.interval_second_label = ttk.Entry(self.frame, textvariable=self.set_interval_second, width=5)
        self.interval_label1 = ttk.Label(self.frame, text="秒間に")

        self.set_screenshot_times = tk.DoubleVar(value=1)
        self.screenshot_times_label = ttk.Entry(self.frame, textvariable=self.set_screenshot_times, width=3)
        self.interval_label2 = ttk.Label(self.frame, text="回スクリーンショットを撮る")
        
        
        ###################         Frame 3         #####################

        # スクリーンショットボタン開始＆終了
        self.screenshot_start = tk.Button(self.frame, text="開始", command=self.pushed_execute_screenshot, font=("MSゴシック","11", "bold"),height=2, width=10, relief=SOLID)
        self.screenshot_finish = tk.Button(self.frame, text="終了", font=("MSゴシック", "11", "bold"),height=2, width=10, relief=SOLID)
  


        ############################################################################

        # Frameの位置
        self.frame.grid(row=0, column=0, sticky=W+E)
        # self.frame.grid(row=1, column=0, sticky=W+E)
        # self.frame.grid(row=2, column=0, rowspan=2, sticky=W+E)

        # widgetの配置
        self.IDirLabel.grid(row=0, column=0, sticky=W+E, pady=10)
        self.IDirEntry.grid(row=0, column=1, columnspan=3, sticky=W+E, pady=10)
        self.IDirButton.grid(row=0, column=4, sticky=W+E, padx=5, pady=10)

        self.interval_second_label.grid(row=1, column=0, sticky=N, pady=10)
        self.interval_label1.grid(row=1, column=1,sticky=N+S, pady=10)
        self.screenshot_times_label.grid(row=1, column=2,sticky=N, pady=10)
        self.interval_label2.grid(row=1, column=3, columnspan=2, sticky=NSEW, pady=10)

        self.screenshot_start.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=E, pady=10)
        self.screenshot_finish.grid(row=2, column=3, rowspan=2, columnspan=2, sticky=W, pady=10)


        


    