import re
f = open(r"Section 6\Stocks\stocks.txt")
string = f.read()

result = re.findall(
    r"(.+?)\s+[0-9]+\.[0-9]+M\s+[1-4][0-9]\.[0-9]+B\s+[0-9]+\.[0-9]+", string)
print(result)
# ['3M', 'Coca-Cola', 'McDonalds', 'Merck&Co', 'Nike', 'Tesla', 'Visa A']


# Write a pattern on line 7, in between the double quotes, that will match the company names whose revenue is between 10B and 30B and P/E ratio is between 10 and 15.
result = re.findall(r"(.+?)\s+[0-9]+\.[0-9]+M\s+[1-2][0-9]\.[0-9]+B\s+1[0-4]\.[0-9]+", string)
print(result)
