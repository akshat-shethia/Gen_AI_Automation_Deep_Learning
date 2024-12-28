import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February. 1234 0123 0012"


s = r"[1-9][0-9]{3}"
t = re.compile(s)

result = re.findall(t, string)
print(result)