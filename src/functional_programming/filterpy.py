
# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把
# 传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
def is_odd(n):
    return n%2==1
s = filter(is_odd,[1,2,4,5,6,9,10,15])
print(type(s))
# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
# 需要用list()函数获得所有结果并返回list。
print(list(s))
print('=============================')
def not_empty(s):
    return s and s.strip()
s1 = filter(not_empty,['A','','B',None,'C',' '])
print(type(s1))
print(list(s1))
print('===========================================')
# 下面开始找素数
# 首先素数肯定是奇数不可能是偶数，因为偶数肯定能被2整除，因此我们从奇数序列开始
# 下面是一个生成器，生成一个无限的技术序列
def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n <1000:
        print(n)
    else:
        break