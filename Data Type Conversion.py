a = int("123")
print(a)
print(type(a))  # Converted from string to integer,works with string

a = float(100)
print(a)
print(type(a))

a = chr(100)
print(a)
print(type(a))

a = ord("1")
print(a)
print(type(a))

a = hex(100)
print(a)
print(type(a))

a = oct(100)
print(a)
print(type(a))

a = complex(100)
print(a)
print(type(a))

a = str(100)
print(a)
print(type(a))

a = repr(100)
print(a)
print(type(a))

a = eval("100")
print(a)
print(type(a))

tuple = (100,200)
print(tuple)
print(type(tuple))

list=[100,200]
print(list)
print(type(list))

set = {"apple", "banana", "cherry"}
print(set)
print(type(set))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])
print(type(thisdict))
