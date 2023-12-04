# [ ]: Matches any single character inside the brackets.
# ^ (within [ ]): Negates the character class (matches any character not inside the brackets).

import re

pattern= re.compile(r'[aeiou]')
result=pattern.findall('hello')

print(result)