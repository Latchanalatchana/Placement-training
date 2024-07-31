u = int(input())
for i in range(n):
    v=input().split()
    w=input().split()
    try:
        print(int(v)//int(w))
    except Exception as e:
        print(f"Error Code: {e}")
