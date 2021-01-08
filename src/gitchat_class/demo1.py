# list = [1,2,3]
# print(list)
# tup = (1,2,3)
# print(tup)
# tup1 = (1,)
# print(tup1)
# tup2 = (1)
# print(tup2)
# print(type(tup2))
# print(type(tup1))
# print(type(list))
#=================================
# def score_mean(lst):
#     lst.sort()
#     lst2 = lst[1:-1]
#     return round(sum(lst2)/len(lst2),1)
# lst = [9.1,9.0,8.1,9.7,19,8.2,8.6,9.8]
#
# temp = score_mean(lst)
# print(temp)
# ====================================
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(j,i,j*i),end='\t')
# ===========================================
# from random import randint,sample
# lst = [randint(0,50) for _ in range(100)]
# print(lst[:5])
# print(lst)
# lst_sample = sample(lst,10)
# print(lst_sample)

# s = 'I love python\t\n'.strip()
# print(s)
# ss = 'I love python'.replace(' ','_')
# print(ss)
# sss = '_'.join(['book','store','count'])
# print(sss)
# ssss = 'I love python'.title()
# print(ssss)
# sa = 'I love python'.find('python')
# print(sa)
# ===================================
# def is_rotation(s1:str,s2:str)->bool:
#     if s1 is None or s2 is None:
#         return False
#     if len(s1)!=len(s2):
#         return False
#     def is_substring(s1:str,s2:str)->bool:
#         return s1 in s2
#     return is_substring(s1,s2+s2)
# r = is_rotation('stringbook','bookstring')
# print(r)
# se = is_rotation('greatman','maneatgr')
# print(se)
# ======================================
# import re
# pat = re.compile(r'[\da-zA-Z]{6,20}')
# q3=pat.fullmatch('qaz12')
# q2=pat.fullmatch('qaz12wsxedcrfvtgb678909422343434')
# q1 = pat.fullmatch('qaz_231')
# print(q1)
# print(q2)
# print(q3)
# =========================================
# class Dog(object):
#     def __init__(self,name,dtype):
#         self.__name = name
#         self.__dtype = dtype
#     def shout(self):
#         print('I\'m %s,type : %s'% (self.__name,self.__dtype))
#     def get_name(self):
#         return self.__name;
#     pass
# wangwang = Dog('wangwang','cute_type')
# # print(wangwang.name)
# # print(wangwang.dtype)
# wangwang.shout()
# # wangwang.name = 'doge'
# print(wangwang.get_name())
# ========================================================
class Book(object):
    def __init__(self,name,sale):
        self.__name = name
        self.__sale = sale
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name = new_name

a_book = Book('magic_book',10000)
print(a_book.name)
a_book.name = 'magic_book_2.0'
print(a_book.name)

