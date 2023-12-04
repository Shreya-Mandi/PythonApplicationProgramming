import re
pattern=re.compile(r"hello", re.IGNORECASE)

res=re.fullmatch(pattern,"heLLO")
# res=re.match(pattern,"heLLO")
# res=re.search(pattern,"heLLO")

print(res.group())
