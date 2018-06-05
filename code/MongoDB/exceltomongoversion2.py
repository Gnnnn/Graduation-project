# -*- coding:utf-8 -*-  
from pymongo import MongoClient  
import  xdrlib ,sys
import xlrd

settings = {  
'ip': '18.218.125.105',  # ip地址  
'port': 27017,  # 端口, mongodb默认端口27017  
'db_name': 'xiaoke',  # 数据库名字  
'set_name': 'intensity'  
}


class MyMongoDB(object):  
    # 初始化函数  
    def __init__(self):  
        try:  
            self.conn = MongoClient(  
                settings['ip'], settings['port']  
            )  
        except Exception as e:  
            print (e)  
        self.db = self.conn[settings['db_name']]  
        self.my_set = self.db[settings['set_name']]  
  
    # 插入数据函数定义  
    def insert(self, dic):  
        print ('insert...')  
        self.my_set.insert(dic)  

    #insert_many()
    def insert_many(self,dictlist):
    	print ('insert many...')
    	self.my_set.insert_many(dictlist)
  
    # 更新数据函数定义  
    def update(self, olddic, newdic):  
        print ('update...' ) 
        self.my_set.update(olddic, newdic)  
  
    # 删除数据函数定义  
    def delete(self, dic):  
        print ('delete...')  
        self.my_set.remove(dic)  
  
    # 查询数据函数定义  
    def dbfind(self, dic):  
        print ('find...')  
        data = self.my_set.find(dic)  
        for res in data:  
            print ('name==%s, age==%s' % (res['name'], res['age']) ) 

def dataInsertMany(diclist):
	mongo = MyMongoDB()
	mongo.insert_many(diclist)


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


#根据名称获取Excel表格中的数据   参数:file：Excel文件路径 by_name：Sheet名称
def excel_table_byname(file,by_name):
    colnameindex=0
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list1 =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             app[colnames[0]] = row[0]
             timeIndex = []
             intensity = []
             for i in range(1,len(colnames)):
             	# i = i + 1
             	timeIndex.append(colnames[i])
             	intensity.append(row[i])
             # print(timeIndex)
             # print(intensity)
             app["time"]= timeIndex
             app["intensity"]= intensity
                # app[colnames[i]] = row[i]
             list1.append(app)
    return list1

def main(file,sheet):
	tables = excel_table_byname(file,sheet)
	print(tables)
	dataInsertMany(tables)
	


if __name__ == '__main__':
	file = '../testData/intensityTime.xlsx'
	sheet = "Sheet1"
    # 集合(相当于mysql的表)名字  
	main(file,sheet)
# INId:1001,madutime:[{time:,intensity:},{},{},]
# INId:1001,timeIndex:[],intensity:[]

