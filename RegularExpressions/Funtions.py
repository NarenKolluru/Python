import re
s="How are you.How is everything"
matches=re.search("How",s)
print(matches.span())
print(matches.group())
print(matches.string)
print(re.split('.',s))
print(re.sub('How','Hello',s))
