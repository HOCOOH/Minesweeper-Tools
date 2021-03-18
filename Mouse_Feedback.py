import win32api
import setting as s
import win32con
import ctypes


class Mouse_Feedback():
    def __init__(self,PIXEL_GAPX,PIXEL_GAPY,PIXEL_SIZE,tasks):
        self.PIXEL_GAPX = PIXEL_GAPX
        self.PIXEL_GAPY = PIXEL_GAPY
        self.PIXEL_SIZE = PIXEL_SIZE
        self.tasks = tasks

    def work(self,):
        for task in tasks:
            pos = task.pos
            op = task.op
            # 进行坐标的换算
            touch_pos = (419 + pos[0] * (self.PIXEL_GAPX), 118 + pos[1] * (self.PIXEL_GAPY))
            ctypes.windll.user32.SetCursorPos(int(touch_pos[0]), int(touch_pos[1]))

            if op == True:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
