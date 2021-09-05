while True:
    string = input("Enter any String: ")
    if string == 'x':
        print("You have chosen death")
        break
# the if and else line should be in the same line and follow indentation
    else:
        newstr = string
    vowels = ('a','e','i','o','u')
    for x in string.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")
    print("New string after removing all vowels: ")
    print(newstr,"\n")