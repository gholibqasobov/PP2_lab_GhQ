import re

txt = input()

result = re.split('(?=[A-Z])', txt)
# result = re.split('[A-Z]', txt)
print(result)

