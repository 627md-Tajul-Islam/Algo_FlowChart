import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a+b) > c and (b+c) >a and (c+a) > b:
    S = (a+b+c)/2
    Area = math.sqrt(S*(S-a)*(S-b)*(S-c))
    print(Area)                 
else:
    print("Triangle not possible")