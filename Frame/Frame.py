import tkinter as tk
from tkinter import ttk
from Window import WindowTitle


class Frame:

    def show_selection(self):
        for i in self.listbox.curselection():
            print(self.listbox.get(i))

    def __init__(self, main_win):
        
        # make tab
        self.frame = ttk.Frame(main_win)
        self.frame.grid()
                
        windows = WindowTitle.get_window_title()
        var = tk.StringVar(value=windows)
        self.listbox = tk.Listbox(self.frame, listvariable=var, height=5, width=20)

        self.listbox.bind('<<ListboxSelect>>', lambda e: self.show_selection())
        self.listbox.grid(row=0,column=0)

        button = ttk.Button(self.frame, text='OK', command=lambda: self.show_selection(),)
        button.grid(row=0, column=1)
        self.frame.pack(padx=10, pady=20)
    