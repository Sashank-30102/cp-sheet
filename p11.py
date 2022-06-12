s = input()
l = input()
n = int(input())
lis = []
num = 97
count = 0
sublist = []
for i in l:
    if i == "1":
        lis.append(num)
    num += 1
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        bad_count = 0
        for k in s[i:j]:
            if ord(k) not in lis :
                bad_count += 1
        if bad_count <= n :
            count += 1
            sublist.append(s[i:j])
print(len(set(sublist)))

