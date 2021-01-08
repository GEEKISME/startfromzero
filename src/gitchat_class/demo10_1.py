import zipfile
import os
import time

def batch_zip(start_dir):
    start_dir = start_dir
    file_news = start_dir+'.zip'
    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED)
    for dir_path,dir_names,file_names in os.walk(start_dir):
        f_path = dir_path.replace(start_dir,'')
        f_path = f_path and f_path + os.sep #实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            z.write(os.path.join(dir_path,filename),f_path+filename)
    z.close()
    return file_news
batch_zip('E:\pycharm_workspace\startfromzero\src\webdev')
print('==================================')
import hashlib
def hash_cry32(s):
    m = hashlib.md5()
    m.update((str(s).encode('utf-8')))
    return m.hexdigest()
print(hash_cry32(1))
print(hash_cry32('hello'))