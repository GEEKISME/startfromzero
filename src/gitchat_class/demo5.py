empty = {}
print(empty)
dic = {'a':1,'b':2,'c':3}
print(dic)

s = dict(a=1,b=2,c=3)
print(s)
s2 = {}.fromkeys(['k1','k2','k3'],[1,2,3])
print(s2)
s3 = {'a':1,'b':2}.fromkeys(['c','d'],[1,2])
print(s3)
print('================================')
d = {'a':1,'b':2,'c':3}
print(d)
print('=================================')
for k,v in d.items():
    print(k,v)
s4 = set(d.keys())
print(s4)
s5 = set(d.values())
print(s5)
print('=================================')
if 'c' in d:
    print('键c 在 字典d中')
if 'e' not in d:
    print('键e 不在字典d中')
print(d.get('c'))

d['d'] = 4
print(d)
print('==================================')
# 删除一个键值对：
# 方法一
del d['d']
print(d)
# 方法二
d.pop('c')
print(d)
print('===============================')
print(d.keys())
print(d.values())
print(d.items())
print('================================')
a = {'a':1,'b':2,'c':3}
key_lst = a.keys()
print(a)
print(key_lst)
print('===========================')
del a['b']
print(a)
print(key_lst)
print('================================')
a =  {'a':1, 'b':2, 'c':3}
items = a.items()
print(a)
print(items)
print('=================================')
a['c'] = 4
print(a)
print(items)
print('===================================')
# lst = [1,2]
# d = {lst:'ok?'}
# print(d)
print('=====================================')
# 集合是一种不允许元素出现重复的容器。
#
# 案例：判断一个列表中是否含有重复元素，便可借助集合这种数据类型。
def duplicated(lst):
    return len(lst)!=len(set(lst))

a = {1,2,3}
print(a)
b = set([1,2,3,4,5,6])
print(b)
print('=======================================')
a= {1,3,5,7}
b,c = {3,4,5,6},{6,7,8,9}
d = a.union(b,c)
print(d)
print('====================================')
f = a.difference(b,c)
print(f)
print('==================================')
a = {1,3,5,7}
b,c = {3,4,5,6},{3,6,7,8,9}

d = a.intersection(b,c)
print(d)
print('====================================')
a = {1,3,5,7}
b = {3,4,5,6}
print(a.issubset(b))

print(a.issubset(a))
print(a.issubset({1,3,5,7,8}))