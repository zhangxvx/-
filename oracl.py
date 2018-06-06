import cx_Oracle

import os
# 数据库的字符集  如果查询中包含中文必须加这一行代码
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.ZHS16GBK"

conn = cx_Oracle.connect('WEIXIN', 'hadoop316', '192.168.50.53:1521/ORCL')
print('连接成功!')
cursor = conn.cursor()

item = "账单查询"
sql = "SELECT Count(WEIXIN.JIAOFEI.ORDER_TYPE) FROM WEIXIN.JIAOFEI WHERE WEIXIN.JIAOFEI.ORDER_TYPE = '%s'" % item
cursor.execute(sql)

alldata = cursor.fetchall()
for k in alldata:
    print(k)

cursor.close()
conn.close()
