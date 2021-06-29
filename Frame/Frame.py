import tkinter as tk
from tkinter import ttk
from tkinter import *
from Window import WindowTitle

from PIL import ImageGrab
from win32gui import GetWindowText, GetForegroundWindow

class Frame:

    def show_selection(self):
        for i in self.listbox.curselection():
            self.current_window['text'] = str(self.listbox.get(i)) + '　　を選択中'

    def take_screenshot(self):
        ImageGrab.grab().save('Image.png')
        

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

        self.title_select_button = ttk.Button(self.frame, text='設定', command=lambda: self.show_selection())
        self.title_select_button.grid(row=2, column=0)

        self.current_window = ttk.Label(text='未設定')
        self.current_window.grid(row=5, column = 0)

        
        self.screenshot_button = ttk.Button(self.frame, text='スクリーンショット開始', command=self.take_screenshot)
        self.screenshot_button.grid(row=6,column=1)
        

        self.frame.grid(padx=30, pady=30)
    