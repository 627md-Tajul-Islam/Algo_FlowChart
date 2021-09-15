a = int("123")
print(a)



print(type(a))  # Converted from string to integer,works with string

a = float(100)
print(a)
print(type(a)) # Converted from integer to float

a = chr(100)
print(a)
print(type(a)) # Converted from integer to charectar

a = ord("1")
print(a)
print(type(a)) # Converted only 1 charecter to integer

a = hex(100)
print(a)
print(type(a)) # Converted from integer to hexadecimal

a = oct(100)
print(a)
print(type(a)) # Converted from integer to octal

a = complex(100)
print(a)
print(type(a)) # Converted from integer to complex

a = str(100)
print(a)
print(type(a)) # Converted from integer to string

a = repr(100)
print(a)
print(type(a)) # Converted from integer to expression string

a = eval("100")
print(a)
print(type(a)) # Converted from integer to hexadecimal

tuple = (100,200)
print(tuple)
print(type(tuple)) # Converted from integer to tuple

list=[100,200]
print(list)
print(type(list)) # Converted from integer to list

set = {"apple", "banana", "cherry"}
print(set)
print(type(set)) # Converted from string to set

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(type(thisdict)) # Converted from string to directory
