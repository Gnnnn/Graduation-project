# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import json
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

def neo4jdb1(g,InstantNoodles):
    g.delete_all()
    tx = g.begin()
    for InstantNoodle in InstantNoodles:
        node = Node("InstantNoodle",**InstantNoodle)
        tx.merge(node)
    tx.commit()  


def neo4jdb2(g,dataList):
    InstantNoodles = []
    i = 1
    while i<len(dataList):
        d = {}
        j = 0
        while j<len(dataList[0]):
            d[dataList[0][j]] = dataList[i][j]
            j = j +1
        i = i +1
        InstantNoodles.append(d)

    manufacturersList = []
    InstantNoodles2 = []

    i = 1
    while i<len(dataList):
        d = {}
        j = 1
        while j<len(dataList[0]):
            d[dataList[0][j]] = dataList[i][j]
            j = j +1
        manufacturersList.append(dataList[i][0])
        manufacturersList = list(set(manufacturersList))
        InstantNoodles2.append(d)
        i = i +1
    print("InstantNoodles2: ")
    print(InstantNoodles2)
    m = 0
    d = {}
    manufacturers = []
    while m<len(manufacturersList):
        d["name"] = manufacturersList[m]
        manufacturers.append(d)
        d = {}
        m = m+1
    print("manufacturers: ")
    print(manufacturers)

    i = 1
    mapInmf = {}
    while i<len(dataList):
        mapInmf[dataList[i][1]] = dataList[i][0]
        i = i +1
    print("map: ")
    print(mapInmf)


    g.delete_all()
    tx = g.begin()
    for InstantNoodle2 in InstantNoodles2:
        node = Node("InstantNoodle2",label = "InstantNoodle2",**InstantNoodle2)
        tx.merge(node)
    for manufacturer in manufacturers:
        node = Node("manufacturer",label = "manufacturer",**manufacturer)
        tx.merge(node)
    tx.commit()
    return mapInmf


def neo4jdb3(g,mapInmf):
    tx = g.begin()
    i=1001
    while i<1031:
        # st = 'match p = ({id: '+str(i)+' }) return p'
        # print(g.run(st).evaluate())
        # st2 = 'match q = ({name: "'+str(mapInmf[i])+'" }) return q'
        # # node2 = g.run(st2).evaluate()
        # rel = Relationship(g.run(st).evaluate(),'belongs_to',g.run(st2).evaluate())
        node1 = g.find_one(label="InstantNoodle2",property_key="id",  property_value=i)
        node2 = g.find_one(label="manufacturer",property_key="name",  property_value=str(mapInmf[i]))
        rel = Relationship(node1,'belongs_to',node2)
        tx.merge(rel)
        i = i + 1
    tx.commit()

def design1():
    #字典映射
    InstantNoodles = []
    i = 1
    while i<len(dataList):
        d = {}
        j = 0
        while j<len(dataList[0]):
            d[dataList[0][j]] = dataList[i][j]
            j = j +1
        i = i +1
        InstantNoodles.append(d)
    print("InstantNoodles: ")
    print(InstantNoodles)

    neo4jdb1(db,InstantNoodles)
    #localhost:7474里输入"MATCH p=() RETURN count(p)"可得出共30个节点
    #输入"MATCH p=() RETURN p"可看到每个节点


def design2(db,dataList):
    mapInmf = neo4jdb2(db,dataList)
    neo4jdb3(g,mapInmf)



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
    file = '../testData/InstantNoodlesAttr.xlsx'
    sheet = 'Sheet1'
    dataList = excel(file,sheet)
    db = neo4jdbConnect()
    #方案一：每种方便面一个节点，无联系
    #design1(db,dataList)
    

    #方案二：方便面和厂商各为一种类型，共两个节点，彼此是从属关系
    #match p= ()-[]-() return p
    design2(db,dataList)
    
    #UserFeedback
    file = '../testData/UserRate.xlsx'
    sheet = 'Sheet1'
    dataList = excel(file,sheet)
    UserList,InstantNoodleList = neo4jdbnode(g,dataList)
    neo4jdbrel(g,dataList,UserList,InstantNoodleList)
    
    

if __name__=="__main__":
    main()