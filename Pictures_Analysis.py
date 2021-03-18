from PIL import Image
import numpy


class Pictures_Analysis():
    def __init__(self, CF, SIZE, BLOCKS, CNT_THRESHOLD, pixel_values, CELL_SIZE, BOARD_PIX_SIZE):
        self.CF = CF
        self.SIZE = SIZE
        self.BLOCKS = BLOCKS
        self.CNT_THRESHOLD = CNT_THRESHOLD
        self.pixel_values = pixel_values
        self.CELL_SIZE = CELL_SIZE
        self.BOARD_PIX_SIZE = BOARD_PIX_SIZE

    def pictures_analysis(self, p, q, position):
        width, height = self.CELL_SIZE, self.CELL_SIZE
        cnt_list={ 'unknown':0, 'flag':0, '0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0 }
        for c1 in range(width):
            for c2 in range(height):
                each_position = (int(position[0]) + c1, int(position[1]) + c2)
                for key,value in self.CF.items():
                    pixel_cell = self.pixel_values[each_position[1] * self.BOARD_PIX_SIZE+ each_position[0]]
                    if pixel_cell[0] in range(self.CF[key][0][0], self.CF[key][0][1]) and pixel_cell[1] in range(self.CF[key][1][0], self.CF[key][1][1]) and pixel_cell[2] in range(self.CF[key][2][0], self.CF[key][2][1]):
                        cnt_list[key] += 1
                        break;
        

        #print("demo{}{}".format(p, q)+" "+str(cnt_list))
        info_p_q = 0
        typical_type = max(cnt_list.values())
        for key in cnt_list.keys():
            if cnt_list[key] == typical_type and typical_type > self.CNT_THRESHOLD:
                 info_p_q = self.BLOCKS[key]
                 break
        #print(info_p_q)
        return info_p_q

    def work(self, p, q, position):
        return self.pictures_analysis(p,q,position)

