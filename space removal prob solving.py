while True:
    print("Enter 'x' for exit.")
    string = input("Entre Any String: ")
    if string =='x':
        break
        print("So you have choosen death")
    else:
        new_string = string.replace(" ","")
        print("\nNew string after removing all spaces: ")
        print(new_string, "\n")