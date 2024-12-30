import re
f = open(r"Section 6\Web_Addresses\web.txt")
string = f.read()
result = re.findall(r".+\s+(http.*://.+\.\w{2,})\s.+Online shopping.+", string)
print(result)
# ['https://tmall.com', 'https://login.tmall.com',
#  'https://taobao.com', 'https://pages.tmall.com']


# Write a pattern on line 7, in between the double quotes, that will match the Site name (e.g. Google, Facebook etc.) of all the websites in the file that are based in China and have a 3-letter URL extension (e.g. .com, .org etc.).
result = re.findall(r"(.+)\sh.+\.[a-zA-Z]{3}\s.+(?:China|china)", string)
print(result)

result = re.findall(r"(.+)\s+http.*://.+\.\w{3}\s.+China.+", string)
print(result)