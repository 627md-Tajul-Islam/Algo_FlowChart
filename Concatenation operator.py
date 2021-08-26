#1
a = "Hello"
b = "World"
add = a + b
print(add)  # adding plain string
#2
a = "Hello"
b = "World"
add = a + "&" + b
print(add)  # adding another text string
#3
a = "Hello"
b = "World"
add = a + " " + "&" + " " + b
print(add)  # adding space
#4
a = "2"
b = "2"
add = a + b
print(add) # it will return 22 instead of 4 cause its a string
#5
""" 
a = 1
b = "2"
c = 3
d = "4"
add = a + b + c + d
print(add)
"""
# this will through an error cause its mixed with string with number

#6
a = str(1)
b = "2"
c = str(3)
d = "4"
add = a + b + c + d
print(add)   # it will retun output cause the numbers are converted

#7
a = 'Welcome '
b = 'to'
c = ' Bangladesh'
add = a + b + c
print(add) # another way to add space.
#8
a = "Tajul " * 5
print(a) # repetition