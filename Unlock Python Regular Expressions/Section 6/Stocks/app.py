import re
f = open(r"Section 6\Stocks\stocks.txt")
string = f.read()

result = re.findall(
    r"(.+?)\s+[0-9]+\.[0-9]+M\s+[1-4][0-9]\.[0-9]+B\s+[0-9]+\.[0-9]+", string)
print(result)
# ['3M', 'Coca-Cola', 'McDonalds', 'Merck&Co', 'Nike', 'Tesla', 'Visa A']
