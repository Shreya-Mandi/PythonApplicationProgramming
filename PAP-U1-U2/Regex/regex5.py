# \d: Matches any digit (0-9).
# \D: Matches any non-digit.
# \w: Matches any word character (alphanumeric + underscore).
# \W: Matches any non-word character.
# \s: Matches any whitespace character.
# \S: Matches any non-whitespace character.

import re

pattern=re.compile(r'\d+\s\w+')
res=pattern.findall('42 apples, 7 oranges')

print(res)