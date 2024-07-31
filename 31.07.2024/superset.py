u= set(map(int,input().strip().split()))
v = int(input())
s= []
for i in range(v):
    w = set(map(int,input().strip().split()))
    if (u.issuperset(w)) and (u!= w):
        s.append(True)
    else:
        s.append(False)
if (len(set(s))==1) and (s[0]==True):
    print (True)
else:
    print (False)
