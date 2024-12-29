import re

f = open(r"Section 6\Date_And_Time\logs.txt")

string = f.read()

# result = re.findall(r".+/2020 (?:12|[1-3]):\d\d:\d\d PM (.+?) \d+", string)

# Write a pattern on line 7, in between the double quotes, that will match the Source substring of all the log entries that were generated after 12 PM and before 4 PM, regardless of the severity level and the date.
result = re.findall(
    r".+/2020 (?:12|[1-3]):[0-9]{2}:[0-9]{2} PM (.+) [0-9]{2}", string)

print(result)
