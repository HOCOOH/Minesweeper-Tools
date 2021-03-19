import time
import win32gui
import win32ui
import win32con
import win32api
import setting as s



class Window_Cut():

    def __init__(self, WINDOW_HEIGHT, WINDOW_WIDTH, SHOOT_POSITION):
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.SHOOT_POSITION = SHOOT_POSITION

    def work(self, ):
        start_position = self.SHOOT_POSITION#(132,145)  #(123,138)
        position = start_position #(start_position[0]+45*i,start_position[1]+45*j)
        #print(position)
        #print("{}{} shoot!".format(i,j))
        hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
        # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        hwndDC = win32gui.GetWindowDC(hwnd)
        # 根据窗口的DC获取mfcDC
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        # mfcDC创建可兼容的DC
        saveDC = mfcDC.CreateCompatibleDC()
        # 创建bigmap准备保存图片
        saveBitMap = win32ui.CreateBitmap()
        # 获取监控器信息
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = self.WINDOW_WIDTH#25
        h = self.WINDOW_HEIGHT#25
        a = position[0]
        b = position[1]
        #print(w,h)
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（w，h）的图片
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (a, b), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC,'./demo.png')


