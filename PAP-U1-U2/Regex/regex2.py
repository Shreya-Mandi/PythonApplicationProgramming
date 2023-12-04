# .: Matches any character except a newline.
# ^: Matches the start of a string.
# $: Matches the end of a string.

import re

pattern =re.compile(r'^hello')
res=pattern.match("hello world")

print(res.group())