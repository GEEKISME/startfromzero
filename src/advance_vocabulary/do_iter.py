# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们称为迭代（Iteration）,在Python中，迭代是通过for ... in来完成的。
# Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list
# 或tuple上，还可以作用在其他可迭代对象上(如生成器)。
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代
# 对象，无论有无下标，都可以迭代，比如dict就可以迭代:

dict_1 = {'a':1,'b':2,'c':3}
for key in dict_1:
    print(key)
    print(dict_1[key])

print('******************************************************')
for value in dict_1.values():
    print(value)
print('******************************************************')
for k,v in dict_1.items():
    print(k,v)
print('******************************************************')
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABC':
    print(ch)
#所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
# 而我们不太关心该对象究竟是list还是其他数据类型。那么，如何判断一个对象是可迭代对象
# 呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))  # 输出false，整数是不可迭代的