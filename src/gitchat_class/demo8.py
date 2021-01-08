# 类型函数
# bool([x])　　
# 测试一个对象是 True，还是 False。
print(bool([0,0,0]))
print(bool([]))
print(bool([1,0,1]))

# bytes([source[, encoding[, errors]]])　　
# 将一个字符串转换成字节类型：
s = 'apple'
s = bytes(s,encoding='utf-8')
print(s)
# str(object='')　　
# 将字符类型、数值类型等转换为字符串类型：
i = 100
print(str(i))
# chr(i)
# 查看十进制整数对应的 ASCII 字符：
print(chr(65))
# ord(c)
# 查看某个 ASCII 字符对应的十进制数：
print(ord('A'))

# dict()　　
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
# 创建数据字典：
print('============================')
print(dict())
print(dict(a='a',b='b'))
print(dict(zip(['a','b'],[1,2])))
print('=============================')
# object()
# 返回一个根对象，它是所有类的基类。
o = object()
print(type(o))
print('===============================')
# 使用魔法函数 __dir__，查看 object 对象上的所有方法：
print(o.__dir__())
print('================================')
# int(x)　　
# int(x, base =10)，x 可能为字符串或数值，将 x 转换为一个整数。
print(int('12'))
print(int('12',16))
print('================================')
print(float('30'))
print('===================================')
# frozenset([iterable])　　
# 创建一个不可修改的冻结集合，一旦创建不允许增删元素。
s = frozenset([1,1,3,2,3])
print(s)
# 但是，普通集合 set 创建后，仍然可以增删元素。
#
# 创建一个普通集合 k：
k = {1,2,3}
# 创建 k 后，仍然能通过 add 方法，再插入元素：
k.add(4)
print(k)
# 普通集合也能删除元素，使用 pop 方法移除集合的第一个元素：
print(k.pop())
print(k)
print('===================================')
# list([iterable])
# 返回可变序列类型：列表。如下，集合类型转列表：
s = {1,2,3}
print(list(s))
print('======================================')
# list 函数还常用在，可迭代类型（Iterable）转化为列表。
#
# 如下，使用 map 函数，转化列表内每一个整形元素为字符串型。
#
# m 是可迭代类型，经过 list 转化后，看到列表 l。
m = map(lambda i:str(i),[186,1243,3201])
l = list(m)
print(l)
print(list(map(lambda x:x%2==1,[1,3,2,4,1])))
print('============================')
# range(stop)；range(start, stop[,step])
# Python 提供两个内置的 range 函数，生成不可变序列：
# # 只有一个参数，默认初始值为 0，步长为 1
print(range(11))
print(range(0,11,1)) #三个参数都提供，分别是开始、终止、步长值
print('=============================')
# set([iterable])
# 返回一个集合对象，并允许创建后再增加、删除元素。
#
# 集合的一大优点，容器里不允许有重复元素，因此可对列表内的元素去重。
a = [1,4,2,3,1]
b = set(a)
print(b)
print('=============================')
# slice(stop)；slice(start, stop[, step])
# 返回一个由 range(start, stop, step) 所指定索引集的 slice 对象：
a = [1,4,2,3,1]
print(a[slice(0,5,2)]) #等价于a[0:5:2]
# tuple([iterable])
# 创建一个不可修改的元组对象：
t = tuple(range(10))
print(t)
print('==================================')
# type(object)；type(name, bases, dict)
# 自定义类 Student，创建实例 xiaoming：
class Student:
    pass
xiaoming = Student()
print(type(xiaoming))
print(type((1,2,3)))
print('==============================')
# zip(*iterables)
# 创建一个迭代器，聚合每个可迭代对象的元素。
#
# 参数前带 *，意味着是可变序列参数，可传入 1 个，2 个或多个参数。
#
# 传入 1 个参数：
for i in zip([1,2]):
    print(i)
print('=========================')
a = range(5)
print(a)
b = list('abcde')
print(b)
for x,y in zip(a,b):
    print(str(y)+str(x))
print('=====================================')
class Student():
    def __init__(self,id = None,name = None):
        self.id = id
        self.name = name
    def instance_method(self):
        print('这是实例方法')
        return self
    @classmethod
    def __annotations__(cls):
        return '学生类'
    @classmethod
    def print_type_name(cs):
        print('这是类上的方法，类名为 %s，注解为 %s' % (cs.__name__, cs.__annotations__()))

Student().print_type_name()
Student().instance_method()
print('=======================================')
# delattr(object, name)　　
# 删除对象的属性，在不需要某个或某些属性时，这个方法就会很有用。
class Student():
    def __init__(self,id = None,name = None):
        self.id = id
        self.name = name
xiaoming = Student(1,'xiaoming')
delattr(xiaoming,'id')
# print(xiaoming.id)
print(hasattr(xiaoming,'id'))
# dir([object])　　
# 不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时返回参数的属性、方法列表。
print('=================================')
print(dir())
print(dir(xiaoming))
# getattr(object, name[, default])　　
# 获取对象的属性：
class Student():
    def __init__(self,id = None,name = None):
        self.id = id
        self.name = name
xiaoming = Student(1,'xiaom')
print(getattr(xiaoming,'name','s'))
print(hasattr(xiaoming,'name'))
delattr(xiaoming,'id')
print(hasattr(xiaoming,'id'))
print('===========================')
# isinstance(object, classinfo)
# 判断 object 是否为类 classinfo 的实例，若是，返回 true。
xiaoli = Student('001','xiaoli')
print(isinstance(xiaoli,Student))
# 序列类型的基类为 Iterable，所以返回 True：
from collections.abc import Iterable
print(isinstance([1,2,3],Iterable))
print('======================================')
# issubclass(class, classinfo)
# 如果 class 是 classinfo 类的子类，返回 True：
class undergradute(Student):
    def studyClass(self):
        pass
    def attendActivity(self):
        pass
print(issubclass(undergradute,Student))
print(issubclass(object,Student))
print(issubclass(Student,object))
# classinfo 取值也可能为元组，若 class 是元组内某个元素类型的子类，也会返回 True：
print(issubclass(int,(int,float)))
# roperty(fget=None, fset=None, fdel=None, doc=None)
# 返回 property 属性。不适用装饰器，定义类上的属性：
print('====================================')
# property(fget=None, fset=None, fdel=None, doc=None)
# 返回 property 属性。不适用装饰器，定义类上的属性：
class Student:
    def __init__(self):
        self._name = None
    def get_name(self):
        return self._name
    def set_name(self,val):
        self._name = val
    def del_name(self):
        del self._name
    #     # # 显示调用 property 函数
    name = property(get_name,set_name,del_name,'name property')

xiaofeng = Student()
xiaofeng.name='xiaofeng'
print(xiaofeng.name)
print('=========================================')
class Student:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @name.deleter
    def name(self):
        del self._name
xiaowu = Student()
xiaowu.name = 'xiaowu'
print(xiaowu.name)
print('===============================')
class Parent():
    def __init__(self,x):
        self.v = x
    def add(self,x):
        return self.v+x
class Son(Parent):
        def add(self,y):
            r = super().add(y)
            print(r)
print(Son(1).add(2))
print('=============================')
# allable(object)　
# 判断对象是否可被调用，能被调用的对象就是一个 callable 对象，比如函
# 数 str、int 等都是可被调用的。
print(callable(str))
print(callable(int))
print('===================')
class Student():
    def __init__(self,id=None,name=None):
           self.id = id
           self.name = name
xiaozhang = Student('002','xiaozhang')
print(callable(xiaozhang))

print('=================')
class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __call__(self, *args, **kwargs):
        print('i can be called')
        print(f'my name is {self.name}')
t = Student('007','xiaozhao')
t()
print(callable(t))