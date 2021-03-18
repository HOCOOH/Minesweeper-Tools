import win32api
import setting as s
import win32con
import ctypes
import time

class Task:
    def __init__(self, position: list[int]=[0, 0], operation: bool=False):
        self.pos = position    # 坐标
        self.op = operation     # 要执行的操作
        # op为True代表单击左键，op为False代表单击右键

    def Execute(self):
        # 进行坐标的换算
        touch_pos = (419+self.pos[0]*(s.PIXEL_GAPX), 118+self.pos[1]*(s.PIXEL_GAPY))
        ctypes.windll.user32.SetCursorPos(int(touch_pos[0]),int(touch_pos[1]))

        if self.op == True:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
        time.sleep(0.02)