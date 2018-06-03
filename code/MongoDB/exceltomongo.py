# -*- coding:utf-8 -*-  
from pymongo import MongoClient  
import  xdrlib ,sys
import xlrd


settings = {  
    'ip': '18.218.125.105',  # ip地址  
     'port': 27017,  # 端口, mongodb默认端口27017  
    'db_name': 'test',  # 数据库名字  
     'set_name': 'xiaoke'  # 集合(相当于mysql的表)名字  
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
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main(file,sheet):
	tables = excel_table_byname(file,sheet)
	print(tables)
	dataInsertMany(tables)
	# client = MongoClient("18.218.125.105", 27017)
	# mdb = client.test
	# collection = mdb.xiaoke
	# mdb.collection.insert_many(table)
	


if __name__ == '__main__':
	file = 'G:/GITHUB/Graduation-project/code/testData/InstantNoodlesAttr.xlsx'
	sheet = "Sheet1"
	main(file,sheet)
