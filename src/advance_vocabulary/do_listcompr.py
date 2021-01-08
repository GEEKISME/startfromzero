print(list(range(1,11)))
print(list(range(2,11)))
ret = [x*x for x in range(1,11)]
print(ret)

s1 = [x*x for x in range(1,11) if x%2==0]
print(s1)
s2 = [m+n for m in 'ABC' for n in 'XYZ']
print(s2)
import os
s3 = [d for d in os.listdir('..')]
print(s3)
d = {'x':'a','y':'b','z':'c'}
for k,v in d.items():
    print(k,'=',v)
s4 = [k+'='+v for k,v in d.items()]
print(s4)

L = ['Amazon','IBM','Apple']
s5 = [s.lower() for s in L]
print(s5)

s6 = [x for x in range(1,11) if x % 2 ==0]
print(s6)
s7 = [x if x%2==0 else -x for x in range(1,11)]
