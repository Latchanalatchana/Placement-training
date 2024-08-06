a=input("Enter a sentence : ")
l=a.split()
m=""
for i in l:
    if len(i)>len(m):
        m=i
print("The biggest word is",m)
