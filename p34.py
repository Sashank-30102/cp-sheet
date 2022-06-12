n = int(input())
commands = []
directory = []
for i in range(n):
    commands.append(input())
for i in commands :
    if i == "pwd":
        for j in directory :
            print("/"+j,end = "")
        print("/")
    elif i[:2] == "cd":
        lis = i[3:].split("/")
        if "" in lis :
            lis.remove("")
        for i in lis :
            if i == "..":
                directory.pop()
            else :
                directory.append(i)
    
