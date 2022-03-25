from PIL import ImageGrab, Image
import time
import sys


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


if __name__ == '__main__':
    args = sys.argv

    scr = Screenshot()

    scr.take_screenshot_enable(float(args[1]))    

    while(1):
        scr.take_screenshot()


