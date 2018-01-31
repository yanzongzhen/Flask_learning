#coding:utf-8
import  os

users = {}
base_path = os.path.abspath(os.path.dirname(__file__))

def userPrase():
    with open(os.path.join(base_path, 'userinfo.txt'),'r') as f:
        data = f.readlines()
        print(data)
        for i in data:
            user = i.split('|')
            yield{
                "name":user[0][4:],
                "password":user[1][3:]
            }

def loginAuth(name,pw):
    for i in userPrase():
        if name == i['name'] and pw == i['password']:
            return True


print(loginAuth("zhang","123"))