import re

f = open(r"Section 6\PhoneBook\phone.txt")

string = f.read()

# Write a pattern on line 7, in between the double quotes, that will match all the persons (first name only) in the file whose last name ends in a vowel (aeiou) and phone number ends in either 0, 7 or 9.
result = re.findall(r"([a-zA-Z]+)\s.+[aeiou]\t.+\s.{7}[079]", string)

print(result)
