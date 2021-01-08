# def is_duplicated(lst):
#     for x in lst:
#         if lst.count(x) > 1:
#             return True
#         return False
#
# a = [1,-2,3,4,1,2]
# print(is_duplicated(a))
# # =====================================
# def reverse(lst):
#     return lst[::-1]
# r = reverse([1,-2,3,4,1,2])
# print(r)
# ============================================
# def find_duplicated(lst):
#     ret = []
#     for x in lst:
#         if lst.count(x) >1 and x not in ret:
#             ret.append(x)
#     return ret
# r = find_duplicated([1,2,3,4,3,2])
# print(r)
# ==============================================
# def fibonacci(n):
#     if n <= 1:
#         return [1]
#     fib = [1,1]
#     while len(fib) < n:
#         fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
#     return fib
#
# r = fibonacci(100)
# print(r)
# print('=========================================')
# def fibonaccis(n):
#     a,b = 1,1
#     for _ in range(n):
#         yield a
#         a,b = b,a+b
# print(list(fibonaccis(5)))
# =======================================================
# def mode(lst):
#     if lst is None or len(lst)==0:
#         return None
#     return max(lst, key=lambda v: lst.count(v))
# lst=[1,3,3,2,1,1,2]
# r = mode(lst)
# print(f'{lst}中出现次数最多的元素为：{r}')

# def mode2(lst):
#     if lst is None or len(lst)==0:
#         return None
#     max_freq_elem = max(lst,key=lambda v:lst.count(v))
#     max_freq = lst.count(max_freq_elem)
#     ret = []
#     for i in lst:
#         if i not in ret and lst.count(i) == max_freq:
#             ret.append(i)
#             return ret
# print(mode2([1,1,2,2,3,2,1]))
# ===============================================
# def max_len(*lists):
#     return max(*lists,key=lambda v:len(v))
# r = max_len([1,2,3],[4,5,6,7],[8])
# print(f'更长的列表是{r}')
# ===============================================
# def head(lst):
#     return lst[0] if len(lst) > 0 else None
# print(head([]))
# print(head([3,4,1]))

# def tail(lst):
#     return lst[-1] if len(lst) >0 else None
# print(tail([]))
# print(tail([3,4,1]))

# ===========================================

# def mul_table():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print(str(j)+str("*")+str(i)+"="+str(j*i),end="\t")
#         print()
# mul_table()
# ===============================================
# s = zip([1,2],[2,3])
# print(type(s))
# k = list(s)
# print(type(k))
# print(k)
# print('==========================================')
# def pair(t):
#     return list(zip(t[:-1],t[1:]))
#
# s = pair([1,2,3])
# print(s)
#
# k = range(10)
# print(type(k))
# print(k)
# print(pair(range(10)))
# ===============================
# from random import randint,sample
# lst = [randint(0,50) for _ in range(100)]
# print(lst)
# print(lst[:5])
# lst_sample = sample(lst,10)
# print(lst_sample)
# ==================================
# from random import shuffle,randint
#
# lst = [randint(0,50) for _ in range(100)]
# print(lst)
# shuffle(lst)
# print(lst)
# ==========================================
# from random import shuffle,randint,uniform
# x,y = [i for i in range(100)],[round(uniform(0,10),2) for _ in range(100)]
# print(y)
print('===========================================')
from pyecharts.charts import Scatter
import pyecharts.options as opts
from random import uniform
def draw_uniform_points():
    x,y = [i for i in range(100)],[round(uniform(1,10),2) for _ in range(100)]
    print(y)
    c = (Scatter().add_xaxis(x).add_yaxis('y',y))
    c.render()
draw_uniform_points()