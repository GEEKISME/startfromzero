a = range(0,11)
b = [x**2 for x in a]
print(b)
a = range(0,10)
b = [str(i) for i in a]
print(b)
from random import random
a = [round(random(),2) for _ in range(10)]
print(a)

a = range(11)
c = [x**2 for x in a if x%2==0]
print(c)

a = [i*j for i in range(10) for j in range(1,i+1)]
print(a)

a = range(5)
print(a)
b = ['a','b','c','d','e']
c = [str(y)+str(x) for x ,y in zip(a,b)]
print(c)
print('=====================')
a = {'a':1,'b':2,'c':3}
b = [k+ '=' + str(v) for k, v in a.items()]
print(b)
print('==========================')
import os
dirs = [d for d in os.listdir('F:\A5CowSystem') ]
dirs_1 = [d for d in os.listdir('F:/A5CowSystem') if os.path.isfile(d)]
print(dirs_1)
print('=============================')
a = ['Hello', 'World','2019Python']
print([w.lower() for w in a])
a1 = ['Hello', 'World',2020,'Python']
s = [str(w).lower() for w in a1]
print(s)

s2 = [w.lower() for w in a1 if isinstance(w,str)]
print(s2)
print('=========================================')
def filter_non_unique(lst):
    return [item for item in lst if lst.count(item) == 1]
sk = filter_non_unique([1, 2, 2, 3, 4, 4, 5])
print(sk)
print('=========================================')
def bifurcate(lst,filter):
    return [
        [x for i,x in enumerate(lst) if filter[i]==True],
        [x for i,x in enumerate(lst) if filter[i]==False]
    ]

sk_1 = bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
print(sk_1)
print('==============================================')
def bifurcate_by(lst,fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]
sk_2 = bifurcate_by(['Python3', 'up', 'users', 'people'], lambda x: x[0] == 'u')
print(sk_2)

def difference(a,b):
    _a,_b = set(a),set(b)
    return [item for item in _a if item not in _b]
sk_3 = difference([1,1,2,3,3], [1, 2, 4])
print(sk_3)

print('=================================')
def difference_by(a,b,fn):
    _b = set(map(fn,b))
    return [item for item in a if fn(item) not in _b ]
from math import floor
sk_4 = difference_by([2.1, 1.2], [2.3, 3.4],floor)
print(sk_4)
m = difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
print(m)