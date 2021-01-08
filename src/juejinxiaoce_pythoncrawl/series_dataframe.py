import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(['a','b','c'])
print(s)

s1 = pd.Series(['a','b','c'],index=['x','y','z'])
print(s1)

print(s1['x'])

s2 = s1[:2]
print(s2)
print('====================================')
s3 = pd.Series({1:'a',2:'b',3:'c'})
print(s3)
print('====================================')
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]
        }
df = pd.DataFrame(data)
print(df)
print('====================================')
# 随机生成6行4列的二维数组
df = pd.DataFrame(np.random.randn(6,4))
print(df)
print('====================================')
dates = pd.date_range('20200304',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)
print(df.columns)
print(df.index)
print(df.values)
print(df.head(3))
print(df.tail())
print('=================================')
# 按照列索引的降序排列：D->C->B->A
print(df.sort_index(axis=1,ascending=False))
# 按照行索引的降序排列：2012-01-06->...->2013-01-01
print(df.sort_index(axis=0,ascending=False))
# 根据B列的值的升序排列
print(df.sort_values(by='B'))
# 先按A的升序排，再按B的降序排
print(df.sort_values(by=['A','B'], ascending=[True, False]))
print('============================================')
# 选择一列，返回 Series 对象
print(df['A'])
# # 选择多列，返回 DataFrame 对象
print(df[['A','B']])
# 切片
print(df[0:3])
# # 通过行索引切片获取指定列数据
print(df.loc["2020-03-04":"2020-03-05",['A','B']])
# 通过行号切片获取（1到4行，0到2列）数据
print(df.iloc[1:4,0:2])
# 通过条件过滤数据
print(df[df.A>0])
print('=====================================')
print(df.sum())
print('=====================================')
print(df.mean())
print('=====================================')
print(df.max())
print('=====================================')
print(df.min())
print('=====================================')
print(df.groupby('A').size())




