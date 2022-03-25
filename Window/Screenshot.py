from PIL import ImageGrab, Image
import time
import sys


class Screenshot:
        
        def __init__(self):
            self.interval_second = 3.0
            self.screenshots_counter = 0
            self.last_time = time.perf_counter()
            self.is_take_screenshots = False            


        def take_screenshot_enable(self,interval_second, times, dir):
            print('interval: ' + str(interval_second) + '  times:  ' + str(times))
            self.interval_second = interval_second / times
            self.save_dir = dir
            self.is_take_screenshots = True

        def take_screenshot(self):
            if self.is_take_screenshots == True:
                #print(time.perf_counter())
                if time.perf_counter() - self.last_time >= self.interval_second:
                    self.screenshots_counter += 1
                    self.last_time = time.perf_counter()
                    
                    # 一度元のサイズで保存
                    ImageGrab.grab().save(self.save_dir + '/' +str(self.screenshots_counter) +'.png')
                    
                    # リサイズ
                    img = Image.open(self.save_dir + '/' +str(self.screenshots_counter) +'.png')
                    img_resize = img.resize((256,256))
                    img_resize.save(self.save_dir + '/' +str(self.screenshots_counter) +'.png')

                    print('\r' + str(self.screenshots_counter) + '枚撮った', end='')
                    

        def count_screenshots(self):
            return self.screenshots_counter


if __name__ == '__main__':
    args = sys.argv

    scr = Screenshot()

    print(args)
    scr.take_screenshot_enable(float(args[1]), float(args[2]), str(args[3]))    

    while(1):
        scr.take_screenshot()


