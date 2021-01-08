import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='whitegrid')
rs = np.random.RandomState(1)
x = rs.normal(2,0.1,50)
y = 2+1.6*x+rs.normal(0,0.1,50)
 
sns.residplot(x,y,lowess=True,color='orange')
plt.show()


