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

    # 返回某个格子所有周围格子的列表
    def GetAround(self, tar: Grid) -> list[Grid]:
        around = []
        tmpX, tmpY = tar.pos
        for k in range(self.N):
            tmpX += self.DIR[k][0]
            tmpY += self.DIR[k][1]
            if tmpX >= 0 and tmpX < self.width and tmpY >= 0 and tmpY < self.height:
                around.append(self.grd[tmpX][tmpY])
        return around

    # 每次获取图像数据后，对格子相关数据进行更新
    def Refresh(self, nums):
        for i in range(self.width):
            for j in range(self.height):
                if self.grd[i][j].status == Grid.UNSOLVED: # 更新未翻开的格子
                    self.grd[i][j].status = nums[j][i]
        # 更新周围格子的信息
        for i in range(self.width):
            for j in range(self.height):
                if self.grd[i][j].isDead == True or self.grd[i][j].status == Grid.UNSOLVED: # 跳过死格子和未翻开格子
                    continue
                self.grd[i][j].numMine = 0
                self.grd[i][j].numUnsolved = 0
                lt = self.GetAround(self.grd[i][j])
                for k in lt:
                    if k.status == Grid.MINE:
                        self.grd[i][j].numMine += 1
                    if k.status == Grid.UNSOLVED:
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
                    # 遍历周围八个格子没翻的全插
                    lt = self.GetAround(self.grd[i][j])
                    for k in lt:
                        if k.status == Grid.UNSOLVED:
                            k.status = Grid.MINE
                            k.isDead = True
                            taskQueue.append(Task(k.pos, False))  # 右击该方块
                            # 对所有插旗方格调用Check函数更新并检查其四周的格子是否可解(optional)
                            self.Check(k, taskQueue)
                    continue
                # 策略二：一个格子四周的插旗数达到其数字，将未翻开的全部翻开
                if self.grd[i][j].status == self.grd[i][j].numMine:
                    self.grd[i][j].isDead = True  # 标记该格子已解开
                    # 遍历周围八个格子没翻的全翻开
                    lt = self.GetAround(self.grd[i][j])
                    for k in lt:
                        if k.status == Grid.UNSOLVED:
                            taskQueue.append(Task(k.pos, True))  # 左击该方块
                    continue
                # 策略三：对于周围剩余雷数为1但未翻开的格子>=2的格子，对可选位置设置问号标记，并对与其共同相邻的格子进行推理
                pass

                # 策略四：当以上策略都失效时，结合剩余的雷数使用枚举法推理
                pass

        # 队列中操作去重
        tmpList = []
        for task in taskQueue:
            for item in tmpList:
                if task.pos == item.pos:
                    break
            else:
                tmpList.append(task)
        tmpList.sort(key=lambda x: x.op)
        return tmpList
        

    # 当标记某个格子为地雷后，更新并检查其四周的格子是否可解 
    def Check(self, tar: Grid, taskQueue: list[Task]):
        lt = self.GetAround(tar)
        for k in lt:
            if k.isDead == True or k.status == Grid.UNSOLVED:  # 跳过已死，没翻开
                continue
            # k是新插旗格子周围未解的数字格
            k.numMine += 1
            k.numUnsolved -= 1
            if k.status == k.numMine:
                k.isDead = True
                # 遍历周围八个格子没翻的全翻开
                ard = self.GetAround(k)
                for item in ard:
                    if item.status == Grid.UNSOLVED:
                        taskQueue.append(Task(item.pos, True))  # 左击该方块

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
