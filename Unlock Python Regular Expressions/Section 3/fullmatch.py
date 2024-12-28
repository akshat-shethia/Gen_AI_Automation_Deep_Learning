string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

import re

print(len(string)) # 285
result = re.fullmatch(r".{285}", string)

print(result)
# <re.Match object; span=(0, 285), match='The Euro STOXX 600 index, which tracks all stock >