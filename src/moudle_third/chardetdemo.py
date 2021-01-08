import chardet
s = chardet.detect(b'Hello World!')
print(s)
data = '离离原上草，一岁一枯荣'.encode('gbk')
s1 = chardet.detect(data)
print(s1)
data = '离离原上草，一岁一枯荣'.encode('utf-8')
s2 = chardet.detect(data)
print(s2)