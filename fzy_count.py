import Grid
import Board

for i in range(width):
    for j in range(height):
        if self.grd[i][j].isDead == True &&  self.grd[i][j].status <= 0:#跳过已死,旗子，没翻开，空白
            continue
#===========================================================================================================================================
        #特殊2 1型排列
        if self.grd[i][j].statue - self.grd[i][j].numMine == 2 and self.grd[i][j].numUnsolved == 3:
            #遍历八个格子找到Unsolved 格子，将坐标对作为一个元素加入列表
            list a = [[]]
            list b = a
            list a_a = []
            temp_v = 2
            '''
            tmpX, tmpY = i,j
            for k in range(8):
                tmpX += self.DIR[k][0]
                tmpY += self.DIR[k][1]
                if tmpX < 0 or tmpX >= self.width or tmpY < 0 or tmpY >= self.height:
                    continue
            '''
            for k_3 in self.GetAround(self.grd[i][j]):
                #if self.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                if k_3.status == Grid.UNKNOWN:
                    #a.append([tmpX,tmpY])#语法可能错了
                    a.append([k.pos[0],k.pos[1]]) 

            #dirList= [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
            for k_4 in range 4:
                AA = dirList[k_4][0]
                BB = dirList[k_4][1]
                if self.grd[AA][BB].isDead == False and self.grd[AA][BB].statue - self.grd[AA][BB].numMine == 1:
                    for k_5 in self.GetAround(self.grd[AA][BB]):
                        if k_5.isDead == False and ([k_5.pos[0],k_5.pos[1]] in b):
                            b.remove([k_5.pos[0],k_5.pos[1]])
                        elif k_5.isDead == False:
                            a_a.append([k_5.pos[0],k_5.pos[1]])
                    if len(b) == 1:
                        taskQueue.append(Task(b[0],False))
                        for k_0 in range(len(a_a)):
                            taskQueue.append(Task(a_a[k_0],True))
                    b = a
                    a_a.clear
'''

            #上下左右的四个方向为1的活点
            if self.grd[i+1][j].isDead == False and self.grd[i+1][j].statue - self.grd[i+1][j].numMine == 1:
                #遍历八个点,没翻开的坐标在b列表中有的，从b中移除，b中没有的加入a_a列表
                tmpX, tmpY = i+1,j
                for k in range(8):
                    tmpX += self.DIR[k][0]
                    tmpY += self.DIR[k][1]
                    if tmpX < 0 or tmpX >= self.width or tmpY < 0 or tmpY >= self.height:
                        continue
                    if self.grd[tmpX][tmpY].isDead == False and ([tmpX,tmpY] in b):
                        b.remove([tmpX,tmpY])
                    elif self.grd[tmpX][tmpY].isDead == False:
                        a_a.append([tmpX,tmpY])

                #if 检查b列表的元素个数等于 1:
                if len(b) == 1:
                    #将这个b列表中的唯一坐标对应格子插旗，a_a列表中的剩余元素翻开
                    taskQueue.append(Task(b[0],False))
                    for k_0 in range(len(a_a)):
                        taskQueue.append(Task(a_a[k_0]),True)
                #b = a 恢复b列表 a_a清空
                b = a
                a_a.clear

            if self.grd[i-1][j].isDead == False and self.grd[i-1][j].statue - self.grd[i-1][j].numMine == 1:
                #遍历八个点,没翻开的坐标在b列表中有的，从b中移除，b中没有的加入a_a列表
                tmpX, tmpY = i-1,j
                for k in range(8):
                    tmpX += self.DIR[k][0]
                    tmpY += self.DIR[k][1]
                    if tmpX < 0 or tmpX >= self.width or tmpY < 0 or tmpY >= self.height:
                        continue
                    if self.grd[tmpX][tmpY].isDead == False and ([tmpX,tmpY] in b):
                        b.remove([tmpX,tmpY])
                    elif self.grd[tmpX][tmpY].isDead == False:
                        a_a.append([tmpX,tmpY])

                #if 检查b列表的元素个数等于 1:
                if len(b) == 1:
                    #将这个b列表中的唯一坐标对应格子插旗，a_a列表中的剩余元素翻开
                    taskQueue.append(Task(b[0],False))
                    for k_0 in range(len(a_a)):
                        taskQueue.append(Task(a_a[k_0]),True)
                #b = a 恢复b列表 a_a清空
                b = a
                a_a.clear

            if self.grd[i][j+1].isDead == False and self.grd[i][j+1].statue - self.grd[i][j+1].numMine == 1:
                #遍历八个点,没翻开的坐标在b列表中有的，从b中移除，b中没有的加入a_a列表
                tmpX, tmpY = i,j+1
                for k in range(8):
                    tmpX += self.DIR[k][0]
                    tmpY += self.DIR[k][1]
                    if tmpX < 0 or tmpX >= self.width or tmpY < 0 or tmpY >= self.height:
                        continue
                    if self.grd[tmpX][tmpY].isDead == False and ([tmpX,tmpY] in b):
                        b.remove([tmpX,tmpY])
                    elif self.grd[tmpX][tmpY].isDead == False:
                        a_a.append([tmpX,tmpY])

                #if 检查b列表的元素个数等于 1:
                if len(b) == 1:
                    #将这个b列表中的唯一坐标对应格子插旗，a_a列表中的剩余元素翻开
                    taskQueue.append(Task(b[0],False))
                    for k_0 in range(len(a_a)):
                        taskQueue.append(Task(a_a[k_0]),True)
                #b = a 恢复b列表 a_a清空
                b = a
                a_a.clear

            if self.grd[i][j-1].isDead == False and self.grd[i][j-1].statue - self.grd[i][j-1].numMine == 1:
                #遍历八个点,没翻开的坐标在b列表中有的，从b中移除，b中没有的加入a_a列表
                tmpX, tmpY = i,j-1
                for k in range(8):
                    tmpX += self.DIR[k][0]
                    tmpY += self.DIR[k][1]
                    if tmpX < 0 or tmpX >= self.width or tmpY < 0 or tmpY >= self.height:
                        continue
                    if self.grd[tmpX][tmpY].isDead == False and ([tmpX,tmpY] in b):
                        b.remove([tmpX,tmpY])
                    elif self.grd[tmpX][tmpY].isDead == False:
                        a_a.append([tmpX,tmpY])

                #if 检查b列表的元素个数等于 1:
                if len(b) == 1:
                    #将这个b列表中的唯一坐标对应格子插旗，a_a列表中的剩余元素翻开
                    taskQueue.append(Task(b[0],False))
                    for k_0 in range(len(a_a)):
                        taskQueue.append(Task(a_a[k_0]),True)
                #b = a 恢复b列表 a_a清空
                b = a
                a_a.clear
'''
