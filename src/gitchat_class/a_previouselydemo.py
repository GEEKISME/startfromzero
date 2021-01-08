# Python的位置参数、默认参数、关键字参数、可变参数区别
a = (1,2,3)
b,c,d = a
print(b)
print(c)
print(d)
print('===========================')
def print_hello(name,sex):
    sex_dict = {1:'先生',2:'女士'}
    print('hello %s %s,welcome to python world!' %(name,sex_dict.get(sex,'先生')))

print_hello('lixiaohui',1)
print_hello(sex=2,name='lixiaohui')
print('===========================')
# # 正确的默认参数定义方式--> 位置参数在前，默认参数在后
# 三、可变参数：
#
# 定义函数时，有时候我们不确定调用的时候会传递多少个参数(不传参也可以)。
# 此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。
def func(*args):
    for i in args:
        print(i)
func()
print('===========')
func('a')
func('a','b')
func('a',1)

print('=====================')
def funcv(**kwargs):
    print(kwargs)
funcv(a=1)
funcv(a=1,b=2,c=3)

print('=================================')
def print_sp(name,sex):
    print(name,sex)
args = ('lixiaohui','male')
print_sp(*args)
print('===================================')
def func(name,age,sex=1,*args,**kargs):
    print(name,age,sex,args,kargs)
func('lxh',25,2,'music','sport',a=1,b=2)
print('=====================================')
# *args 表示任何多个无名参数，它是一个tuple；**kwargs 表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前，否则会报语法错误！！！
#
# 作者：快乐的bug制造者
# 链接：https://www.jianshu.com/p/c4c27db76f66
# 来源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
def foo(*args,**kwargs):
    print(args)
    print(kwargs)
    print('===============================')
foo(1,2,3,4)
foo(a=1,b=2,c=3)
foo(1,2,3,4, a=1,b=2,c=3)
foo('a', 1, None, a=1, b='2', c=3)
print('=====================================')
# 总结：
#
# 位置参数：
#
# 调用函数时所传参数的位置必须与定义函数时参数的位置相同
#
# 关键字参数：
#
# 使用关键字参数会指定参数值赋给哪个形参，调用时所传参数的位置可以任意
#
# *位置参数：可接受任意数量的位置参数(元组)；只能作为最后一个位置参数出现，其后参数均为关键字参数
#
# **关键字参数：可接受任意数量的关键字参数(字典)；只能作为最后一个参数出现
#
