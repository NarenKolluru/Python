import re
p=re.compile('[aeiou]')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)


import re
p=re.compile('[a-f]')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

import re
p=re.compile('[^a-f]')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)
