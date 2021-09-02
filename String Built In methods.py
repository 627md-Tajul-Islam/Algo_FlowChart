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