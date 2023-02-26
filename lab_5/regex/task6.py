import re

txt = input()

result = re.sub('[ ,.]', ':', txt)

print(result)
