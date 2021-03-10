import Grid
import Board

for i in range(width):
    for j in range(height):
        #插旗
        if Broad_o.grd[i][j].isDead == True &&  Broad_o.grd[i][j].status <= 0:#跳过已死,旗子，没翻开，空白
            continue
        if Broad_o.grd[i][j].status - Broad_o.grd[i][j].numMine == Broad_o.grd[i][j].numUnsolved: #活点，右键插旗
            Broad_o.grd[i][j].isDead = True #已死插满
            #push queue 遍历八个格子没插的全插,对所有插旗方格check函数检测当前旗子周围的数字进行连点左键

            
        if Broad_o.grd[i][j].status == Broad_o.grd[i][j].numMine:    #活点，左键翻开，旗插满可解但有未解的方格
            Broad_o.grd[i][j].isDead = True #已死插满
            #push queue 遍历八个格子没翻的全翻
#==========================================================================================================================================
        #特殊，广义1雷,两格没开恰好标问号
        if Broad_o.grd[i][j].status - Broad_o.grd[i][j].numMine == 1 and Broad_o.grd[i][j].numUnsolved == 2:
            #遍历八个格子返回找到这剩下的两个坐标，假设，x_0,y_0 x_1,y_1
            #预先设置雷
            Broad_o.grd[x_0][y_0].status = -2#假设插了个旗子
            Broad_o.grd[x_1][y_1].status = -2
            if abs(x_0 - x_1) == 2 and abs(y_0 - y_1) == 2:
                continue#无解对角线
            elif x_0 == x_1 and abs(y_0 - y_1)== 1:#上下挨着
                if Broad_o.grd[x_0+1][y_0].status - Broad_o.grd[x_0+1][y_0].numMine -1 ==0:
                    Broad_o.grd[x_0+1][y_0].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_0+1, y_0
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))
                if Broad_o.grd[x_0-1][y_0].status - Broad_o.grd[x_0-1][y_0].numMine -1 ==0:
                    Broad_o.grd[x_0-1][y_0].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_0-1, y_0
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))
                if Broad_o.grd[x_0+1][y_1].status - Broad_o.grd[x_0+1][y_1].numMine -1 ==0:
                    Broad_o.grd[x_0+1][y_1].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_0+1, y_1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))
                if Broad_o.grd[x_0-1][y_1].status - Broad_o.grd[x_0-1][y_1].numMine -1 ==0:
                    Broad_o.grd[x_0-1][y_1].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_0-1, y_1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))


                if Broad_o.grd[x_0+1][y_0].status - Broad_o[x_0+1][y_0].numMine - 1 == Broad_o.grd[x_0+1][y_0].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_0+1, y_0
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                if Broad_o.grd[x_0-1][y_0].status - Broad_o[x_0-1][y_0].numMine - 1 == Broad_o.grd[x_0-1][y_0].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_0-1, y_0
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                if Broad_o.grd[x_0+1][y_1].status - Broad_o[x_0+1][y_1].numMine - 1 == Broad_o.grd[x_0+1][y_1].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_0+1, y_1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                if Broad_o.grd[x_0-1][y_1].status - Broad_o[x_0-1][y_1].numMine - 1 == Broad_o.grd[x_0-1][y_1].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_0-1, y_1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                

            elif x_0 == x_1 and abs(y_0 - y_1)== 2:#上下隔着
                if Broad_o.grd[x_0+1][(y_0+y_1)/2].status - Broad_o.grd[x_0+1][(y_0+y_1)/2].numMine -1 ==0:
                    Broad_o.grd[x_0+1][(y_0+y_1)/2].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_0+1, (y_0+y_1)/2
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))
                if Broad_o.grd[x_0-1][(y_0+y_1)/2].status - Broad_o.grd[x_0-1][(y_0+y_1)/2].numMine -1 ==0:
                    Broad_o.grd[x_0-1][(y_0+y_1)/2].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_0-1, (y_0+y_1)/2
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))

                if Broad_o.grd[x_0+1][(y_0+y_1)/2].status - Broad_o[x_0+1][(y_0+y_1)/2].numMine - 1 == Broad_o.grd[x_0+1][(y_0+y_1)/2].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_0+1, (y_0+y_1)/2
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                if Broad_o.grd[x_0-1][(y_0+y_1)/2].status - Broad_o[x_0-1][(y_0+y_1)/2].numMine - 1 == Broad_o.grd[x_0-1][(y_0+y_1)/2].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_0-1, (y_0+y_1)/2
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                

            elif abs(x_0 - x_1)== 1 and y_0 == y_1:#左右挨着
                if Broad_o.grd[x_0][y_0+1].status - Broad_o.grd[x_0][y_0+1].numMine -1 ==0:
                    Broad_o.grd[x_0][y_0+1].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_0, y_0+1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))
                if Broad_o.grd[x_0][y_0-1].status - Broad_o.grd[x_0][y_0-1].numMine -1 ==0:
                    Broad_o.grd[x_0][y_0-1].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_0, y_0-1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))
                if Broad_o.grd[x_1][y_1+1].status - Broad_o.grd[x_1][y_1+1].numMine -1 ==0:
                    Broad_o.grd[x_1][y_1+1].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_1, y_0+1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))
                if Broad_o.grd[x_1][y_1-1].status - Broad_o.grd[x_1][y_1-1].numMine -1 ==0:
                    Broad_o.grd[x_1][y_1-1].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = x_1, y_0-1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))

                if Broad_o.grd[x_0][y_0+1].status - Broad_o[x_0][y_0+1].numMine - 1 == Broad_o.grd[x_0][y_0+1].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_0, y_0+1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                if Broad_o.grd[x_0][y_0-1].status - Broad_o[x_0][y_0-1].numMine - 1 == Broad_o.grd[x_0][y_0-1].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_0, y_0-1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                if Broad_o.grd[x_1][y_1+1].status - Broad_o[x_1][y_1+1].numMine - 1 == Broad_o.grd[x_1][y_1+1].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_1, y_1+1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                if Broad_o.grd[x_1][y_1-1].status - Broad_o[x_1][y_1-1].numMine - 1 == Broad_o.grd[x_1][y_1-1].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = x_1, y_1-1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))

                    

            elif abs(x_0 - x_1)== 2 and y_0 == y_1:#左右隔着
                if Broad_o.grd[(x_0+x_1)/2][y_0+1].status - Broad_o.grd[(x_0+x_1)/2][y_0+1].numMine -1 ==0:
                    Broad_o.grd[(x_0+x_1)/2][y_0+1].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = (x_0+x_1)/2 , y_0+1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))
                if Broad_o.grd[(x_0+x_1)/2][y_0-1].status - Broad_o.grd[(x_0+x_1)/2][y_0-1].numMine -1 ==0:
                    Broad_o.grd[(x_0+x_1)/2][y_0-1].isDead = True #已死插满
                    #push queue 遍历八个格子没翻的全翻
                    tmpX, tmpY = (x_0+x_1)/2 , y_0-1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], True))


                if Broad_o.grd[(x_0+x_1)/2][y_0+1].status - Broad_o.grd[(x_0+x_1)/2][y_0+1].numMine - 1 == Broad_o.grd[(x_0+x_1)/2][y_0+1].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = (x_0+x_1)/2 , y_0+1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))
                if Broad_o.grd[(x_0+x_1)/2][y_0-1].status - Broad_o.grd[(x_0+x_1)/2][y_0-1].numMine - 1 == Broad_o.grd[(x_0+x_1)/2][y_0-1].numUnsolved -2:
                    #仍是活点死不了
                    #push queue 遍历八个格子没插的全插
                    tmpX, tmpY = (x_0+x_1)/2 , y_0-1
                    for k in range(8):
                        tmpX += Broad_o.DIR[k][0]
                        tmpY += Broad_o.DIR[k][1]
                        if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                            continue
                        if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                            taskQueue.append(Task([tmpX, tmpY], False))

            Broad_o.grd[x_0][y_0].status = -1#保持未翻开
            Broad_o.grd[x_1][y_1].status = -1

#===========================================================================================================================================
        #特殊2 1型排列
        if Broad_o.grd[i][j].statue - Broad_o.grd[i][j].numMine == 2 and Broad_o.grd[i][j].numUnsolved == 3:
            #遍历八个格子找到Unsolved 格子，将坐标对作为一个元素加入列表
            list a = [[]]
            list b = a
            list a_a = []
            temp_v = 2
            tmpX, tmpY = i,j
            for k in range(8):
                tmpX += Broad_o.DIR[k][0]
                tmpY += Broad_o.DIR[k][1]
                if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                    continue
                if Broad_o.grd[tmpX][tmpY].status == Grid.UNSOLVED:
                    a.append([tmpX,tmpY])#语法可能错了


            #上下左右的四个方向为1的活点
            if Broad_o.grd[i+1][j].isDead == False and Broad_o.grd[i+1][j].statue - Broad_o.grd[i+1][j].numMine == 1:
                #遍历八个点,没翻开的坐标在b列表中有的，从b中移除，b中没有的加入a_a列表
                tmpX, tmpY = i+1,j
                for k in range(8):
                    tmpX += Broad_o.DIR[k][0]
                    tmpY += Broad_o.DIR[k][1]
                    if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                        continue
                    if Broad_o.grd[tmpX][tmpY].isDead == False and ([tmpX,tmpY] in b):
                        b.remove([tmpX,tmpY])
                    elif Broad_o.grd[tmpX][tmpY].isDead == False:
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

            if Broad_o.grd[i-1][j].isDead == False and Broad_o.grd[i-1][j].statue - Broad_o.grd[i-1][j].numMine == 1:
                #遍历八个点,没翻开的坐标在b列表中有的，从b中移除，b中没有的加入a_a列表
                tmpX, tmpY = i-1,j
                for k in range(8):
                    tmpX += Broad_o.DIR[k][0]
                    tmpY += Broad_o.DIR[k][1]
                    if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                        continue
                    if Broad_o.grd[tmpX][tmpY].isDead == False and ([tmpX,tmpY] in b):
                        b.remove([tmpX,tmpY])
                    elif Broad_o.grd[tmpX][tmpY].isDead == False:
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

            if Broad_o.grd[i][j+1].isDead == False and Broad_o.grd[i][j+1].statue - Broad_o.grd[i][j+1].numMine == 1:
                #遍历八个点,没翻开的坐标在b列表中有的，从b中移除，b中没有的加入a_a列表
                tmpX, tmpY = i,j+1
                for k in range(8):
                    tmpX += Broad_o.DIR[k][0]
                    tmpY += Broad_o.DIR[k][1]
                    if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                        continue
                    if Broad_o.grd[tmpX][tmpY].isDead == False and ([tmpX,tmpY] in b):
                        b.remove([tmpX,tmpY])
                    elif Broad_o.grd[tmpX][tmpY].isDead == False:
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

            if Broad_o.grd[i][j-1].isDead == False and Broad_o.grd[i][j-1].statue - Broad_o.grd[i][j-1].numMine == 1:
                #遍历八个点,没翻开的坐标在b列表中有的，从b中移除，b中没有的加入a_a列表
                tmpX, tmpY = i,j-1
                for k in range(8):
                    tmpX += Broad_o.DIR[k][0]
                    tmpY += Broad_o.DIR[k][1]
                    if tmpX < 0 or tmpX >= Broad_o.width or tmpY < 0 or tmpY >= Broad_o.height:
                        continue
                    if Broad_o.grd[tmpX][tmpY].isDead == False and ([tmpX,tmpY] in b):
                        b.remove([tmpX,tmpY])
                    elif Broad_o.grd[tmpX][tmpY].isDead == False:
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
