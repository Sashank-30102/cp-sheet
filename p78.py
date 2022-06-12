n = int(input())
lis = [int(i) for i in input().split()]
energy = 0
amount = 0
h = 0
for i in range(len(lis)-1):
    if energy > lis[i]-h and h < lis[i]:
        h = lis[i]
        energy -= lis[i]-h
    elif energy < lis[i]-h and h < lis[i]:
        amount += lis[i]-h-energy
        energy = 0
        h = lis[i]
    elif h > lis[i]:
        energy += h-lis[i]
        h = lis[i]
print(amount)
    
        
