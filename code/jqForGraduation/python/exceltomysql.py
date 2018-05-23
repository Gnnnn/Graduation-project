# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd,re
import pymysql.cursors
import xml.dom.minidom

#现在还存在的小问题包括：table名是根据文件名传的，所以也包括了路径和.xlsx后缀，要做一下正则处理。
#每次插入都要重新开一个指针，所以插入太慢。这里可以优化。完成
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


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


#根据名称获取Excel表格中的数据   参数:file：Excel文件路径 by_name：Sheet名称,
# Attr:根据config.xml映射出的行列值字典
def excel_table_byname(file,sheetname,Attr):
    data = open_excel(file)
    table = data.sheet_by_name(sheetname)
    colnameindex=0
    colnames =  table.row_values(colnameindex) #第一行数据
    # print(colnames)
    Attrlist = []
    for k,v in Attr.items():
        Attrlist.append(v)
    print(Attrlist)
    #我们的config规定列名只有一列，有一个值是data，所以行名的数量为len-2
    RowNameNum = len(Attrlist)-2
    print(RowNameNum)
    # columnName = Attr.get('column')
    # rowName = Attr.get('row')
    # dataName = Attr.get('data')
    nrows = table.nrows
    ncols = table.ncols
    print(nrows)
    print(ncols)
    # cell_value = table.cell_value(2,2)
    # print (cell_value)
    rowindex=0
    columnName =  table.col_values(rowindex) #第一行数据
    # columnName = columnName[RowNameNum:]
    print(columnName)
    i = 0
    RowName = []
    while i < RowNameNum:
        # RowName.append(table.row_values(i)[1:])
        RowName.append(table.row_values(i))
        i = i +1
    # print(RowName)
    RowAttr = list(zip(*RowName))
    print(RowAttr)
    # print(RowAttr[0][1])

    data = []
    for i in range(RowNameNum,nrows):
        row_data = table.row_values(i)
        for j in range(1,ncols):
            dataDict = {}
            # print (i)
            dataDict[Attrlist[0]] = columnName[i]
            for k in range(0,RowNameNum) :
                dataDict[Attrlist[k+1]] = RowAttr[j][k]
            # print (i,j)
            dataDict[Attrlist[-1]] = table.cell_value(i,j)
            # print (dataDict)
            data.append(dataDict)
    print(data)
    #[{TesterId:1,InstantNoodleId:1001,InstantNoodleAttr:'色泽',attrRate:'8.5'},{}]
    return data

def createTableSql(tableName,data):
    for row in data:
        print(row)
        Attrlen = len(row);
        l = 0
        sqlModel = "CREATE TABLE `{}` ( "
        sqlAttrModel = "`{}` {} DEFAULT NULL"
        sqlModelEnd = " ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        while l < Attrlen-1: 
            sqlModel = sqlModel + sqlAttrModel + ", "
            l = l+ 1
        sqlModel = sqlModel +sqlAttrModel + sqlModelEnd
        # print(sqlModel)
        rowType = {}
        # tableName = re.compile(tableName).match(r"/[].")
        sqlvalue = "'"+tableName+"';"
        for key in row:
            if isinstance(row[key],str):
                rowType[key] = 'varchar(30)'
            elif isinstance(row[key],(int,bool)):
                rowType[key] = 'int(100)'
            elif isinstance(row[key],float):
                rowType[key] = 'float(10,4)'
            sqlvalue = sqlvalue + key+";"+rowType[key]+";"
        sqlvalue=DelLastChar(sqlvalue)
        sqlvaluelist = sqlvalue.split(";")
        # print(sqlvaluelist)
        sql = sqlModel.format(*sqlvaluelist)
        print (sql)
        return sql

def insertSql(row):
    Attrlen = len(row);
    sql = "INSERT INTO `'"+ file +"'` values ("
    for key in row:
        value = row[key]
        sql = sql+"'"+str(value)+"',"
    sql = DelLastChar(sql)
    sql = sql +");"
    print(sql)
    return sql

def insert(data,conn):
    cursor = conn.cursor() 
    if not cursor: 
        raise Exception('数据库连接失败！') 
    for row in data:
        Attrlen = len(row);
        sql = "INSERT INTO `'"+ file +"'` values ("
        for key in row:
            value = row[key]
            sql = sql+"'"+str(value)+"',"
        sql = DelLastChar(sql)
        sql = sql +");"
        print(sql)
        cursor.execute(sql) 
    conn.commit() 
    cursor.close() 
    #conn.close() 
    return 


#连接数据库-查询
def database(conn,sql):
    cursor = conn.cursor() 
    if not cursor: 
        raise Exception('数据库连接失败！') 
    cursor.execute(sql) 
    results = cursor.fetchall() 
    cursor.close() 
    #conn.close() 
    i = 0 
    datas = [] 
    print(results)
    while i < len(results): 
        i = i+1 
        result = results[i-1] 
        result = checkdata(result) 
        datas.append(result) 
    return datas 



#连接数据库-增删改
def databasesql(conn,sql):
    cursor = conn.cursor() 
    if not cursor: 
        raise Exception('数据库连接失败！') 
    cursor.execute(sql) 
    conn.commit() 
    cursor.close() 
    #conn.close() 
    return 

def DelLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)

def DelFirstChar(str):
    str_listTemp=list(str)
    str_list=str_listTemp[1]
    return "".join(str_list)

def arraydictToMysql(tableName,data):
    for row in data:
        print(row)
        Attrlen = len(row);
        l = 0
        sqlModel = "CREATE TABLE `{}` ( "
        sqlAttrModel = "`{}` {} DEFAULT NULL"
        sqlModelEnd = " ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        while l < Attrlen-1: 
            sqlModel = sqlModel + sqlAttrModel + ", "
            l = l+ 1
        sqlModel = sqlModel +sqlAttrModel + sqlModelEnd
        print(sqlModel)

        rowType = {}
        sqlvalue = "'"+tableName+"';"
        for key in row:
            if isinstance(row[key],str):
                rowType[key] = 'varchar(30)'
            elif isinstance(row[key],(int,bool)):
                rowType[key] = 'int(100)'
            elif isinstance(row[key],float):
                rowType[key] = 'float(10,4)'
            sqlvalue = sqlvalue + key+";"+rowType[key]+";"
        sqlvalue=DelLastChar(sqlvalue)
        sqlvaluelist = sqlvalue.split(";")
        print(sqlvaluelist)
        sql = sqlModel.format(*sqlvaluelist)
        print (sql)
        return sql



def main(xmlfile,file):
    # conn = pymysql.connect(host='18.218.245.165',user='root',passwd='test',db='Gra') 
    # Connect to the database
    conn = pymysql.connect(host='18.218.245.165',
                             user='root',
                             password='test',
                             db='Gra',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    sheetname,Attr = xmlExcel(xmlname)
    data = excel_table_byname(file,sheetname,Attr)

    createsql = createTableSql(file,data)
    databasesql(conn,createsql)
    insert(data,conn)
    conn.close()
    print("finished!")

if __name__=="__main__":
    # file = sys.argv[1]
    # sheet = "Sheet1"
    file = 'testData/MultipleAttr.xlsx'
    xmlname = "testData/MultipleAttr.xml"
    # print(tableName)
    main(xmlname,file)
