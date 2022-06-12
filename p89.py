s = input()
lis = s.split()
lis[0] = lis[0].title()
for i in range(1,len(lis)):
    lis[i] = lis[i].lower()
print(" ".join(lis))
