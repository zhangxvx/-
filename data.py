import json

filepath1="D:\Workspaces\ShenNeng\微客服\jiaofei order_type.json"
filepath2="D:\Workspaces\ShenNeng\微客服\yewubanli order_type.json"

with open(filepath1,'r',encoding='utf-8') as f1:
    ls=list()
    data = json.load(f1)
    jfcount=data['RECORDS']
    for k in jfcount:
        name=k['ORDER_TYPE']
        count=k['ctype']
        ls.append({name:count})
    f1.close()
print(ls)

with open('jfdata.json', 'w') as f:
    json.dump(ls, f)


