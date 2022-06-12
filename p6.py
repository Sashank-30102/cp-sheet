n = int(input())
for i in range(n):
    num = input()
    numint = int(num)
    lis = []
    div = 10
    for i in range(len(num)+1):
        x = 10**i
        lis.append(numint%x)
        numint = numint - (numint%x)
    lis.remove(0)
    l = [i for i in lis if i != 0]
    print(len(l))
    print(l)


