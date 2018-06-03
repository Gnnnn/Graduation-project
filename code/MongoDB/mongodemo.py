# -*- coding:utf-8 -*-  
from pymongo import MongoClient  
settings = {  
    'ip': '18.218.125.105',  # ip地址  
     'port': 27017,  # 端口, mongodb默认端口27017  
    'db_name': 'test',  # 数据库名字  
     'set_name': 'xiaoke'  # 集合(相当于mysql的表)名字  
}  
  

# 定义mongodb的通用接口  
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
    def insert1(self, dic):  
        print ('insert...')  
        self.my_set.insert(dic)  
  
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

def query():
    # 条件操作符  
    # 查询集合中age大于25的记录  
    for i in my_set.find({"age": {"$gt": 25}}):  
        print i  
      
    # 判断类型  
    for i in my_set.find({"name": {'$type': 3}}):  
        print i  
      
    # 指定字段排序  
    for i in my_set.find().sort([('age', 1)]):  
        print i  
      
    # 查询指定条数limit, 跳过指定条数skip  
    # 以下表示跳过两条后查询出两条信息  
    for i in my_set.find().skip(2).limit(2):  
        print i  
      
    # in操作查询(包含查询)  
    for i in my_set.find({'age': {'$in': (18, 26)}}):  
        print i  
      
    # or操作查询(或查询)  
    for i in my_set.find({'$or': [{'age': 23}, {'age': 26}]}):  
        print i  
      
    # all操作查询(查找满足全部条件的数据)  
    # 先插入数据  
    # dic = {'name': 'lisi', 'age': 16, 'li': [1, 2, 3]}  
    # dic2 = {'name': 'zhangsan', 'age': 18, 'li': [1, 2, 3, 4, 5, 6]}  
    # my_set.insert(dic)  
    # my_set.insert(dic2)  
      
    # for i in my_set.find({'li': {'$all': [1, 2, 3, 4]}}):  
    #     print i  
      
    # push插入  
    # my_set.update({'name': 'lisi'}, {'$push': {'li': 4}})  
    # for i in my_set.find({'name': 'lisi'}):  
    #     print i  
      
    # pushall插入  
    # my_set.update({'name': 'lisi'}, {'$pushAll': {'li': [4, 5]}})  
    # for i in my_set.find({'name': 'lisi'}):  
    #     print i  
      
    # pop移除最后一个元素  
    # my_set.update({'name': 'lisi'}, {'$pop': {'li': 1}})  
    # for i in my_set.find({'name': 'lisi'}):  
    #     print i  
      
    # pull按值移除  
    # my_set.update({'name': 'lisi'}, {'$pull': {'li': [4, 5]}})  
    # for i in my_set.find({'name': 'lisi'}):  
    #     print i  
      
    # pullAll移除全部符合条件的  
    # my_set.update({'name': 'lisi'}, {'$pullAll': {'li': [4, 4]}})  
    # for i in my_set.find({'name': 'lisi'}):  
    #     print i  
      
    # 多级目录元素操作  
    # 先插入一条数据  
    # dic = {  
    #     'name': 'zhangsan',  
    #     'age': 18,  
    #     'contact': {  
    #         'email': '123456789@163.com',  
    #         'iphone': '110112114119'  
    #     }  
    # }  
    # my_set.insert(dic)  
      
    # 多级目录用.连接  
    # for i in my_set.find({'contact.iphone': '110112114119'}):  
    #     print i  
    #  
    # print my_set.find_one({'contact.iphone': '110112114119'})  
    #  
    # res = my_set.find_one({'contact.iphone': '110112114119'})  
    # print res['contact']['iphone']  # python方式取值  
      
    # 对数据进行索引操作  
    # 插入数据  
    # dic = {"name": "lisi",  
    #        "age": 18,  
    #        "contact": [{  
    #            "email": "111111@qq.com",  
    #            "iphone": "111"},  
    #            {  
    #            "email": "222222@qq.com",  
    #            "iphone": "222"  
    #            }]  
    #        }  
    # my_set.insert(dic)  
    # 通过索引查找数据  
    res = my_set.find_one({'contact.1.iphone': '222'})  
    print res  
    print res['contact'][1]['email']  
    # 修改  
    result = my_set.update(  
        {'contact.1.iphone': '222'},  
        {'$set': {'contact.1.email': '222222@qq.com'}}  
    )


def main():  
    dic = {'id': 2,'name': 'xiaoxiaoke', 'age': 20}  
    mongo = MyMongoDB()  
  
    # 插入数据  
    mongo.insert1(dic)  
    mongo.dbfind({'name': 'xiaoxiaoke'})  # 查看数据  
  
     # 修改数据  
    mongo.update({'name': 'xiaoxiaoke'}, {'$set': {'age': 25}})  
    mongo.dbfind({'name': 'xiaoxiaoke'})  # 查看数据  
  
     # 删除数据  
    mongo.delete({'name': 'xiaoxiaoke'})  
    mongo.dbfind({'name': 'xiaoxiaoke'})  
  
if __name__ == '__main__':  
    main()  