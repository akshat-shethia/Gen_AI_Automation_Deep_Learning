import re
f = open(r"Section 6\Web_Addresses\web.txt")
string = f.read()
result = re.findall(r".+\s+(http.*://.+\.\w{2,})\s.+Online shopping.+", string)
print(result)
# ['https://tmall.com', 'https://login.tmall.com',
#  'https://taobao.com', 'https://pages.tmall.com']
