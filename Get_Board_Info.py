import setting as s

from PIL import Image
from PIL import ImageGrab

import time
import os

from Pictures_Analysis import Pictures_Analysis
from Window_Cut import Window_Cut
from Get_Window import Get_Window


class Get_Board_Info():

    def __init__(self, PIXEL_GAPX, PIXEL_GAPY, PIXEL_SIZE, CF, SIZE, BLOCKS, CNT_THRESHOLD, WINDOW_POSITION_START, CELL_SIZE, BOARD_PIX_SIZE):
        self.PIXEL_GAPX = PIXEL_GAPX
        self.PIXEL_GAPY = PIXEL_GAPY
        self.PIXEL_SIZE = PIXEL_SIZE
        self.CF = CF
        self.SIZE = SIZE
        self.BLOCKS = BLOCKS
        self.CNT_THRESHOLD = CNT_THRESHOLD
        self.WINDOW_POSITION_START = WINDOW_POSITION_START
        self.CELL_SIZE = CELL_SIZE
        self.BOARD_PIX_SIZE = BOARD_PIX_SIZE
        self.previous_board = []

    def board_refresh(self, Board_Info):
        self.previous_board = Board_Info

    def cal_unknown_cell(self):

        previous_unknown_cells = []
        if len(self.previous_board) != 0:
            for c1 in range(self.SIZE):
                for c2 in range(self.SIZE):
                    if (self.previous_board[c1][c2] == -2):
                        previous_unknown_cells.append((c1,c2))

            return previous_unknown_cells
        else:

            return []

    def get_single_info(self, c1, c2 ,pixel_values):

        position = (self.WINDOW_POSITION_START[0] + c2 * (self.PIXEL_GAPX), self.WINDOW_POSITION_START[1] + c1 * (self.PIXEL_GAPY));
        pictures_analysis = Pictures_Analysis(self.CF, self.SIZE, self.BLOCKS, self.CNT_THRESHOLD, pixel_values, self.CELL_SIZE, self.BOARD_PIX_SIZE)
        cell_info = pictures_analysis.work(c1, c2 , position)

        return cell_info

    def get_all_info(self,):
        
        window_get = Get_Window(s.WINDOW_NAME)
        window_get.work()
        
        window_cut = Window_Cut(self.PIXEL_GAPX, self.PIXEL_GAPY, self.PIXEL_SIZE, self.BOARD_PIX_SIZE)
        shoot = window_cut.work()

       

        im = Image.open("./demo.png",'r')
        pixel_values = list(im.getdata())

        previous_unknown_cells =  self.cal_unknown_cell()

        Board_Info = []

        if len(previous_unknown_cells) != 0:
            for cell in  previous_unknown_cells:
                self.previous_board[cell[0]][cell[1]] = self.get_single_info(cell[0], cell[1], pixel_values)
            Board_Info = self.previous_board

        else:
            for c1 in range(self.SIZE):
                temp = []
                for c2 in range(self.SIZE):
                    temp.append(self.get_single_info(c1, c2, pixel_values))
                Board_Info.append(temp)

        os.system('del *.png')

        self.board_refresh(Board_Info)
        return Board_Info

    def work(self,):
        return self.get_all_info()
    


if __name__ == '__main__':
    start = time.time()
    test = Get_Board_Info(s.PIXEL_GAPX,s.PIXEL_GAPY,s.PIXEL_SIZE,s.CF, s.SIZE, s.BLOCKS,s.CNT_THRESHOLD,s.WINDOW_POSITION_START, s.CELL_SIZE, s.BOARD_PIX_SIZE)
    Board_Info = test.work()
    for i in range(s.SIZE):
        print(Board_Info[i])
    end = time.time()
    print("Total:"+str(end-start))
