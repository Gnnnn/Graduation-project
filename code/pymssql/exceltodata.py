# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import  xml.dom.minidom

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


def DelLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)


def excel_table_byname(file,sheetname,Attr):
    data = open_excel(file)
    table = data.sheet_by_name(sheetname)
    colnameindex=0
    colnames =  table.row_values(colnameindex) #第一行数据
    # print(colnames)
    columnName = Attr.get('column')
    rowName = Attr.get('row')
    dataName = Attr.get('data')
    nrows = table.nrows
    ncols = table.ncols
    # cell_value = table.cell_value(2,2)
    # print (cell_value)
    data = []
    for i in range(1,nrows):
        row_data = table.row_values(i)
        for j in range(1,ncols):
            dataDict = {}
            dataDict[columnName] = row_data[0]
            dataDict[rowName] = colnames[j]
            dataDict[dataName] = table.cell_value(i,j)
            # print (dataDict)
            data.append(dataDict)
    print(data)
    #[{InstantNoodleId:1001,UserId:1,UserRate:1},{}]
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



def insertSql(data):
    for row in data:
        Attrlen = len(row);
        sql = "INSERT INTO `'"+ file +"'` values ("
        for key in row:
            value = row[key]
            sql = sql+"'"+str(value)+"',"
        sql = DelLastChar(sql)
        sql = sql +");"
        print(sql)
    return sql


def main(file):
    xmlname = "UserRate.xml"
    sheetname,Attr = xmlExcel(xmlname)
    data = excel_table_byname(file,sheetname,Attr)

    createsql = createTableSql(file,data)
    insertsql = insertSql(data)
    print("finished!")


if __name__=="__main__":
    # file = sys.argv[1]
    # sheet = "Sheet1"
    file = 'UserRate.xlsx'
    main(file)