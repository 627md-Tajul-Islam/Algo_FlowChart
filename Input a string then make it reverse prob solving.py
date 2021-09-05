while True:
    string = input("Enter any string: ")
    if string == 'x':
        break
    else:
        reverseString = string[::-1]
        print("Reverse String =",reverseString,"\n")