import random,time,queue
from multiprocessing.managers import BaseManager


# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


def re_task_queue():
    global task_queue
    return task_queue


def re_result_queue():
    global result_queue
    return result_queue


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable= re_task_queue)
    QueueManager.register('get_result_queue', callable= re_result_queue)
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动queue
    manager.start()
    # 获得通过网络访问的queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('put task %d...' % n)
        task.put(n)
    print('try get result...')
    for i in range(10):
        r = result.get(timeout=10)
        print('result:%s' % r)
    manager.shutdown()
    print('master exit.')