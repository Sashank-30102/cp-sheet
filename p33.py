s = input()
stack = []
for i in s:
    if len(stack) == 0:
        stack.append(i)
    elif i == stack[-1]:
        stack.pop()
    elif i != stack[-1]:
        stack.append(i)

if len(stack) == 0:
    print("Yes")
else :
    print("No")


