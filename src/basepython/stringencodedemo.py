# Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非
# 常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。
# 现在，捋一捋ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码
# 通常是2个字节。
# 汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制
# 的01001110 00101101。
# 你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。
#
# 新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文
# 本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存
# 储和传输上就十分不划算。
# 在计算机内存中，统一使用Unicode编码(2个字节)，当需要保存到硬盘或者需要传输的时候，
# 就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再
# 把Unicode转换为UTF-8保存到文件：
# 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
print('包含中文的str')
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网
# 络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
s = 'ABC'.encode('ascii')
print(s)
s2 = '中文'.encode('utf-8')
print(s2)
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编
# 码的范围超过了ASCII编码的范围，Python会报错。