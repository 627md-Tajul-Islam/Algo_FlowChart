StudentMarks  = int(input("Enter a number: "))

if StudentMarks >= 90:
    print('Student scored grade A ')
else:
    if StudentMarks >= 80:
        print('Student scored grade B ')
    else:
        if StudentMarks >= 70:
            print('Student scored grade C ')
        else:
            if StudentMarks >= 60:
                print('Student scored grade D ')
            else:
                if StudentMarks >= 50:
                    print('Student scored grade Passed ')
                else:
                    if StudentMarks >= 40:
                        print('Student scored grade Failed ')