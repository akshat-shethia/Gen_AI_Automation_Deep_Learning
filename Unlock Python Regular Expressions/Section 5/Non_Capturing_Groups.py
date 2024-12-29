import re
string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

result = re.search(r".+(\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
print(result.groups())
# ('index', 'FTSE', '19 February')

print(result.group(1))
# 'index'

print(result.group(2))
# 'FTSE'

print(result.group(3))
# '19 February'

result = re.search(r".+(?:\b.+ex\b).+(\b[A-Z]{4}\b).+(\d\d\s.+)\.", string)
# '?:' at the start of the () indicates that it's a non capturing group
print(result.groups())
# ('FTSE', '19 February')

print(result.group(1))
# 'FTSE'

print(result.group(2))
# '19 February'

print(result.group(3))
# Traceback (most recent call last):
#   File "c:\miniconda\Gen_AI_Automation_Deep_Learning\Unlock Python Regular Expressions\Section 5\Non_Capturing_Groups.py", line 27, in <module>
#     print(result.group(3))
#           ^^^^^^^^^^^^^^^
# IndexError: no such group
