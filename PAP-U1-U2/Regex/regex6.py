import re

pattern=re.compile(r'\d+')

res=pattern.finditer('42 apples, 7 oranges')
res2=pattern.sub('xx','42 apples, 7 oranges')

for i in res:
    print(i.group())

print(res2)