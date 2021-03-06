from scipy.stats import binom,uniform
import  numpy as np
import matplotlib.pyplot as plt
from functools import wraps


def my_plot(label0 = None,label1=None,ylabel = 'probability density function',fn = None):
       def decorate(f):
          @wraps(f)
          def myplot():
             fig = plt.figure(figsize=(16,9))
             ax = fig.add_subplot(111)
             x,y,y1 = f()
             ax.plot(x,y,linewidth=2,c='r',label=label0)
             ax.plot(x,y1,linewidth=2,c='b',label=label1)
             ax.legend()
             plt.ylabel(ylabel)
             plt.savefig('./img/%s' %(fn,))
             plt.close()
          return myplot
       return decorate

@my_plot(label0='b-a=1.0',label1='b-a=2.0',fn='uniform.png')
def unif():
    x = np.arange(-0.01,2.01,0.01)
    y = uniform.pdf(x,loc = 0.0,scale = 1.0)
    y1 = uniform.pdf(x,loc=0.0,scale=2.0)
    return x,y,y1

unif()

@my_plot(label0='n=50,p=0.3',label1='n=50,0=0.7',fn='binom.png',ylabel='probability mass function')
def bino():
    x = np.arange(50)
    n,p,p1 = 50,0.3,0.7
    y = binom.pmf(x,n=n,p=p)
    y1 = binom.pmf(x,n=n,p=p1)
    return x,y,y1
bino()