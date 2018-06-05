# -*- coding: utf-8 -*- 
import xdrlib
import xlrd
from py2neo import Graph,Node,Relationship


def excel(fileName,sheetName):
    bk = xlrd.open_workbook(fileName)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name(sheetName)
    except:
        print("no sheet in file")
    nrows = sh.nrows
    ncols = sh.ncols
    print("nrows %d, ncols %d" % (nrows, ncols))
    dataList = []
    for i in range(0,nrows):
        dataList.append(sh.row_values(i))
    print("dataList: ")
    print(dataList)
    return dataList


def neo4jdbConnect():
    global g
    g = Graph(host = "18.218.125.105",http_port = 7474,user = "neo4j",password = "test")
    return g


def neo4jdbnode(g,dataList):
    UserList = []
    InstantNoodleList = []
    i = 1
    while i < len(dataList):
        UserList.append(dataList[i][0])
        i = i + 1
    d = {}
    m = 0 
    UserDict = []
    while m < len(UserList):
        d["name"] = str(UserList[m])
        UserDict.append(d)
        d = {}
        m = m + 1
    print("UserDict: ")
    print(UserDict)

    i = 1
    while i < len(dataList[0]):
        InstantNoodleList.append(dataList[0][i])
        i = i + 1
    d = {}
    m = 0 
    InstantNoodleDict = []
    while m < len(InstantNoodleList):
        d["id"] = InstantNoodleList[m]
        InstantNoodleDict.append(d)
        d = {}
        m = m + 1
    print("InstantNoodleDict: ")
    print(InstantNoodleDict)

    g.delete_all()
    tx = g.begin()
    for User in UserDict:
        node = Node("User",label = "User",**User)
        tx.merge(node)
    for InstantNoodle in InstantNoodleDict:
        node = Node("InstantNoodle",label = "InstantNoodle",**InstantNoodle)
        tx.merge(node)
    tx.commit()
    return UserList,InstantNoodleList

    

def neo4jdbrel(g,dataList,UserList,InstantNoodleList):
    tx = g.begin()
    i = 0
    j = 0
    num = 0
    while i < len(UserList):
        j = 0
        while j <len(InstantNoodleList):
            print(UserList[i])
            print(InstantNoodleList[j])
            node1 = g.find_one(label="User",property_key="name",  property_value=str(UserList[i]))
            node2 = g.find_one(label="InstantNoodle",property_key="id",  property_value=InstantNoodleList[j])
            print(node1)
            print(node2)
            rel = Relationship(node1,'rated',node2)
            rel["rate"] = dataList[i+1][j+1]
            tx.merge(rel)
            print (num)
            num = num + 1
            j = j +1
        i = i + 1
    tx.commit()


def main():
    file = '../testData/UserRate.xlsx'
    sheet = 'Sheet1'
    dataList = excel(file,sheet)
    g = neo4jdbConnect()
    UserList,InstantNoodleList = neo4jdbnode(g,dataList)
    neo4jdbrel(g,dataList,UserList,InstantNoodleList)
    #match p= ({name:'用户1号'})-[]-() return p
    #match p= () return p


if __name__ == "__main__":
	main()




