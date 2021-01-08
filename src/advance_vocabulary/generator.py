# L = [x*x for x in range(10)]
# print(L)
# print(type(L))
# g = (x*x for x in range(10))
# print(type(g))
# for n in g:
#     print(n)
# =================================================
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a+b
#         n = n+1
#     return 'done'
# fib(6)
# fib(100)
# ====================================
# def fib(max):
#     n,a,b = 0,0,1
#     while n<max:
#         yield b
#         a,b = b,a+b
#         n = n+1
#     return 'done'
#
# f = fib(6)
# print(type(f))
# for n in f:
#     print(n)
# ====================================
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd()
# print(type(next(o)))
next(o)
next(o)
next(o)
next(o)