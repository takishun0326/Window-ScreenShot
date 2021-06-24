import sys
import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
from win32gui import GetWindowText, GetForegroundWindow

from Frame import Frame


if __name__ == '__main__':
    
    main_win = tk.Tk()
    main_win.title('自動スクリーンショット')
    main_win.geometry('700x600')
    #print(GetWindowText(GetForegroundWindow()))
    
    frame = Frame.Frame(main_win)

    main_win.mainloop()
    ImageGrab.grab().save('Image.png')