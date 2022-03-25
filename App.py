import sys
import tkinter as tk
from tkinter import messagebox
from Frame import Frame

if __name__ == '__main__':
    
    main_win = tk.Tk()
    main_win.title('自動スクリーンショット')
    main_win.geometry('350x190')
    #print(GetWindowText(GetForegroundWindow()))
    
    frame = Frame.Frame(main_win)

    main_win.mainloop()