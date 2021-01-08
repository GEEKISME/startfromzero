# 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实
# 现了上下文管理，就可以用于with语句。
#
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实
# 现了这两个方法：

# class Query(object):
#
#     def __init__(self,name):
#         self.name = name
#     def __enter__(self):
#         print('begin')
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print('error')
#         else:
#             print('end')
#     def query(self):
#         print('Query info about %s...' %self.name)
# with Query('bob') as q:
#     q.query()
print('=============================')
from contextlib import contextmanager

# class Query(object):
#     def __init__(self,name):
#         self.name = name
#     def query(self):
#         print('Query info about %s...' %self.name)
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
# with create_query('Bob') as q:
#     q.query()
print('===================================')
# 代码的执行顺序是：
#
# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。
# 因此，@contextmanager让我们通过编写generator来简化上下文管理。
# @contextmanager
# def tag(name):
#     print('<%s>' %name)
#     yield
#     print('<%s>' %name)
# with tag('h1'):
#     print('hello')
#     print('world')
# =============================
print('================================')
