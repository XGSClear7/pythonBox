import json

# 使用三引号将浏览器复制出来的requests headers参数赋值给一个变量
headers = """
Host: zhan.qq.com
Proxy-Connection: keep-alive
Content-Length: 799432
Pragma: no-cache
Cache-Control: no-cache
Origin: https://www.colorgg.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryuptjZg9xmsfWzngP
Accept: */*
Referer: https://www.colorgg.com
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: pgv_pvi=4342937600; RK=xFr4lrf07R; ptcz=a247c6170fb56cb4d5d41bf8461f11097a9be27bc7e7dc8b921254de9b1c924b;
"""

# 去除参数头尾的空格并按换行符分割
headers = headers.strip().split('\n')

# 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}

# 使用json模块将字典转化成json格式打印出来
print(json.dumps(headers, indent=2))
