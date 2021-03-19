from Board import *
from Get_Board_Info import *
from Get_Window import *
import time
import setting as s 

if __name__ == '__main__':
    # 初始化棋盘
    board = Board(s.SIZE, s.SIZE, s.MINE_TOTAL)
    scanner = Get_Board_Info(s.PIXEL_GAPX, s.PIXEL_GAPY, s.PIXEL_SIZE, s.CF, s.SIZE, \
        s.BLOCKS, s.CNT_THRESHOLD, s.WINDOW_POSITION_START, s.CELL_SIZE, s.BOARD_PIX_SIZE)
    # 点击屏幕中央的方格
    Get_Window(s.WINDOW_NAME).work()
    Task([7, 7], True).Execute()
    time.sleep(0.1)
    # for i in range(2):
    cnt = 1;
    while board.mineLeft > 0:
        print('Pass %2d' % cnt)
        cnt += 1
        # 获取图像数据
        boardInfo = scanner.work()
        # print(boardInfo)
        # 算法分析
        board.Refresh(boardInfo)
        tasks = board.Solution()
        if (len(tasks) == 0):
            break
        # 执行操作
        for task in tasks:
            print(task.__dict__)
            task.Execute()
        time.sleep(0.1)
    board.FinalCheck()
