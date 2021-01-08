# 首先安装mysql-connector 包
# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:我们就直接连我们mysql中已有的testdb数据库，这个数据库中
# 已经有两张表user和users了
conn = mysql.connector.connect(user='root',password='chaojie132129',database='testdb')
cursor = conn.cursor()
# 我们创建一张pyuser表:
cursor.execute('create table pyuser (id varchar (20) primary key ,name varchar (20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into pyuser (id,name ) values (%s,%s)',['1','Michael'])
s = cursor.rowcount
print(s)
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from pyuser where id = %s',('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close
