# Day 9：Python 字符串和正则介绍总结
# 字符串无所不在，字符串的处理也是最常见的操作。
#
# 今天，一起学习字符串处理相关的操作。主要包括：
#
# 基本的字符串操作
# 高级字符串操作之正则部分
# Python中有.join()和os.path.join()两个函数，具体作用如下：
#    . join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接
#    生成一个新的字符串
#     os.path.join()：  将多个路径组合后返回
# #对序列进行操作（分别使用'  ' 、' - '与':'作为分隔符）
a = ['1','2','3','4','5']
print(';'.join(a))
print(''.join(a))
print('.'.join(a))
# #对字符串进行操作（分别使用'  ' 、' - '与':'作为分隔符）
b = 'hello world'
print(''.join(b))
print(' '.join(b))
print('  '.join(b))
print('-'.join(b))
print(';'.join(b))
# #对元组进行操作（分别使用'  ' 、' - '与':'作为分隔符）
c=('1','2','3','4','5')
print(''.join(c))
print('-'.join(c))
print(';'.join(c))
#对字典进行无序操作（分别使用'  ' 、' - '与':'作为分隔符）
d={'name1':'a','name2':'b','name3':'c','name4':'d'}
print(''.join(d))
print('-'.join(d))
print(';'.join(d))
print('.'.join(d))
# #对目录进行操作
import os
print(os.path.join('/hello/','good/date','datbody'))
# =======================================================
print('==================================')
s = 'python'
rs = ''.join(reversed(s))
print(rs)
print(s[::-1])
print('==========================================')
# 字符串切片操作
# 生成 1 到 15 的序列，并在满足条件的索引处，替换为 java 或 python。
java,python = 'java','python'
jl,pl = len(java),len(python)
s = [str(java[i%3*jl:]+python[i%5*pl:] or i) for i in range(1,10)]
print(s)
print('==========================================')
# join 串联字符串
# 用下划线 _ 连接字符串 mystr：
mystr = ['i','love','python']
res = '_'.join(mystr)
print(res)
print('==========================================')
# 分割字符串
# 根据指定字符或字符串，分割一个字符串时，使用方法 split。
#
# join 和 split 可看做一对互逆操作：
s = 'i_love_python'.split('_')
print(s)
print('==========================================')
# 替换
# 字符串替换，使用 replace 方法。
#
# 如下字符串，小写的 o 全部替换为大写的 O：
s = 'i love python'.replace('o','0')
print(s)
print('==========================================')
# 子串判断
# 判断 a 串是否为 b 串的子串。
# 方法 1，使用 in：
a = 'our'
b = 'flourish'
r = True if a in b else False
print(r)
# 方法 2，使用方法 find，返回字符串 b 中匹配子串 a 的最小索引：
print(b.find(a))
print('==========================================')
# 去空格
# 清洗字符串时，位于字符串开始和结尾的空格，有时需要去掉，strip 方法能实现。
#
# 如下字符串，使用 strip，清理字符串开头和结尾的空格和制表符。
a = '  \tI love python  \b\n'
print(a)
print(a.strip())
# 字符串的字节长度
# encode 方法对字符串编码后：
print('==========================================')
def str_byte_len(my_str):
    mystr_byte = my_str.encode('utf-8')
    return (len(mystr_byte))


print(str_byte_len('i love python'))
print('==========================================')
# 正则表达式
# 字符串封装的方法，处理一般的字符串操作，还能应付。但是，稍微复杂点的字符串处理任务，需要靠正则表达式，简洁且强大。
#
# 首先，导入所需要的模块 re：
import re
# 正则表达式，常会涉及到以上这些元字符或通用字符，下面通过 14 个细分的与正则相关的小功能，讨论正则表达式。
s = 'i love python very much'
pat = 'python'
r = re.search(pat,s)
print(r.span())
print('=================================')
# match 与 search 不同
# 正则模块中，match、search 方法匹配字符串不同
#
# 具体不同：
#
# match 在原字符串的开始位置匹配
# search 在字符串的任意位置匹配
# 原字符串：
s = 'flourish'
# 寻找模式串 our，使用 match 方法：
recom = re.compile('our')
s1 = recom.match(s)
print(s1)
s2 = recom.search(s)
print(s2)
print(s2.span()) ## OK, 匹配成功，our 在原字符串的起始索引为 2
# 那么，什么字符串才能使用 match 方法匹配到 our？
#
# 比如，字符串 ourselves，ours 才能 match 到 our。
print('=================================')
# finditer 匹配迭代器
# 使用正则模块，finditer 方法，返回所有子串匹配位置的迭代器。
#
# 通过返回的对象 re.Match，使用它的方法 span 找出匹配位置。
s = '山东省潍坊市青州第1中学高三1班'
pat = '1'
r = re.finditer(pat,s)
for i in r:
    print(i)
    print(i.span())
print('====================================')
# findall 所有匹配
# 正则模块，findall 方法能查找出子串的所有匹配。
#
# 原字符串 s：
s = '一共20行代码运行时间13.59s'
# 目标查找出所有所有数字：通用字符 \d 匹配一位数字 [0-9]，+ 表示匹配数字前面的一个字符 1 次或多次。
pat = r'\d+'
r = re.findall(pat,s)
print(r)
# 返回一个列表，找到三个数字 20、13、59，没有达到预期，期望找到 20、13.59。
#
# 因此，需要修改正则表达式。
# 案例：匹配浮点数和整数
# ? 表示前一个字符匹配 0 或 1 次
# .? 表示匹配小数点（.）0 次或 1 次。
# 匹配浮点数和整数，第一版正则表达式：r'\d+\.?\d+'，图形化演示，此正则表达式的分解演示：
pat = r'\d+\.?\d+'
r= re.findall(pat,s)
print(r)
# 上面的正则表达式 r'\d+\.?\d+'，能适配所有情况吗？
s = '一共2行代码运行时间1.66s'
r = re.findall(pat,s)
print(r)
# 观察结果，没有匹配到数字 2。
#
# 正则难点之一，需要考虑全面、足够细心，才可能写出准确无误的正则表达式。
#
# 出现问题原因：r'\d+\.?\d+'，后面的 \d+ 表示至少有一位数字，因此，整个表达式至少会匹配两位数。
#
# 修复问题，重新优化正则表达式，将最后的 + 后修改为 *，表示匹配前面字符 0 次、1 次或多次。
#
# 最终正则表达式为：r'\d+\.?\d*'，正则分解图：
pat = r'\d+\.?\d*'
r = re.findall(pat,s)
print(r)
# 案例：匹配正整数
# 案例：写出匹配所有正整数的正则表达式。
#
# 如果这样写：^\d*$，会匹配到 0，所以不准确。
#
# 如果这样写：^[1-9]*，会匹配 1. 串中 1，不是完全匹配，体会 $ 的作用。
#
# 正确写法：^[1-9]\d*$，正则分解图：
s = [-16, 1.5, 11.43, 10, 5]
pat = r'^[1-9]\d*$'
print([i for i in s if re.match(pat,str(i))])
# re.I 忽略大小写
# re.I 是方法的可选参数，表示忽略大小写。
#
# 如下，找出字符串中所有字符 t 或 T 的位置，不区分大小写。
print('==================================')
s = 'That'
pat = r't'
r = re.finditer(pat,s,re.I)
for i in r:
    print(i.span())

print('=======================================')
# split 分割单词
# 正则模块中 split 函数强大，能够处理复杂的字符串分割任务。
#
# 如果一个规则简单的字符串，直接使用字符串，split 函数。
#
# 如下字符串，根据分割符 \t 分割：
s = 'id\tname\taddress'
print(s.split('\t'))
# 但是，对于分隔符复杂的字符串，split 函数就无能为力。
#
# 如下字符串，可能的分隔符有 ,、;、\t、|。
s = 'This,,,   module ; \t   provides|| regular ; '
words = re.split('[,\s;|]+',s)
print(words)
print('==================================')
# sub 替换匹配串
# 正则模块，sub 方法，替换匹配到的子串：
content="hello 12345, hello 456321"
pat=re.compile(r'\d+') #要替换的部分
m=pat.sub("666",content)
print(m)