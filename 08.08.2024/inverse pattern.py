n = int(input("Enter a number :"))
print(n)
k =int(input("Enter a number :"))
print(k)
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
