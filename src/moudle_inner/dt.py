from datetime import datetime
# 注意到datetime是模块，datetime模块还包含一个datetime类，通
# 过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
# datetime.now()返回当前日期和时间，其类型是datetime。
now = datetime.now()
print(now)
print(type(now))
# 要指定某个日期和时间，我们直接用参数构造一个datetime：
dt = datetime(2020,2,24,17,1)
print(dt)
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
s = dt.timestamp()
print(s)
# timestamp转换为datetime
print(datetime.fromtimestamp(s))
# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(s))
print('====================================')
# =====================================
# str转换为datetime
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，
# 首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，
# 需要一个日期和时间的格式化字符串：
cday = datetime.strptime('2020-2-25 9:02:30','%Y-%m-%d %H:%M:%S')
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。
print(cday)
# =====================
print('====================')
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M:%S'))
print('=====================')
from datetime import timedelta
now = datetime.now()
print(now+timedelta(hours=10))
print('=======================')
print(now - timedelta(days=1))
print('=====================================')
from datetime import timezone
# # 创建时区UTC+8:00
tz_utc_8 = timezone(timedelta(hours=8))
print(datetime.now())