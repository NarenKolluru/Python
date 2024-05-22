s=input()
for i in range(len(s)):
    if s[i].isnumeric():
        print(s[i-1]*int(s[i]),end='')
