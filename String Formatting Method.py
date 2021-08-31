#1
a = 10
b = 20
print('Value of a = {}, value of b = {}' .format(a,b)) # using multiple variable
#2
a = 10
b = 50
s = "Value of a = {}, value of b = {}"
print(s.format(a,b)) #  format using a var, storing string into
#3
name = "Tajul"
print('Hi, My name is {}|' .format(name)) #formatting variable using string format
#4
list = [1,2,3,4,5]
print("The List is:{}".format(list)) # formatting list
#5
msg = "My score on C: {0}, Python: {1},Java: {2}".format(6,6.5,5)
print(msg) # using placeholders to using string
#6
a = '{2},{1},{0}'.format('a','b','c')
print(a)