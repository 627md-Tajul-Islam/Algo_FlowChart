# All built in functions
"""
len join replace strip split capitalize upper lower casefold count find
"""
a = "Tajul Islam"
b = len(a)
print(b) # gives you the length

""" 
a = mohammad
b = Tajul
c = Islam
print(",".join(["mohammad","b","c"]))
"""  # code not allowed

x = "How are you"
y = x.split()
print(y) #  split method

x = "hello tajul, how are you"
words = x.split()
for x in words:
    print(x) # split by word

 #1
x = "Welcome to america"
print(x)
y = x.replace("america","Afghanistan")
print(y) # its replaced

#2
x = "Tajul"
print(x)
y = x.replace("a","i")
print(y)


x = "Welcome to Jashore polytechnic institute"
print(x)
y = x.strip('W')
print(y) # strip method. used to remove 1st and last charectar

y = "welcome"
z = y.capitalize()
print(z) # capitalize method.

x = "welcome"
print(x)
y = x.upper()
print(y) # upper method

x = "WELCOME"
print(x)
y = x.lower()
print(y) # lower method

x = "Welcome"
y = x.swapcase()
print(y) # swapcase method
