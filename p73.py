s1 = input()
s2 = input()
n1 = s1
n2 = s2
while len(s1) != len(s2):
    if min(len(s1),len(s2)) == len(s1):
        s1 = s1 + n1
    else :
        s2 = s2 + n2
if s1 != s2:
    print(-1)
else:
    print(s1)
