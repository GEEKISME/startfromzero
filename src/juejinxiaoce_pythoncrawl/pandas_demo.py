
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
display_columns = ["title","read_num","like_num","comment_num","reward_num","p_date"]
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


df = pd.read_csv('post.csv')
df = df.reindex(columns=display_columns)
df.p_date = pd.to_datetime(df['p_date'])
print(df.describe())
top_read_num_10 = df.sort_values(by=['read_num'],ascending=False)[:10]
top_read_num_10 = top_read_num_10[display_columns]
top_read_num_10.reset_index(drop=True)
print(top_read_num_10)

ax = df.plot(y='read_num',x = 'p_date',title = '文章阅读量趋势',figsize = (9,6))
ax.set_ylabel('阅读量')
ax.set_xlabel('')
ax.legend().set_visible(False)
plt.show()

