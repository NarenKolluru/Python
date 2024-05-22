import re
e='ababbaabbb'
p=re.compile('ab*')
ans=p.findall(e)
print(ans)

p=re.compile('ab?')
ans=p.findall(e)
print(ans)

p=re.compile('ab+')
ans=p.findall(e)
print(ans)
