num1 = int(input("Enter first number: "))
num1 = int(input("Enter second number: "))
num1 = int(input("Enter third number: "))


if num1 < num2 and num1 < num3:
    small = num1
if num2 < num1 and num2 < num1:
    small = num2
else:
    small = num3
print("Small number is :",small)