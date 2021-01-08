# 位置参数
def power(x):
    return x*x

x = power(2)
print(x)

print('**********************************')
# 默认参数
def power_n(x,n=2):
    s = 1;
    while n>0:
        n = n-1
        s = s*x
    return s

print(power_n(5))
print(power_n(5))

print('*************************************')


def enroll(name,gender,age = 6,city = 'Shanghai'):
    print('name',name)
    print('gender',gender)
    print('age',age)
    print('city',city)

enroll('Sarah','F')
enroll('Bob','M',7)
enroll('Adam','M',city='Tianjin')

# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L
# 也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用
# 时，默认参数的内容就变了，不再是函数定义时的[]了。

print('******************************************')
# 可变参数
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以
# 把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
s1 = calc([1,2,3])
print(s1)
# 上面还要组tuple获取这list,更简洁的方法如下,我们把函数的参数改为可变参数：

def calc_1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数,免去自己组装tuple
# 或者list的麻烦：
print(calc_1(1,2,3))
print(calc_1(1,3,5,7))
# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1,2,3]
print(calc_1(nums[0],nums[1],nums[2]))
# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple
# 前面加一个*号，把list或tuple的元素变成可变参数传进去：
print(calc_1(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有
# 用，而且很常见。

print('**************************************')
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组
# 装为一个dict。请看示例：
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只
# 传入必选参数：
print(person('Mical',30))
print(person('Bob',40,city='beijing'))
print(person('Adam',50,gender = 'M',job='engineer'))
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack',24,city=extra['city'],job=extra['job']))
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参
# 数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影
# 响到函数外的extra。
print(person('Jack',24,**extra))

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键
# 字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、
# 默认参数、可变参数、命名关键字参数和关键字参数。
