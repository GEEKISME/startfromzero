p = (1,2)
print(p)
from collections import namedtuple


# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以
# 用属性而不是索引来引用tuple的某个元素。 这样一来，我们用namedtuple可以很方便地定义一种数据
# 类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
Point = namedtuple('Point',['x','y'])
p1 = Point(1,2)
print(p1)
print(p1.x)
print(p1.y)
# 可以验证创建的Point对象是tuple的一种子类：
temp = isinstance(p1,Point)
print(temp)
print(isinstance(p1,tuple))
# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义： namedtuple('名称', [属性list]):
Circle = namedtuple('Circle',['x','y','z'])
print('==================================================')
# deque 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是
# 线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
# 这样就可以非常高效地往头部添加或删除元素。
print(q)
print('=================================================')
# defaultdict 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key
# 不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda :'N/A')
dd['key1']= 'abx'
print(dd['key1'])
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
print(dd['key2'])
print('======================================')
# OrderedDict   使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d  = dict([('a',1),('b',2),('c',3),('d',4),('e',5),('f',6)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3),('d',4),('e',5),('f',6)])
print(od)
odd = OrderedDict()
odd['z'] = 1
odd['y'] = 2
odd['x'] = 3
print(list(odd.keys()))
print('==================================')
# ======================================
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
from collections import OrderedDict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >=self._capacity:
            last = self.popitem(last=False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self,key,value)


print('==============================')
from collections import ChainMap
import  os,argparse
# 构造缺省参数:
defaults = {
    'color':'red',
    'user':'guest'
}
# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k:v for k,v in vars(namespace).items() if v}
# 组合成ChainMap:
combined = ChainMap(command_line_args,os.environ,defaults)
# 打印参数:
print('color=%s' %combined['color'])
print('user=%s' %combined['user'])
print('=========================================')
#Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1
print(c)