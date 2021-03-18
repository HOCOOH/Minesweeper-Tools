import setting as s
import win32ui
import win32gui
import win32api
import win32con
import time


class Get_Window():

    def __init__(self, WINDOW_NAME):
        self.WINDOW_NAME = WINDOW_NAME
        
    def work(self,):
        wrHd=win32gui.FindWindow(None, self.WINDOW_NAME)
        win32gui.SetForegroundWindow(wrHd)
        win32gui.ShowWindow(wrHd,win32con.SW_MAXIMIZE)
        time.sleep(0.3)