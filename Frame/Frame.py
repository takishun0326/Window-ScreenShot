import tkinter as tk
from tkinter import ttk
from tkinter import *
from Window import WindowTitle
from Window import Screenshot
import threading
import subprocess

class Frame:

    def show_selection(self):
        for i in self.listbox.curselection():
            self.current_window_name = str(self.listbox.get(i))
            self.current_window['text'] = self.current_window_name + '　　を選択中'
    
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
                
        windows = WindowTitle.get_window_title()
        var = tk.StringVar(value=windows)
        self.listbox = tk.Listbox(self.frame, listvariable=var, height=10, width=80)

        self.listbox.bind('<<ListboxSelect>>', lambda e: self.show_selection())
        self.listbox.grid(row=0,column=0)

            # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.frame,
            orient=VERTICAL,
            command=self.listbox.yview)
        self.listbox['yscrollcommand'] = scrollbar.set
        scrollbar.grid(row=0, column=1, sticky=(N, S))

        # 設定ボタン
        self.title_select_button = ttk.Button(self.frame, text='設定', command=lambda: self.show_selection())
        self.title_select_button.grid(row=2, column=0)

        # 選択中のウィンドウ名
        self.current_window_name=''
        self.current_window = ttk.Label(self.frame, text='未設定')
        self.current_window.grid(row=5, column = 0)

        # n秒間に1回スクリーンショットをとるか
        self.set_interval_second = tk.DoubleVar(value=10.0)
        self.set_interval_second_label = ttk.Entry(self.frame, textvariable=self.set_interval_second, width = 6)
        self.set_interval_second_label.grid(row=7, column=0)
        self.set_interval_label = ttk.Label(self.frame, text="秒間に1回スクリーンショットを撮る")
        self.set_interval_label.grid(row=7, column=1)

        # スクリーンショットボタン
        scr = Screenshot.Screenshot()
        self.screenshot_button = ttk.Button(self.frame, text='スクリーンショット開始', command=self.pushed_execute_screenshot)
        self.screenshot_button.grid(row=8,column=0)
        # スクリーンショット
    
        # 保存場所指定    

        self.frame.grid(padx=30, pady=30)


        


    