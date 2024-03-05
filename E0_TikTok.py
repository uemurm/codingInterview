import re

string = "10#11#12"
# s1 = "1326#"

print(re.findall(r'\d\d#', string))
