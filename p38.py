n = int(input())
s = input()
dic = {}
for i in s :
    if i not in dic :
        dic[i] = 1
    else :
        dic[i] += 1
keys = list(dic.keys())
flag = 0
for i in range(1,len(keys)):
    if dic[keys[i]] != dic[keys[i-1]] and dic[keys[i]] != n:
        print(-1)
        flag = 1
        break
st = ""
if flag == 0:
    while dic[keys[0]] > 0:
        for i in dic:
            st = st + i
            dic[i] -= 1
    print(st)
