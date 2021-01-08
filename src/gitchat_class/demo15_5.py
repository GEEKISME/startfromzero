from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
sns.set(style="ticks")

df = sns.load_dataset("iris")
df02 = df.iloc[:,[0,2,4]] # 选择一对特征
print(df02)
sns.pairplot(df02, hue="species")
plt.show()
# ===================================
print('=======================================')
clf = tree.DecisionTreeClassifier()
train_index = [i for i in range(150) if i<30 or 50<=i<80 or 100<=i<130]
test_index = [i for i in range(150) if 30<=i<50 or 80<=i<100 or 130<=i<150]
train_data, train_target = df02.iloc[train_index,[0,1]],df02.iloc[train_index,2]
test_data, test_target = df02.iloc[test_index,[0,1]],df02.iloc[test_index,2]
clf = clf.fit(train_data, train_target)
print(clf)
# 结果
test_val = clf.predict(test_data)
print(test_val)
right = [i for i, j in zip(test_val,test_target) if i==j]
percent = len(right) / len(test_target)
print(percent)  # 0.95
