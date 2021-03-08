from Grid import *
from Task import *

class Board:
    # 依次遍历某个方块周围的8个格子
    DIR = [(0, -1), (1, 0), (0, 1), (0, 1), (-1, 0), (-1, 0), (0, -1), (0, -1)]
    N = 8

    def __init__(self, width, height):
        self.grd = [[Grid([i, j]) for j in range(height)] for i in range(width)]
        self.width = width
        self.height = height

    # 每次获取图像数据后，对格子相关数据进行更新
    # todo 对第一次输入设置死格子
    def Refresh(self, nums):
        for i in range(self.width):
            for j in range(self.height):
                if self.grd[i][j].isDead == True: # 跳过死格子
                    continue
                self.grd[i][j].status = nums[j][i]
        # 更新周围格子的信息
        for i in range(self.width):
            for j in range(self.height):
                if self.grd[i][j].isDead == True or self.grd[i][j].status == Grid.UNSOLVED: # 跳过死格子和未翻开格子
                    continue
                self.grd[i][j].numMine = 0
                self.grd[i][j].numUnsolved = 0
                tmpX, tmpY = i, j
                for k in range(self.N):
                    tmpX += self.DIR[k][0]
                    tmpY += self.DIR[k][1]
                    if tmpX < 0 or tmpX >= self.width or tmpY < 0 or tmpY >= self.height:
                        continue
                    if self.grd[tmpX][tmpY].status == Grid.MINE:
                        self.grd[i][j].numMine += 1
                    if self.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                        self.grd[i][j].numUnsolved += 1
    
    # 尝试求解数字格子
    def Solution(self) -> list[Task]:
        taskQueue = []
        for i in range(self.width):
            for j in range(self.height):
                if self.grd[i][j].isDead == True or self.grd[i][j].status == Grid.UNSOLVED:  # 跳过已死,旗子，没翻开，空白
                    continue
                # 策略一：一个格子周围未翻开的格子数等于剩余的雷数，将未翻开的全部插旗
                if self.grd[i][j].status == self.grd[i][j].numMine + self.grd[i][j].numUnsolved:
                    self.grd[i][j].isDead = True  # 标记该格子已解开
                    # todo 遍历周围八个格子没翻的全插
                    tmpX, tmpY = i, j
                    for k in range(self.N):
                        tmpX += self.DIR[k][0]
                        tmpY += self.DIR[k][1]
                        if tmpX < 0 or tmpX >= self.width or tmpY < 0 or tmpY >= self.height:
                            continue
                        if self.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))  # 右击该方块
                        # todo 对所有插旗方格调用Check函数更新并检查其四周的格子是否可解(optional)
                        pass 
                    continue
                # 策略二：一个格子四周的插旗数达到其数字，将未翻开的全部翻开
                if self.grd[i][j].status == self.grd[i][j].numMine:
                    self.grd[i][j].isDead = True  # 标记该格子已解开
                    # 遍历周围八个格子没翻的全翻开
                    tmpX, tmpY = i, j
                    for k in range(self.N):
                        tmpX += self.DIR[k][0]
                        tmpY += self.DIR[k][1]
                        if tmpX < 0 or tmpX >= self.width or tmpY < 0 or tmpY >= self.height:
                            continue
                        if self.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))  # 左击该方块
                    continue
                # 策略三：对于周围剩余雷数为1但未翻开的格子>=2的格子，对可选位置设置问号标记，并对与其共同相邻的格子进行推理
                pass


                # 策略四：当以上策略都失效时，结合剩余的雷数使用枚举法推理
                if len(taskQueue) == 0:
                    pass

        # 队列中操作去重
        tmpList = []
        for task in taskQueue:
            for item in tmpList:
                if task.pos == item.pos:
                    break
            else:
                tmpList.append(task)
        return tmpList

    # 当标记某个格子为地雷后，更新并检查其四周的格子是否可解 
    def Check(self):
        pass

    # dubug
    def Report(self):
        for i in range(self.width):
            for j in range(self.height):
                print('[%d, %d]: num = %d, mine = %d, unsolved = %d' % \
                    (i, j, self.grd[i][j].status, self.grd[i][j].numMine, self.grd[i][j].numUnsolved))



if __name__ == '__main__':
    lt = [
        [-2,1,0,0,0,0,0,0,0],
        [-2,1,0,0,0,0,1,1,1],
        [-2,2,1,0,0,1,3,-1,-2],
        [-2,-2,1,1,1,2,-2,-2,-2],
        [-2,-2,-2,-2,-2,-2,-2,-2,-2]
    ]
    x = Board(9, 5)
    x.Refresh(lt)
    # x.Report()
    ret1 = x.Solution()
    for task in ret1:
        print(task.__dict__)
