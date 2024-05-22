import re
p=re.compile('\s')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)

import re
p=re.compile('\S')
ans=p.findall("abc1 123 def 45 56 67")
print(ans)
