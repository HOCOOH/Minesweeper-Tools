from Board import *
import time

if __name__ == '__main__':
    # todo 点击屏幕中央的方格
    pass

    # 初始化棋盘
    width, height = 16
    board = Board(width, height)
    while True:
        # 获取图像数据
        pass

        # 算法分析
        nums = []
        board.Refresh(nums)
        tasks = board.Solution()
        for task in tasks:
            task.Execute()
        time.sleep(0.5)


