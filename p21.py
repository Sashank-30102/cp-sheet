s = input()
l = [int(i) for i in s.split("+")]
l.sort()
for i in l[:-1]:
    print(str(i)+"+",end = "")
print(str(l[-1]))
    
