import random
c = 7
fp = open("test.txt","w")
for i in range(c):
    fp.write("[")
    for j in range(c):
        var = str(random.randint(-2,0))
        fp.write(var)
        if j< c-1:
            fp.write(",")
    fp.write("]\n")
fp.close()