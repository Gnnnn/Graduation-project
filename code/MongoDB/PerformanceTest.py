import time,datetime
# from pymongo import Connection
from pymongo import MongoClient 
import random

# connection = Connection('18.218.125.105', 27017)
# db = connection['xiaoke']

client = MongoClient("18.218.125.105", 27017)
db = client.xiaoke

#时间记录器
def func_time(func):
    def _wrapper(*args,**kwargs):
            start = time.time()
            func(*args,**kwargs)
            print (func.__name__,'run:',time.time()-start)
    return _wrapper

@func_time
def insert(num):
    posts = db.test
    for x in range(num):
        post = {"_id" : str(x),
                "author": str(x)+"Eva",
                "text": "My first test!",
                "tags": ["mongodb", "python", "pymongo"],
                "date": datetime.datetime.utcnow()}
        posts.insert(post)

#@func_time
def randy():
    rand = random.randint(1,5000000)
    return rand

@func_time
def mread(num):
    find = db.test
    for i in range(num):
        rand = randy()
#随机数查询
        find.find({"author": str(rand)+"Eva"})

@func_time
def remove():
    posts = db.test
    print ('count before remove:',posts.count())
    posts.remove({});
    print ('count after remove:',posts.count())


if __name__ == "__main__":
	#设定循环1000次
   num = 100000
   insert(num)
   # insert run: 266.69562578201294--1000
   mread(num)
   # mread run: 0.01651144027709961--1000
   remove()
   # remove run: 1.8748316764831543--1000
