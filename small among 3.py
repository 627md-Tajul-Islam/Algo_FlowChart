a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a < b and a < c:
    print("A is smallest")
elif b < a and b < c:
    print("B is smallest")
else:
    print("C is smallest")