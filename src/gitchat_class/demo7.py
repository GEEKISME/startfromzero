a = [1,2,3,4,2,2,3]
s = max(a,key=lambda x:a.count(x),default=1)
print(s)
print('===========================')
def f(a,*,b):
    return a
s = f(6,b=1)
print(s)
# s = f(7,8)
# print(s)
print('=============================')
dic = {'a':1,'b':2}
print(len(dic))
s = max(3,1,4,2,1)
print(s)
s = max((),default=0)
print('===========================')
di = {'a':3,'b1':1,'c':4}
s = max(di)
print(s)
print('=============================')
a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'xiaohong','age':20,'gender':'female'}]
s = max(a,key=lambda x:x['age'])
print(s)
print('=============================')
def max_length(*lst):
    return max(*lst,key=lambda v:len(v))
s = max_length([1, 2, 3], [4, 5, 6, 7], [8])
print(s)
print('=======================================')
s = pow(3,2)
print(s)
s = pow(3,2,4)
print(s)
print('=======================================')
s = round(10.22222,3)
print(s)
print('==================================')
a = [1,4,2,3,1]
s = sum(a)
print(s)
s = sum(a,10)
print(s)
print('========================')
s = abs(-6)
print(s)
print('=========================')
# 分别取商和余数：
s = divmod(12,3)
print(s)
print('=========================')
# 创建一个复数：
s = complex(1,2)
print(s)
print('===========================')
p = hash('xiaoming')
print(p)
s = id('xiaoming')
print(s)
print('===============================')
# 逻辑运算
# all(iterable)
# 接受一个迭代器，如果迭代器的所有元素都为真，返回 True，否则返回 False：
s = all([1,0,3,6])
print(s)
s1 = all([1,1,3,6])
print(s1)
print('=================================')
# any(iterable)　
# 接受一个迭代器，如果迭代器里有一个元素为真，返回 True，否则返回 False：
s = any([0,0,0,[]])
print(s)
s1 = any([0,0,1])
print(s1)
print('====================================')
class Student():
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
    def __repr__(self):
        return 'id='+self.__id+',name'+self.__name

xiaoming = Student('001','xiaoming')
print(xiaoming)
print(ascii(xiaoming))
print('===================================')
print(bin(10))
print(oct(9))
print(hex(15))