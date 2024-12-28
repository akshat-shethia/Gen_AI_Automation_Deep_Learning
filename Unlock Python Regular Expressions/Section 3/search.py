string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."


import re

result = re.search(r"[1-9][0-9]{2}", string) # Only matches and returns the first occurance of the word

print(result)
# <re.Match object; span=(15, 18), match='600'>