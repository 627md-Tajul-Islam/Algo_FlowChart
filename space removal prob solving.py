while True:
    print("Enter 'x' for exit.")
    string = input("Entre Any String: ")
    if string =='x':
        print("So you have choosen death")
        break


    else:
        new_string = string.replace(" ","")
        print("\nNew string after removing all spaces: ")
        print(new_string, "\n")