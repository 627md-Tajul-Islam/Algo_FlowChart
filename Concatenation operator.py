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

""" 
a = "2"
b = "2"
add = a + b
print(add) # it will return 22 instead of 4 cause its a string

a = 1
b = "2"
c = 3
d = "4"
add = a + b + c + d
print(add)
"""
# this will through an error cause its mixed with string with number