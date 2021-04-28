import json

# 使用三引号将浏览器复制出来的requests headers参数赋值给一个变量
headers = """
m: LiveList
do: getLiveListByPage
gameId: 100022
tagAll: 0
callback: getLiveListJsonpCallback
page: 2
"""

# 去除参数头尾的空格并按换行符分割
headers = headers.strip().split('\n')

# 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}

# 使用json模块将字典转化成json格式打印出来
print(json.dumps(headers, indent=2))
