import psutil

# 2说明是双核超线程, 4则是4核非超线程
# s = psutil.cpu_count()
# print(s)
# s1 = psutil.cpu_count(logical=False)
# print(s1)
# s2 = psutil.cpu_times()
# print(s2)
# for x in range(10):
#     s3 = psutil.cpu_percent(interval=1,percpu=True)
#     print(s3)
#
s4 = psutil.virtual_memory()
print(s4)
s5 = psutil.swap_memory()
print(s5)