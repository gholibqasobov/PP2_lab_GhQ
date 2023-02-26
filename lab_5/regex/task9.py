import re
from re import sub

txt = input()

result = re.findall('[a-zA-Z][a-z]+', txt)

print(' '.join(result))