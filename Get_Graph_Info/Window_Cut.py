import time
import win32gui, win32ui, win32con, win32api
import setting as s
import pyautogui

class Window_Cut():

    def __init__(self,PIXEL_GAPX,PIXEL_GAPY,PIXEL_SIZE):
        self.PIXEL_GAPX = PIXEL_GAPX
        self.PIXEL_GAPY = PIXEL_GAPY
        self.PIXEL_SIZE = PIXEL_SIZE
        
    def work(self, i, j):
        position = (419+j*(self.PIXEL_GAPX), 118+i*(self.PIXEL_GAPY))
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
        w = int(self.PIXEL_SIZE)
        h = int(self.PIXEL_SIZE)
        a = int(position[0]) 
        b = int(position[1])
        #print(w,h)
        # 为bitmap开辟空间
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        # 高度saveDC，将截图保存到saveBitmap中
        saveDC.SelectObject(saveBitMap)
        # 截取从左上角（0，0）长宽为（w，h）的图片
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (a, b), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC,'./demo({}{}).png'.format(i,j))