s = float(input("Enter Score: "))
if 0.0>s>1.0:
    print("Error: Score is out of range")
elif s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
elif s<0.6:
    print("F")
