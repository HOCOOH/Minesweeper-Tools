    def Strategy4_2(self, tar:Grid, taskQueue: list):
        unfindmine_tmp = tar.status - tar.numMine#计数剩余雷
        unknown_tmp = tar.numUnknown#计数剩余未翻开
        unList = []
        #find unknown
        for k in self.GetAround(tar):
            if k.status == Grid.UNKNOW:
                unList.append(k.pos)

        #assert len(unList) == unknown_tmp
        i,j = tar.pos
        DIR = [(0, -1), (1, 0), (0, 1), (0, 1), (-1, 0), (-1, 0), (0, -1), (0, -1)]
        tarList = []
        for k in range(8):
            i += DIR[k][0]
            j += DIR[k][1]
            if i <0 or i >= self.width or j <0 or j >= self.height:
                continue
            if self.grd[i][j].status > 0 and tar.pos != [i,j] and self.grd[i][j].isDead == False:
                tarList.append(self.grd[i][j])
        for k in tarList:
            if k.status - k.numMine == unfindmine_tmp:
                for item in self.GetAround(k):
                    if item.status == Grid.UNKNOW and item.pos not in unList:
                        taskQueue.append(Task(item.pos,True))
                        print(item.pos,True)
                for p in unList:
                    if abs(p[0] - k.pos[0]) >1 or abs(p[1] - k.pos[1]) >1:
                        item = self.grd[p[0]][p[1]]
                        item.status = Grid.MINE
                        item.status = Grid.MINE
                        item.isDead = True
                        taskQueue.append(Task(item.pos, False))
                        print(item.pos, False)
                        self.mineLeft -= 1
                        self.Check(item, taskQueue)
                        # 直接退出
                        return
