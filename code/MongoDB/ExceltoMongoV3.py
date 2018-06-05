# -*- coding:utf-8 -*-  
from pymongo import MongoClient  
import  xdrlib ,sys
import xlrd
import xml.dom.minidom

settings = {  
'ip': '18.218.125.105',  # ip地址  
'port': 27017,  # 端口, mongodb默认端口27017  
'db_name': 'xiaoke',  # 数据库名字  
'set_name': 'InstantNoodlesAttr'  
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

def xmlExcel(xmlname):
    #打开xml文档
    dom = xml.dom.minidom.parse(xmlname)

    #得到文档元素对象
    root = dom.documentElement
    sheetname = root.nodeName
    # print (root.nodeName)
    i = 1
    Attrdict = {}
    while i < len(root.childNodes):
        childNode = root.childNodes[i]
        # print (childNode.nodeName)
        # print (childNode.getAttribute('name'))
        Attrdict[childNode.nodeName] = childNode.getAttribute('name')
        i = i + 2
    print(Attrdict)
    return sheetname,Attrdict

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径 by_name：Sheet名称
def excel_table_byname_InstantNoodlesAttr(file,by_name):
    colnameindex=0
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list1 =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         # print(row)
         if row:
             app = {}
             app[colnames[0]] = row[0]
             special = {}
             INAttr = {}
             for i in range(1,len(colnames)-2):
             	# i = i + 1
                INAttr[colnames[i]]=row[i]
             for i in range(len(colnames)-2,len(colnames)):
                if row[i]!='':
                    special[colnames[i]] =row[i]
                    INAttr['special']=special
             # print(INAttr)
             list1.append(INAttr)
    return list1


def excel_table_byname_intensityTime(file,by_name):
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

def excel_table_byname_MultipleAttr(file,by_name):
    colnameindex=0
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list1 =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         # print(row)
         if row:
             app = {}
             app[colnames[0]] = row[0]
             special = {}
             INAttr = {}
             for i in range(1,len(colnames)):
                # i = i + 1
                INAttr[colnames[i]]=row[i]
             # print(INAttr)
             list1.append(INAttr)
    return list1

def excel_table_byname_TesterRate(file,by_name,Attr):
    data = open_excel(file)
    table = data.sheet_by_name(sheetname)
    colnameindex=0
    colnames =  table.row_values(colnameindex) #第一行数据
    # print(colnames)
    # rownames =  table.col_values(colnameindex)[2:] #第一行数据
    # print(rownames)
    columnNameList = []
    i = 0
    while i <len(Attr)-2:
        i = i + 1
        columnName = 'column'+str(i)
        columnNameList.append(Attr.get(columnName))
    print("columnNameList:")
    print(columnNameList)
    rowName = Attr.get('row')
    dataName = Attr.get('data')
    nrows = table.nrows
    ncols = table.ncols
    # cell_value = table.cell_value(2,1)
    # print (cell_value)
    data = []

    for i in range(0,nrows-len(Attr)+2):
        row_data = table.row_values(i)
        for j in range(1,ncols):
            dataDict = {}
            for k in range(0,len(columnNameList)):
                dataDict[columnNameList[k]] = table.row_values(k)[j]
                # print(table.row_values(k+1)[j])
                # dataDict[columnNameList[k+1]] = table.row_values(k+1)[j]
                k = k +1
                # print(dataDict)
            dataDict[rowName] = table.col_values(0)[2:]
            dataDict[dataName] = table.col_values(j)[2:]
            print ("dataDict")
            print (dataDict)
            data.append(dataDict)
    print("data:")
    print(data)
    print(len(data))
    # return;
    #[{InstantNoodleId:1001,UserId:1,UserRate:1},{}]
    return data

def excel_table_byname_UserRate(file,by_name):
    colnameindex=0
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list1 =[]
    for rownum in range(1,nrows):
         INAttr={}
         row = table.row_values(rownum)
         # print(row)
         INAttr["InstantNoodleId"]=table.row_values(0)[1:]
         INAttr["UserRate"]=row[1:]
         INAttr["UserId"]=table.col_values(0)[rownum]
         # print(INAttr)
         list1.append(INAttr)
    return list1

def excel_table_byname_attrFrequencyTime(file,by_name):
    colnameindex=0
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list1 =[]
    for rownum in range(2,nrows):
         row = table.row_values(rownum)
         if row:
             for j in range(1,4):
                app = {}
                app["InstantNoodleId"] = row[0]
                app["time"]= table.row_values(1)[1:7]
                Frequency = []
                for i in range(1,8):
                    Frequency.append(row[i+7*(j-1)])
                app["Attr"]= table.col_values(j*7)[0]
                app["Frequency"]= Frequency
                # print(app)
                list1.append(app)
    return list1



def main(file,sheet):
    if file=="../testData/InstantNoodlesAttr.xlsx":
    	tables = excel_table_byname_InstantNoodlesAttr(file,sheet)
    elif file == "../testData/intensityTime.xlsx":
        tables = excel_table_byname_intensityTime(file,sheet)
    elif file == "../testData/MultipleAttr.xlsx":
        tables = excel_table_byname_MultipleAttr(file,sheet)  
    elif file == "../testData/TesterRate.xlsx":
        tables = excel_table_byname_TesterRate(file,sheet)
    elif file == "../testData/UserRate.xlsx":
        tables = excel_table_byname_UserRate(file,sheet)
    elif file == "../testData/attrFrequencyTime.xlsx":
        tables = excel_table_byname_attrFrequencyTime(file,sheet)
    print(tables)
    dataInsertMany(tables)

# def main(file,sheet,Attrdict):
#     tables = excel_table_byname_TesterRate(file,sheet,Attrdict)
#     print(tables)
#     dataInsertMany(tables)

settings['set_name']='attrFrequencyTime'
if __name__ == '__main__':
     #这是方法一，手动修改代码
     file = '../testData/attrFrequencyTime.xlsx'
     sheet = "Sheet1"
     main(file,sheet)

     #这是方法二，使用xml配置文件
     # xmlname = '../testData/TesterRate.xml'
     # sheetname,Attrdict = xmlExcel(xmlname)
     # main(file,sheetname,Attrdict)

# INId:1001,madutime:[{time:,intensity:},{},{},]
# INId:1001,timeIndex:[],intensity:[]

