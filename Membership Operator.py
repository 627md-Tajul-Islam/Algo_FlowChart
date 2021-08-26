# in & not in
# if  a character is in a specific string it will return true
# if  a character is not in a specific string it will return false


# we can use [in] keyword to check if the string is whether the string is a part of the group.
#1
a = "j"
b = "tajul"
c = a in b
print(c)
# it will return true cause [j] is in the {tajul} word

#2
a = "T"
b = "tajul"
c = a in b
print(c) # it will return false cause [T] is not in {tajul}

# we can use [not in] keyword to check if the string is whether the string is not a part of the group.
#3
a = "T"
b = "tajul"
c = a not in b
print(c) # it will return true cause [T] is not in {tajul}

a = "t"
b = "tajul"
c = a not in b
print(c) # it will return false cause [t] is in {tajul}