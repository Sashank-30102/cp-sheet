s = input()
stack = []
maxlen = 0
count = 0
n = 0
for i in s:
    if i == ")" and len(stack) > 0:
        if stack[-1] == "(":
            stack.pop()
            count += 2
            if count == maxlen:
                n += 1
            if count > maxlen:
                maxlen = count
                n = 1
    elif i == "(":
        stack.append("(")
    if (len(stack) == 0):
        count = 0
print(maxlen,end = " ")
if n == 0:
    n = 1
print(n)
