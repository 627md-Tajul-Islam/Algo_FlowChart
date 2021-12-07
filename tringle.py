import math

a = int(input("Enter 1st hand: "))
b = int(input("Enter 2nd hand: "))
c = int(input("Enter 3rd hand: "))

if (a+b)>c and (b+c)>a and (c+a)>b:
    S = a+b+c /2
    Area = math.sqrt(S*(S-a)*(S-c)*(S-c))
    print(Area)
else:
    print("Triangle not possible")