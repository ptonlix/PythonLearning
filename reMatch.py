import re

s = r'ABC\\-001'

result = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(result)
result = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(result)