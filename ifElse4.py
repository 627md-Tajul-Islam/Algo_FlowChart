import math 

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a+b) > c and (b+c) > a and (c+a) >b:
    s = (a+b+c)/2
    Area = cmath.sqrt(s*(s-a)*(s-b)*(s-c))
    print(Area)
else:
    print("Triangle not possible")