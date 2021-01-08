# 准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，
# 字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，
# 以及字节和int，float的转换。

# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得
# 配合位运算符这么写：
import struct
