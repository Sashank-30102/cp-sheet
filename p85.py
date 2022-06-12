l = [int(i) for i in input().split()]
a1 = l[0]
k = l[1]
def recfun(k):
    if k == 1:
        return a1
    l = list(str(recfun(k-1)))
    l = [int(i) for i in l]
    min_digit = min(l)
    max_digit = max(l)
    l = [str(i) for i in l]
    num = int("".join(l))
    return num + min_digit*max_digit
print(recfun(k))   
        
