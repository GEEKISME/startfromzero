from multiprocessing import Process
import os
# def run_proc(name):
#     print('Run child process %s(%s)...' %(name,os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s' % os.getpid())
#     创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，
#     这样创建进程比fork()还要简单。target = run_proc 代表的就是这个子进程将要执行的方法，args
#     是一个tuple，里面是run_proc方法需要的参数
#     p = Process(target=run_proc,args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child process end')
#========================================
# from multiprocessing import Pool
# import os,random,time
# def long_time_task(name):
#     print('run task %s(%s)...' %(name,os.getpid()))
#     # 进程运行的开始时间
#     start = time.time()
#     time.sleep(random.random()*3)
#     # 进程结束时间
#     end = time.time()
#     print('Task %s runs %0.2f seconds' %(name,(end-start)))
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     # 一个拥有四个进程的进程吃
#     p = Pool(4)
#     for i in range(5):
#         # 每调用一次就在进程池出现一个进程，
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
# =================================================
import subprocess
print('$nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)