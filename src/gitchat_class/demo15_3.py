import numpy as np
import matplotlib.pyplot as plt
def setup_axes():
    fig,axes = plt.subplots(ncols=3,figsize = (6.5,3))
    for ax in fig.axes:
        ax.set(xticks=[],yticks=[])
    fig.subplots_adjust(wspace=0,left=0,right=0.93)
    return fig,axes
x = np.linspace(0,10,100)
fig, axes = setup_axes()
for ax in axes:
    ax.margins(y=0.10)
for i in range(1, 6):
    axes[0].plot(x, i * x)
for i, ls in enumerate(['-', '--', ':', '-.']):
    axes[1].plot(x, np.cos(x) + i, linestyle=ls)
for i, (ls, mk) in enumerate(zip(['', '-', ':'], ['o', '^', 's'])):
    axes[2].plot(x, np.cos(x) + i * x, linestyle=ls, marker=mk, markevery=10)