import win32gui
wh = win32gui.FindWindow(None, 'Microsoft Minesweeper')

left = 0
top = 0
right = 0
bottom = 0
 
if wh:
    print("找到窗口")
    left, top, right, bottom = win32gui.GetWindowRect(wh)
    print("窗口坐标：")
    print(str(left)+' '+str(right)+' '+str(top)+' '+str(bottom))
else:
    print("未找到窗口")
