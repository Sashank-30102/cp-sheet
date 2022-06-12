s = input()
h = input()
lis_1 = list(s)
lis_2 = list(h)
flag = 0
if len(h) > len(s):
    for i in range(0,len(h)-len(s)+1):
        if sorted(lis_2[i:i+len(s)]) == sorted(lis_1):
            print("YES")
            flag = 1
            break
    if flag == 0:
        print("NO")
elif len(h) == len(s):
    if sorted(lis_2) == sorted(lis_1):
        print("YES")
    else :
        print("NO")
else :
    print("NO")

