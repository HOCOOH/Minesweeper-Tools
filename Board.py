from Grid import *
from Task import *

class Board:
    # 依次遍历某个方块周围的8个格子
    DIR = [(0, -1), (1, 0), (0, 1), (0, 1), (-1, 0), (-1, 0), (0, -1), (0, -1)]
    N = 8

    def __init__(self, width, height, mineLeft):
        self.grd = [[Grid([i, j]) for j in range(height)] for i in range(width)]
        self.width = width
        self.height = height
        self.mineLeft = mineLeft

    # 返回某个格子所有周围格子的列表
    def GetAround(self, tar: Grid) -> list:
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
                if self.grd[i][j].status == Grid.UNKNOWN: # 更新未翻开的格子
                    self.grd[i][j].status = nums[j][i]
        # 更新周围格子的信息
        for i in range(self.width):
            for j in range(self.height):
                if self.grd[i][j].isDead == True or self.grd[i][j].status == Grid.UNKNOWN: # 跳过死格子和未翻开格子
                    continue
                self.grd[i][j].numMine = 0
                self.grd[i][j].numUnknown = 0
                for k in self.GetAround(self.grd[i][j]):
                    if k.status == Grid.MINE:
                        self.grd[i][j].numMine += 1
                    if k.status == Grid.UNKNOWN:
                        self.grd[i][j].numUnknown += 1

    # 尝试求解数字格子
    def Solution(self) -> list:
        taskQueue = []
        for i in range(self.width):
            for j in range(self.height):
                if self.grd[i][j].isDead == True or self.grd[i][j].status == Grid.UNKNOWN:  # 跳过已死,旗子，没翻开，空白
                    continue
                # 策略一：一个格子周围未翻开的格子数等于剩余的雷数，将未翻开的全部插旗
                if self.grd[i][j].status == self.grd[i][j].numMine + self.grd[i][j].numUnknown:
                    self.grd[i][j].isDead = True  # 标记该格子已解开
                    # 遍历周围八个格子没翻的全插
                    for k in self.GetAround(self.grd[i][j]):
                        if k.status == Grid.UNKNOWN:
                            k.status = Grid.MINE
                            k.isDead = True
                            taskQueue.append(Task(k.pos, False))  # 右击该方块
                            self.mineLeft -= 1
                            # 对所有插旗方格调用Check函数更新并检查其四周的格子是否可解
                            self.Check(k, taskQueue)
                    continue
                # 策略二：一个格子四周的插旗数达到其数字，将未翻开的全部翻开
                if self.grd[i][j].status == self.grd[i][j].numMine:
                    self.grd[i][j].isDead = True  # 标记该格子已解开
                    # 遍历周围八个格子没翻的全翻开
                    for k in self.GetAround(self.grd[i][j]):
                        if k.status == Grid.UNKNOWN:
                            taskQueue.append(Task(k.pos, True))  # 左击该方块
                    continue
        if len(taskQueue) == 0:
            print('ttttttttttttttttttttttttttttttttttttttttt')
            for i in range(self.width):
                for j in range(self.height):
                    if self.grd[i][j].isDead == True or self.grd[i][j].status == Grid.UNKNOWN:  # 跳过已死,旗子，没翻开，空白
                        continue
                    # 策略三：对于周围剩余雷数为1但未翻开的格子=2的格子，对可选位置设置问号标记，并对与其共同相邻的格子进行推理
                    if self.grd[i][j].status != Grid.MINE:
                        self.Strategy3(self.grd[i][j], taskQueue)
                        self.Strategy4(self.grd[i][j], taskQueue)
        



        # 策略五：当以上策略都失效时，结合剩余的雷数使用枚举法推理
        
        

        # 队列中操作去重并排序
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
    def Check(self, tar: Grid, taskQueue: list):
        for k in self.GetAround(tar):
            if k.isDead == True or k.status == Grid.UNKNOWN:  # 跳过已死，没翻开
                continue
            # k是新插旗格子周围未解的数字格
            k.numMine += 1
            k.numUnknown -= 1
            if k.status == k.numMine:
                k.isDead = True
                # 遍历周围八个格子没翻的全翻开
                for item in self.GetAround(k):
                    if item.status == Grid.UNKNOWN:
                        taskQueue.append(Task(item.pos, True))  # 左击该方块

    def GetTarList(self, lt: list, tar: Grid):
        x0, y0 = lt[0].pos
        x1, y1 = lt[1].pos
        originList = []
        if abs(x0 - x1) == 1 and y0 == y1:  # 左右挨着
            originList = [[x0, y0 + 1], [x0, y0 - 1], [x1, y1 + 1], [x1, y1 - 1]]
        elif abs(x0 - x1) == 2 and y0 == y1:  # 左右隔着
            originList = [[(x0 + x1) // 2, y0 + 1], [(x0 + x1) // 2, y0], [(x0 + x1) // 2, y0 - 1]]
        elif x0 == x1 and abs(y0 - y1) == 1:  # 上下挨着
            originList = [[x0 + 1, y0], [x0 - 1, y0], [x0 + 1, y1], [x0 - 1, y1]]
        elif x0 == x1 and abs(y0 - y1) == 2:  # 上下隔着
            originList = [[x0 + 1, (y0 + y1) // 2], [x0, (y0 + y1) // 2], [x0 - 1, (y0 + y1) // 2]]
        tarList = []
        for p in originList:
            if p[0] < 0 or p[0] >= self.width or p[1] < 0 or p[1] >= self.height:
                continue
            if self.grd[p[0]][p[1]].status > 0 and tar.pos != p and self.grd[p[0]][p[1]].isDead == False:
                tarList.append(self.grd[p[0]][p[1]])
        return tarList

    # 策略三：对于周围剩余雷数为1但未翻开的格子=2的格子，对可选位置设置问号标记，并对与其共同相邻的格子进行推理
    def Strategy3(self, tar: Grid, taskQueue: list):
        if tar.status - tar.numMine == 1 and tar.numUnknown == 2:
            # 遍历八个格子返回找到这剩下的两个坐标
            lt = []
            for k in self.GetAround(tar):
                if k.status == Grid.UNKNOWN:
                    lt.append(k)
            tarList = self.GetTarList(lt, tar)
            for k in tarList:
                if k.status - k.numMine - 1 == 0:  # 可以翻开
                    for item in self.GetAround(k):
                        if item.status == Grid.UNKNOWN and item.pos != lt[0].pos \
                            and item.pos != lt[1].pos:
                            taskQueue.append(Task(item.pos, True))
                    continue
                if k.status - k.numMine - 1 == k.numUnknown - 2:  # 可以插旗
                    for item in self.GetAround(k):
                        if item.status == Grid.UNKNOWN and item.pos != lt[0].pos \
                            and item.pos != lt[1].pos:
                            item.status = Grid.MINE
                            item.isDead = True
                            taskQueue.append(Task(item.pos, False))
                            self.mineLeft -= 1
                            self.Check(item, taskQueue)

    
    def Strategy4(self, tar: Grid, taskQueue: list):
        if tar.status - tar.numMine == 2 and tar.numUnknown == 3:
            unList = []
            #遍历八个格子找到Unknown格子，将坐标对作为一个元素加入列表
            for k in self.GetAround(tar):
                if k.status == Grid.UNKNOWN:
                    unList.append(k.pos)
            # 三个unknown格子要位于同一行或同一列
            assert len(unList) == 3
            if not ((unList[0][0] == unList[1][0] and unList[0][0] == unList[2][0]) or \
                (unList[0][1] == unList[1][1] and unList[0][1] == unList[2][1])):
                return
            i, j = tar.pos
            originList = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
            tarList = []
            for p in originList:
                if p[0] < 0 or p[0] >= self.width or p[1] < 0 or p[1] >= self.height:
                    continue
                if self.grd[p[0]][p[1]].status > 0 and tar.pos != p and self.grd[p[0]][p[1]].isDead == False:
                    tarList.append(self.grd[p[0]][p[1]])
            for k in tarList:
                if k.status - k.numMine - 1 == 0:
                    # 翻开格子
                    for item in self.GetAround(k):
                        if item.status == Grid.UNKNOWN and item.pos not in unList:
                            taskQueue.append(Task(item.pos, True))
                            print(item.pos, True)
                    # 插旗
                    for p in unList:
                        if abs(p[0] - k.pos[0]) > 1 or abs(p[1] - k.pos[1]) > 1:
                            item = self.grd[p[0]][p[1]]
                            item.status = Grid.MINE
                            item.isDead = True
                            taskQueue.append(Task(item.pos, False))
                            print(item.pos, False)
                            self.mineLeft -= 1
                            self.Check(item, taskQueue)
                            # 直接退出
                            return


    def FinalCheck(self):
        if self.mineLeft != 0:
            return
        for i in range(self.width):
            for j in range(self.height):
                if self.grd[i][j].status == Grid.UNKNOWN:
                    Task([i, j], True).Execute()

    # dubug
    def Report(self):
        for i in range(self.width):
            for j in range(self.height):
                print('[%d, %d]: num = %d, mine = %d, unsolved = %d' % \
                    (i, j, self.grd[i][j].status, self.grd[i][j].numMine, self.grd[i][j].numUnknown))


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
