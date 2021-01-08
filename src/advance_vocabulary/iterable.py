from collections import Iterable
from collections import Iterator

s = isinstance([],Iterable)
print(s)

s1 = isinstance({},Iterable)
print(s1)

s2 = isinstance('abc',Iterable)
print(s2)

s3 = isinstance((x for x in range(10)),Iterable)
print(s3)

s4 = isinstance(100,Iterable)
print(s4)

# =====================
print('=================================')
s_1 = isinstance([],Iterator)
print(s_1)
s2_1 = isinstance('abc',Iterator)
print(s2_1)
s3_1 = isinstance((x for x in range(10)),Iterator)
print(s3_1)
s4_1 = isinstance(100,Iterator)
print(s4_1)
# =====================
print('===========================')
sk = isinstance(iter([]),Iterator)
print(sk)
sk_1 = isinstance(iter('abc'),Iterator)
print(sk_1)