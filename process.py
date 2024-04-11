import numpy as np
f = open("statics.txt", "r")
i = 0
g = open("statics1.txt","w")
first = -1454.706371
temp = first
Step = 0.5
sum = 0#临时储存个数
while temp!= -1431.991503:
    strList=f.readline()
    temp = float(strList)#转化浮点格式
    if temp > first+Step*i and temp < first+Step*(i+1) :
        sum = sum + 1
    else:
        x = round(i*Step,5)
        g.write("{} \n".format( sum))
        i = i+1
        sum=0
f.close
g.close