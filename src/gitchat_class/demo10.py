# Day 10：Python 文件操作 11 个案例总结
# Python 文件 IO 操作：
#
# 涉及文件读写操作
# 获取文件后缀名
# 批量修改后缀名
# 获取文件修改时间
# 压缩文件
# 加密文件等常用操作
import  os
def read_file(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError('%s not exist' %(filename,))
    with open(filename,encoding='utf-8') as f:
        content = f.read()
    return content
content =  read_file('F:/BaiduNetdiskDownload/haha.txt')
print(content)
# 文件按行读
# read 函数一次读取整个文件，readlines 函数按行一次读取整个文件。读入文件小时，使用它们没有问题。
#
# 但是，如果读入文件大，read 或 readlines 一次读取整个文件，内存就会面临重大挑战。
#
# 使用 readline 一次读取文件一行，能解决大文件读取内存溢出问题。
#
# 文件 a.txt 内容如下：
print('=====================================')
from collections import defaultdict
# 关于defaultdict的用法可见：https://www.cnblogs.com/summer1019/p/11233783.html
strings = ('puppy', 'kitten', 'puppy', 'puppy','weasel', 'puppy', 'kitten', 'puppy')
counts = defaultdict(int)
for kw in strings:
   counts[kw] += 1
print(counts)
print('========================================')
# defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化
# 一个值作为默认值默认值的类型由工厂函数决定。
dic1 = defaultdict(int)
print(dic1['a'])
dic2 = defaultdict(list)
print(dic2['a'])
dic3 = defaultdict(dict)
print(dic3['a'])

print('====================================')

from collections import defaultdict
import re

rec = re.compile('\s+')
dd = defaultdict(int)
with open('a.txt','r+') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
        clean_line = line.strip()
        if clean_line:
            words = rec.split(clean_line)
            for word in words:
               dd[word]+=1
dd = sorted(dd.items(),key=lambda x:x[1],reverse=True)
print('---print stat---')
print(dd)
print('--word done -----')
print('============================================')
import  os
def write_to_file(file_path,file_name):
    if os.path.exists(file_path) is False:
        os.mkdir(file_path)
    whole_path_filename = os.path.join(file_path,file_name)
    to_write_content = '''
                        Hey, Python
                        I just love Python so much,
                        and want to get the whole python stack by this 60-days column
                        and believe!
    '''
    with open(whole_path_filename,mode='w',encoding='utf-8') as f:
        f.write(to_write_content)
    print('-------write done--------')
    print('-------begin reading------')
    with open(whole_path_filename,encoding='utf-8') as f:
        content = f.read()
        print(content)
        if content == to_write_content:
            print('content is equal by reading and writing')
        else:
            print('----Warning: NO Equal-----------------')
write_to_file('F:\BaiduNetdiskDownload','lxh.aa')

print('===================================')
# 获取文件名
# 有时拿到一个文件名时，名字带有路径。这时，使用 os.path、split 方法实现路径和文件的分离。
import os
file_ext = os.path.split('F:\BaiduNetdiskDownload\lxh.aa')
ipath,ifile = file_ext
print(ipath)
print(ifile)
print(file_ext)
# 获取后缀名
# 如何优雅地获取文件后缀名？os.path 模块，splitext 能够优雅地提取文件后缀。
file_extension = os.path.splitext('F:\BaiduNetdiskDownload\lxh.aa')
print(file_extension[0])
print(file_extension[1])
print('=====================================================')
# 获取后缀名的文件
import os
def find_file(work_dir,extension='zip'):
    lst = []
    for filename in os.listdir(work_dir):
        print(filename)
        splits = os.path.splitext(filename)
        ext = splits[1] #拿到扩展名
        if ext =='.'+extension:
            lst.append(filename)
    return lst
r = find_file('F:\BaiduNetdiskDownload','zip')
print(r)
print('==============================================')
import argparse
import os
def get_parser():
    parser = argparse.ArgumentParser(description='工作目录中文件后缀名修改')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='修改后缀名的文件目录')
    parser.add_argument('old_ext', metavar='OLD_EXT',type=str, nargs=1,
                        help='原来的后缀')
    parser.add_argument('new_ext', metavar='NEW_EXT',type=str, nargs=1,
                        help='新的后缀')
    return parser
def batch_rename(work_dir,old_ext,new_ext):
    '''
    传递当前目录，原来后缀名，新的后缀名后，批量重命名后缀
    :param work_dir:
    :param old_ext:
    :param new_ext:
    :return:
    '''
    for filename in os.listdir(work_dir):
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        if file_ext==old_ext:
            newfile = split_file[0]+new_ext
            os.rename(
                os.path.join(work_dir,filename),
                os.path.join(work_dir,newfile)
            )
    print('Done !')
    print(os.listdir(work_dir))

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]

    if old_ext[0] !='.':
        old_ext = '.'+old_ext
    new_ext = args['new_ext'][0]
    if new_ext[0]!='.':
        new_ext = '.'+new_ext
    batch_rename(work_dir,old_ext,new_ext)

# batch_rename('F:\BaiduNetdiskDownload','.aa','.txt')
print('===========================================')
import os
from datetime import datetime
print(f"当前时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
def get_modify_time(indir):
    for root,_,files in os.walk(indir):# 循环目录和子目录
        for file in files:
            whole_file_name = os.path.join(root,file)
            modify_time = os.path.getmtime(whole_file_name)# 1581164725.991523，这种时间格式太不人性化
            nice_show_time = datetime.fromtimestamp(modify_time) # 转化为人性化的时间显示格式：2020-02-08 20:25:25.991523
            print('文件 %s 最后一次修改时间：%s' % (file, nice_show_time))
get_modify_time('.')