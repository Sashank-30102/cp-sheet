n = input()
s = ""
for i in n :
    if n.index(i) == 0 and int(i) == 9:
        s = s + i
        continue
    if int(i) > 4 :
        s = s + str(9-int(i))
    else :
        s = s + i
print(s)

