import re
p=re.compile('\w')
ans=p.findall("abc1 234 def 47 56 69")
print(ans)

import re
p=re.compile('\W')
ans=p.findall("abc1 234 def 47 56 69")
print(ans)
