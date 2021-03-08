from Grid import *

class Board:
    def __init__(self, nums, height, width):
        self.grd = [[Grid([i, j], nums[i][j]) for j in range(height)] for i in range(width)]
        self.height = height
        self.width = width
'''
    def Scan(self):
        for i in range(self.height):
            for j in range(self.width):
                
'''



'''
if __name__ == '__main__':
    x = Board(2, 3)
    x.grd[1][1] = Grid([2, 3], 5)
    print(x.grd[1][1].status)
'''