d = {'a':1,'b':2}
print(d)
d.update({'c':3,'d':4,'e':5})
print(d)
d.update([('f',6),('g',7)])
print(d)
print('======================')
d = {'a':1,'b':2}
print(d)
r = d.setdefault('c',3)
print(r)
print(d)
r = d.setdefault('c',33)
print(r)
print(d)
print('================================')
def f(d:dict)->dict:
    return {**d}
s = f({'a':1,'b':2})
print(s)

print('=============================')
def merge(d1,d2):
    return {**d1,**d2}

c = merge({'a':1,'b':2},{'c':3})
print(c)
print('=====================================')
def difference(d1,d2):
    return dict([(k,v) for k,v in d1.items() if k not in d2])
s = difference({'a':1,'b':2,'c':3},{'b':2})
print(s)
print('======================================')
# 5. 按键排序
def sort_by_key(d):
    return sorted(d.items(),key=lambda x:x[0])
s2 = sort_by_key({'a':3,'c':1,'b':2})
print(s2)
print('====================================')
# 6. 按值排序
# 与按照键排序原理相同，按照值排序时，key 函数定义为按值（x[1]）比
# 较。为照顾小白，解释为什么是 x[1]。
def sort_by_value(d):
    return sorted(d.items(),key=lambda x:x[1],reverse=False)
s3 = sort_by_value({'a':3,'b':1,'c':2})
print(s3)
print('====================================')
# 7. 最大键
# 通过 keys 拿到所有键，获取最大键，返回 (最大键,值) 的元组
def max_key(d):
    if len(d) == 0:
        return
    max_key = max(d.keys())
    return (max_key,d[max_key])
s = max_key({'a':3,'c':3,'b':2})
print(s)
print('============================')
# 8. 最大字典值
# 最大值的字典，可能有多对：
def max_value(d):
    if len(d)==0:
        return []
    max_value = max(d.values())
    return [(key,max_value) for key in d if d[key]==max_value]
k1 = max_value({'a':3,'c':3,'b':2})
print(k1)
# 9. 集合最值
# 找出集合中的最大、最小值，并装到元组中返回：
print('=================')
def max_min(s):
    return (max(s),min(s))
k2 = max_min({1,3,4,5,7})
print(k2)
# 10. 单字符串
# 若组成字符串的所有字符仅出现一次，则被称为单字符串。
print('=================================')
def single(string):
    return len(set(string)) == len(string)
s = single('love_python')
print(s)
s = single('python')
print(s)
# 11. 更长集合
# key 函数定义为按照元素长度比较大小，找到更长的集合：
def longer(s1,s2):
    return max(s1,s2,key=lambda x:len(x))
s = longer({1,3,5,7},{1,5,7})
print(s)
print('==============================')
# 12. 重复最多
# 在两个列表中，找出重叠次数最多的元素。默认只返回一个。
#
# 解决思路：
#
# 求两个列表的交集
# 遍历交集列表中的每一个元素，min(元素在列表 1 次数, 元素在列表 2 次数) ，就是此元素的重叠次数
# 求出最大的重叠次数
def max_overlap(lst1,lst2):
    overlap = set(lst1).intersection(lst2)
    ox = [(x,min(lst1.count(x),lst2.count(x))) for x in overlap]
    return max(ox,key=lambda x:x[1])
s = max_overlap([1,2,2,2,3,3],[2,2,3,2,2,3])
print(s)
# 13. topn 键
# 找出字典前 n 个最大值，对应的键。
#
# 导入 Python 内置模块 heapq 中的 nlargest 函数，获取字典中的前 n 个最大值。
print('===================================')
from heapq import nlargest
def topn_dict(d,n):
    return nlargest(n,d,key=lambda k :d[k])
s = topn_dict({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3)
print(s)
# 14. 一键对多值字典
# 一键对多个值的实现方法 1，按照常规思路，循序渐进：
d = {}
lst = [(1,'apple'),(2,'orange'),(1,'compute')]
for k,v in lst:
    if k not in d:
        d[k] = []
    d[k].append(v)
print(d)
print('=================================')
from collections import defaultdict

d = defaultdict(list)
for k,v in lst:
    d[k].append(v)
print(d)
# 15. 逻辑上合并字典
# 案例 3 中合并字典的方法：
print('=============================')
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged = {**dic1, **dic2}
print(merged)
print('================================')
from collections import ChainMap
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged = ChainMap(dic1,dic2)
print(merged)
merged['x'] = 10
print(dic1)