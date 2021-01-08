# empty = []
# lst = [1,'xiaoming',29.5,'17312662388']
# lst2 = ['001','2019-11-11',['三文鱼','电烤箱']]
# print(empty)
# print(lst)
# print(lst2)
# print(len(empty))
# print(len(lst))
# print(len(lst2))
#
# for i in lst:
#     print(f'{i}的类型是{type(i)}')
#
# sku = lst2[2]
# print(sku)
# sku.append('烤鸭')
# print(sku)
# sku.insert(1,'牛肚')
# print(sku)
# item = sku.pop()
# print(item)
# print(sku)
# sku.remove('三文鱼')
# print(sku)
# print(lst2)
# sku_deep = lst2[2].copy()
# print(sku_deep)
# sku_deep[0] = '肚'
# print(sku_deep)
# print(lst2)
# ========================================
# a = list(range(1,20,3))
# print(a)
# b = a[:3]
# print(b)
# c = a[-1]
# print(c)
# d = a[:-1]
# print(d)
# e = a[1:5]
# print(e)
# f = a[1:5:2]
# print(f)
# g = a[::3]
# print(g)
# h = a[::-3]
# print(h)
#
# def reverse(lst):
#     return lst[::-1]
#
# ra = reverse(a)
# print(ra)
# ================================================
# a = ()
# b = (1,'xiaoming',29.5,'17312662388')
# c = ('001','2019-11-11',['三文鱼','电烤箱'])
# from numpy import random
# a = random.random_integers(1,5,10)
# print(type(a))
# at = tuple(a)
# print(at)
# print(at.count(3))
# ===========================================
# a = [1,3,[5,7],9,11,13]
# print(a)
# a.pop()
# print(a)
# a.insert(3,8)
# print(a)
# a[2].insert(1,6)
# print(a)
# print('=======================================')
b = (1,3,[5,7],9,11,13)
print(b)
b[2].insert(1,6)
print(b)
