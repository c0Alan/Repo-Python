import json

""" 写数据 """
def _demo01():
    data1 = json.dumps([])         # 列表
    print(data1, type(data1))
    data2 = json.dumps(2)          # 数字
    print(data2, type(data2))
    data3 = json.dumps('3')        # 字符串
    print(data3, type(data3))
    dict = {"name": "Tom", "age": 23}   # 字典
    data4 = json.dumps(dict)
    print(data4, type(data4))


""" 写文件 """
def _demo02():
    dict = {"name": "Tom", "age": 23}  
    filename = "files/test.json"
    with open(filename, "w", encoding='utf-8') as f:
        # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
        # f.write(json.dumps(dict, indent=4))
        json.dump(dict, f, indent=4)  # 传入文件描述符，和dumps一样的结果


""" 读数据 """
def _demo03():
    dict = '{"name": "Tom", "age": 23}'   # 将字符串还原为dict
    data1 = json.loads(dict)
    print(data1, type(data1))

""" 读文件 """
def _demo04():
    filename = "files/test.json"
    with open(filename, "r", encoding='utf-8') as f:
        data2 = json.loads(f.read())    # load的传入参数为字符串类型
        print(data2, type(data2))
        f.seek(0)                       # 将文件游标移动到文件开头位置
        data3 = json.load(f)
        print(data3, type(data3))

_demo04()