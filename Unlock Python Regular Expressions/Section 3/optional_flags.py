import re
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."


result = re.findall(r"the", string)
print(result)
result = re.findall(r"the", string, re.I)
# re.I -> Ignore Case Flag, Considers `uppercase` and `lowercase`
print(result)


string2 = "Hello\nPython"
result = re.search(r".+", string2)
print(result)
# <re.Match object; span=(0, 5), match='Hello'>

result = re.search(r".+", string2, re.S)  # Includes New Line Characters
print(result)
# <re.Match object; span=(0, 12), match='Hello\nPython'>


result = re.search(r""".+\s #Beginning of the string
			(.+ex) #Searching for index
			.+ #Middle of the string
			(\d\d\s.+). #Date at the end""", string, re.X)
print(result.groups())
