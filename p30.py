s = input()
lis = []
for i in s :
    if i.upper() not in ["A","E","I","O","U","Y"]:
        lis.append(i.lower())
for i in lis :
    print("."+i,end = "")

