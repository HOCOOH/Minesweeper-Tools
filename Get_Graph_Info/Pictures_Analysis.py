from PIL import Image
import numpy

class Pictures_Analysis():
    def __init__(self, CF, SIZE, BLOCKS,CNT_THRESHOLD):
        self.CF = CF
        self.SIZE = SIZE
        self.BLOCKS = BLOCKS
        self.CNT_THRESHOLD = CNT_THRESHOLD

    def pictures_analysis(self,p,q):
        im = Image.open("./demo("+str(p)+str(q)+").png",'r') #demo(15,15).png demo(0,0).png
        width, height = im.size
        pixel_values = list(im.getdata())#所有像素点
        pixel_values = numpy.array(pixel_values).reshape((width, height, 3))    #重塑数组
        cnt_list={'unknown':0,'flag':0,'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0}


        for c1 in range(0,25):
            for c2 in range(0,25):
                for key,value in self.CF.items():
                    #print(key,value)
                    if pixel_values[c1][c2][0] in range(self.CF[key][0][0],self.CF[key][0][1]) and pixel_values[c1][c2][1] in range(self.CF[key][1][0],self.CF[key][1][1]) and pixel_values[c1][c2][2] in range(self.CF[key][2][0],self.CF[key][2][1]):
                        cnt_list[key]+=1
                        break
        
        #print("demo{}{}".format(p, q)+" "+str(cnt_list))
        info_p_q = 0
        typical_type = max(cnt_list.values())
        for key in cnt_list.keys():
            if cnt_list[key]==typical_type and typical_type > self.CNT_THRESHOLD:
                 info_p_q=self.BLOCKS[key]
                 break
        #print(info_p_q)
        return info_p_q

    def work(self, p,q):
        return self.pictures_analysis(p,q)

