a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a > b) and (a > c):
    print("a is the largest")
elif (b > a) and (b > c):
    print("b is the largest")
else:
    print("c is the largest")
