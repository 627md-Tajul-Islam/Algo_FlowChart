while True:
    string = input("Enter any String: ")
    if string == 'x':
        print("You have chosen death")
    break

else:
    Newstring = string
    vowels = ('a','e','i','o','u')
    for x in string.lower():
        if x in vowels:
