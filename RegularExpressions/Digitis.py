import re
p=re.compile('\d+')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

p=re.compile('\D')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)


p=re.compile('[0-8][0-8]')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)
