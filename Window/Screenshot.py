from PIL import ImageGrab, Image
import win32gui 
import time
import sys

import win32ui
import win32con
import numpy as np
import cv2



class Screenshot:
        
        def __init__(self):
            self.interval_second = 3.0
            self.screenshots_counter = 0
            self.last_time = time.perf_counter()
            self.is_take_screenshots = False            


        def take_screenshot_enable(self,set_interval_second):
            print('interval: ' + str(set_interval_second))
            self.interval_second = set_interval_second
            self.is_take_screenshots = True

        def take_screenshot(self):
            if self.is_take_screenshots == True:
                #print(time.perf_counter())
                if time.perf_counter() - self.last_time >= self.interval_second:
                    self.screenshots_counter += 1
                    self.last_time = time.perf_counter()

                    ImageGrab.grab().save('imgs/' + str(self.screenshots_counter) +'.png')
                    # img = self.WindowCapture(title)
                    # Image.fromarray(img).save('imgs/' + str(self.screenshots_counter) +'.png')
                    print('\r' + str(self.screenshots_counter) + '枚撮った', end='')
                    

        def count_screenshots(self):
            return self.screenshots_counter

        # def WindowCapture(window_name: str, bgr2rgb: bool = False):
        #     # 現在アクティブなウィンドウ名を探す
        #     process_list = []

        #     def callback(handle, _):
        #         process_list.append(win32gui.GetWindowText(handle))
        #     win32gui.EnumWindows(callback, None)

        #     # ターゲットウィンドウ名を探す
        #     for process_name in process_list:
        #         if str(window_name) in process_name:
        #             hnd = win32gui.FindWindow(None, process_name)
        #             break
        #     else:
        #         # 見つからなかったら画面全体を取得
        #         hnd = win32gui.GetDesktopWindow()

        #     # ウィンドウサイズ取得
        #     x0, y0, x1, y1 = win32gui.GetWindowRect(hnd)
        #     width = x1 - x0
        #     height = y1 - y0
        #     # ウィンドウのデバイスコンテキスト取得
        #     windc = win32gui.GetWindowDC(hnd)
        #     srcdc = win32ui.CreateDCFromHandle(windc)
        #     memdc = srcdc.CreateCompatibleDC()
        #     # デバイスコンテキストからピクセル情報コピー, bmp化
        #     bmp = win32ui.CreateBitmap()
        #     bmp.CreateCompatibleBitmap(srcdc, width, height)
        #     memdc.SelectObject(bmp)
        #     memdc.BitBlt((0, 0), (width, height), srcdc, (0, 0), win32con.SRCCOPY)

        #     # bmpの書き出し
        #     if bgr2rgb is True:
        #         img = np.frombuffer(bmp.GetBitmapBits(True), np.uint8).reshape(height, width, 4)
        #         img = cv2.cvtColor(img, cv2.COLOR_bgr2rgb)
        #     else:
        #         img = np.fromstring(bmp.GetBitmapBits(True), np.uint8).reshape(height, width, 4)

        #     # 後片付け
        #     # srcdc.DeleteDC()
        #     memdc.DeleteDC()
        #     # win32gui.ReleaseDC(hnd, windc)
        #     win32gui.DeleteObject(bmp.GetHandle())

        #     return img



if __name__ == '__main__':
    args = sys.argv

    scr = Screenshot()

    # window_name = ''
    # for i in range(2,len(args)):
    #     window_name += args[i] + ' '
    # window_name.rstrip()

    # print(window_name)
    scr.take_screenshot_enable(float(args[1]))
    #hnd = win32gui.FindWindow(None, args[2])
    

    while(1):
        scr.take_screenshot()


