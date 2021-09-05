while True:
    string = input("Enter any string: ")
    if string == 'x':
        print("so you have chosen death")
        break
    else:
        reverseString = string[::-1]
        print("Reverse String =",reverseString,"\n")