st = [int(i) for i in input().split(":")]
et = [int(i) for i in input().split(":")]
stmins = st[0]*60 + st[1]
etmins = et[0]*60 + et[1]
mins = etmins - stmins
mins = mins//2
h = st[0]
h = h + mins//60
m = st[1]
m = m + mins%60
if len(str(h)) <= 1 :
    h = str(h)
    h = "0"+h
if len(str(m)) <= 1 :
    m = str(m)
    m = "0"+m
print(str(h)+":"+str(m))
