import setting as s
import win32ui
from PIL import Image
from PIL import ImageGrab
from Pictures_Analysis import Pictures_Analysis
from Window_Cut import Window_Cut
import threading
import time
from multiprocessing import Pool
import win32gui
import win32api
import win32con
import numpy
import os

#返回一个信号量，该计数器代表 初始值+release-acquare的值。每次调用acquare方法都会使内部计数器减一，
#一旦计数器为负的，则acquare方法会被阻塞，直到其他线程调用release方法，使信号量内部计数器值为正。
#简单来说的话就是保证锁能正常的被获得或者释放
s1=threading.Semaphore(200)
#====================

class Get_Board_Info():
    def __init__(self,PIXEL_GAPX,PIXEL_GAPY,PIXEL_SIZE,CF, SIZE, BLOCKS, CNT_THRESHOLD):
        self.PIXEL_GAPX = PIXEL_GAPX
        self.PIXEL_GAPY = PIXEL_GAPY
        self.PIXEL_SIZE = PIXEL_SIZE
        self.CF = CF
        self.SIZE = SIZE
        self.BLOCKS = BLOCKS
        self.CNT_THRESHOLD = CNT_THRESHOLD

        
    def get_single_info(self,i):
        
        s1.acquire()
        #print("shoot begin!!")
        each_res = []
        for j in range(self.SIZE):
            windows_cut = Window_Cut(self.PIXEL_GAPX,self.PIXEL_GAPY,self.PIXEL_SIZE)
            windows_cut.work(i,j)
            pictures_analysis = Pictures_Analysis(self.CF, self.SIZE, self.BLOCKS, self.CNT_THRESHOLD)
            each_res.append(pictures_analysis.work(i, j))
        s1.release()
        #print(each_res)
        return each_res

    def get_all_info(self,):
        wrHd=win32gui.FindWindow(None,'Microsoft Minesweeper')
        win32gui.SetForegroundWindow(wrHd)
        win32gui.ShowWindow(wrHd,win32con.SW_MAXIMIZE)
        time.sleep(0.5)

        start=time.time()
        pool = Pool(processes=self.SIZE)

        res = [] 
        for i in range(self.SIZE):
            res.append(pool.apply_async(self.get_single_info, (i,))) # 右边那个括号里是传run函数的参数
        pool.close()
        pool.join()

        os.system('del *.png')
        end=time.time()
        print(end-start)
        return res
    
    def work(self,):
       return self.get_all_info()
    
    def final_dealing(self,re):
        Board_Info = []
        for each_re in re:
            Board_Info.append(each_re.get())
        return Board_Info


'''

if __name__ == '__main__':
    test = Get_Board_Info(s.PIXEL_GAPX,s.PIXEL_GAPY,s.PIXEL_SIZE,s.CF, s.SIZE, s.BLOCKS,s.CNT_THRESHOLD)
    Board_Info = test.final_dealing(test.work())
    for i in range(16):
        print(Board_Info[i])

'''
