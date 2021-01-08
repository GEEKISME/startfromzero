import  time

seconds = time.time()
print(seconds)

local_time = time.localtime(seconds)
print(local_time)

str_time = time.asctime(local_time)
print(str_time)

format_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
print(format_time)

str_to_struct = time.strptime(format_time,'%Y-%m-%d %H:%M:%S')
print(str_to_struct)
print('================================')
from datetime import date,datetime,time,timedelta

tod = date.today()
print(tod)
str_date = date.strftime(tod,'%Y-%m-%d')
print(str_date)
str_to_date = datetime.strptime('2020-02-22','%Y-%m-%d')
print(str_to_date)
print('=================================')
right = datetime.now()
print(right)
str_time = datetime.strftime(right,'%Y-%m-%d %H:%M:%S')
print(str_time)

str_to_time = datetime.strptime('2020-02-22 15:12:33','%Y-%m-%d %H:%M:%S')
print(str_to_time)
print('===========================================')
def get_days_girlfriend(birthday:str)->int:
    import re
    splits = re.split(r'[-.\s+/]',birthday)
    splits = [s for s in splits if s] # 去掉空格字符
    if len(splits) < 3:
        raise ValueError('输入格式不正确，至少包括年月日')
    splits = splits[:3] # 只截取年月日
    birthday = datetime.strptime('-'.join(splits),'%Y-%m-%d')
    tod = date.today()
    delta = birthday.date() - tod
    return delta.days

s = get_days_girlfriend('2020-04-13')
print(s)
s1 = get_days_girlfriend('2020/5/20')
print(s1)
print('============================================')
import calendar
from datetime import date
mydate = date.today()
year_calender_str = calendar.calendar(2020)
print(f"{mydate.year}年的日历图：{year_calender_str}\n")
print('===========================')
import calendar
from datetime import date
mydate = date.today()
month_calender_str = calendar.month(mydate.year,mydate.month)
print(f"{mydate.year}年-{mydate.month}月的日历图：{month_calender_str}\n")
print('===============================')
import calendar
from datetime import  date
mydate = date.today()
is_leap = calendar.isleap(mydate.year)
print_leap_str = "%s年是闰年" if is_leap else "%s年不是闰年\n"
print(print_leap_str %mydate.year)
print('=====================================================')
import calendar
from datetime import date

mydate = date.today()
weekday, days = calendar.monthrange(mydate.year, mydate.month)
print(f'{mydate.year}年-{mydate.month}月的第一天是那一周的第{weekday}天\n')
print(f'{mydate.year}年-{mydate.month}月共有{days}天\n')
print('======================================')
from datetime import date
mydate = date.today()
month_first_day = date(mydate.year, mydate.month, 1)
print(f"当月第一天:{month_first_day}\n")
print('===================================')
from datetime import date
import calendar
mydate = date.today()
_, days = calendar.monthrange(mydate.year, mydate.month)
month_last_day = date(mydate.year, mydate.month, days)
print(f"当月最后一天:{month_last_day}\n")
print('==========================================')
