# *: Matches 0 or more occurrences of the preceding pattern.
# +: Matches 1 or more occurrences of the preceding pattern.
# ?: Matches 0 or 1 occurrence of the preceding pattern.
# {m}: Matches exactly m occurrences of the preceding pattern.
# {m, n}: Matches between m and n occurrences of the preceding pattern

import re

pattern=re.compile(r'abc{2,4}?')

res=pattern.findall('abcabcccc abs abcc abc cc')
print(res)