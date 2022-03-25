import tkinter as tk
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
        
        # make tab
        self.frame = ttk.Frame(main_win)
        self.frame.grid()


        # n秒間に1回スクリーンショットをとるか
        self.set_interval_second = tk.DoubleVar(value=10.0)
        self.set_interval_second_label = ttk.Entry(self.frame, textvariable=self.set_interval_second, width = 6)
        self.set_interval_second_label.grid(row=7, column=0)
        self.set_interval_label = ttk.Label(self.frame, text="秒間に1回スクリーンショットを撮る")
        self.set_interval_label.grid(row=7, column=1)

        # スクリーンショットボタン
        self.screenshot_button = ttk.Button(self.frame, text='スクリーンショット開始', command=self.pushed_execute_screenshot)
        self.screenshot_button.grid(row=8,column=0)

        # スクリーンショット
    
        # 保存場所指定    

        self.frame.grid(padx=30, pady=30)


        


    