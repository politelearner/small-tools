import codecs #判断文件类型
def judgeTxt(file_name):
    data = open(file_name).read()
    if data[:3] == codecs.BOM_UTF8: 
        data = data[3:]
        print (data.decode("utf-8"))


def openreadtxt(file_name):
    data = []
    file = open(file_name,'r',encoding="UTF-8")  #打开文件
    file_data = file.readlines() #读取所有行
    for row in file_data:
        tmp_list = row.split() #按‘括号内容'切分每行的数据
        #tmp_list[-1] = tmp_list[-1].replace('\n','') #去掉换行符(目前不需要)
        data.append(tmp_list) #将每行数据插入data中
    return data

def cuttext(file_name , str):#注意是已读返回文件数据数组(文件名，特殊字符跳过一整行)
    data = openreadtxt(file_name)
     

if __name__=="__main__":
    data = openreadtxt('test.txt')
    print(data)
    print(type(data[1][0]),len(data[1][0]))
    #judgeTxt('test.txt')
