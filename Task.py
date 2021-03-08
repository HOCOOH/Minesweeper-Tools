class Task:
    def __init__(self, position: list[int]=[0, 0], operation: bool=False):
        self.pos = position    # 坐标
        self.op = operation     # 要执行的操作
        # op为True代表单击左键，op为False代表单击右键

    def Execute(self):
        