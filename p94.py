n = int(input())
s = list(input())

for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        if ord(s[i]) > ord(s[len(s)-i-1]):
            s[i] = chr(ord(s[i])-1)
        elif ord(s[i]) < ord(s[len(s)-i-1]):
            s[i] = chr(ord(s[i])+1)
    else :
        if s[i] != "z":
            s[i] = chr(ord(s[i])+1)
        else :
            s[i] = chr(ord(s[i])-1)
         
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        if ord(s[i]) > ord(s[len(s)-i-1]):
            s[len(s)-i-1] = chr(ord(s[len(s)-i-1])+1)
        elif ord(s[i]) < ord(s[len(s)-i-1]):
            s[len(s)-i-1] = chr(ord(s[len(s)-i-1])-1)
    else :
        if s[i] != "z":
            s[i] = chr(ord(s[len(s)-i-1])+1)
        else :
            s[i] = chr(ord(s[len(s)-i-1])-1)
            
s = "".join(s)
print(s)
if s == s[::-1]:
    print("YES")
else :
    print("NO")
                
