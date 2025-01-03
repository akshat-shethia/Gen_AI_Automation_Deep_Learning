string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

import re

result = re.match(r"[a-zA-Z1-9][a-zA-Z0-9]{2}", string) # Starts matching from the index 0 , so if i use r"[a-zA-Z1-9][a-zA-Z0-9]{3}, ill get None

print(result)
# <re.Match object; span=(0, 3), match='The'>