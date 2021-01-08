import pandas as pd

s1 = pd.Series([3,5,7])
print(s1)
print(type(s1))
print('============================')
s2 = pd.Series([3,5,7],index=list('ABC'),name='s3')
print(s2)
print('==============================')
df = pd.DataFrame([[9,0,1],[7,3,10]],index=['a','b'],columns=['A','B','C'])
print(df)
print('==================================')
df= pd.DataFrame({'A':[9,7],'B':[0,3],'C':[1,10]},index=['a','b'])
print(df)