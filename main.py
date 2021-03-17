from Board import *
from Get_Board_Info import *
import time
import setting as s 

if __name__ == '__main__':
    # 点击屏幕中央的方格
    wrHd = win32gui.FindWindow(None, s.WINDOW_NAME)
    win32gui.SetForegroundWindow(wrHd)
    win32gui.ShowWindow(wrHd, win32con.SW_MAXIMIZE)
    time.sleep(0.2)
    Task([7, 7], True).Execute()
    time.sleep(0.2)

    # 初始化棋盘
    width, height = 16, 16
    board = Board(width, height)
    # for i in range(2):
    while True:
        # 获取图像数据
        test = Get_Board_Info(s.PIXEL_GAPX,s.PIXEL_GAPY,s.PIXEL_SIZE,s.CF, s.SIZE, s.BLOCKS,s.CNT_THRESHOLD)
        Board_Info = test.final_dealing(test.work())
        # 算法分析
        startTime = time.time()
        board.Refresh(Board_Info)
        tasks = board.Solution()
        endTime = time.time()
        print('solu: ' + str(endTime - startTime))
        if (len(tasks) == 0):
            break
        for task in tasks:
            # print(task.__dict__)
            task.Execute()
            time.sleep(0.02)
        time.sleep(0.2)
        

