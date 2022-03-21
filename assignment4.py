whole_prog_again = True
while whole_prog_again == True:
    whichCalc = int(input("Do you want to convert a decimal number to binary or perform standard operations on 2 numbers? Enter 1 for binary conversion and 2 for standard operations.\n"))

    if whichCalc == 1:
        go_again = True

        while go_again == True:
            number = int(input("Enter the number you want to be converted:\n"))
            if number < 0:
                go_again = True
                print("The entered number was not positive, please try again.\n")
            elif number >= 0:
                go_again = False
                listofZerosandOnes = []
                while number > 0:
                    binarynumber = number % 2
                    listofZerosandOnes.append(binarynumber)
                    number = number // 2
                listofZerosandOnes.reverse()
                for x in listofZerosandOnes:
                        print(x, end=" ")

    elif whichCalc == 2:
        again = True

        num1 = float(input("Enter the 1st number you would like to convert:\n"))
        num2 = float(input("Enter the 2nd number you would like to convert:\n"))
        while again == True:
            operator = input("Enter the operation you wish to perform.\n")
            if operator != '*' and operator != '+' and operator != '-' and operator != "**" and operator != '/':
                again = True
                print("The entered operator was not one listed. Please enter it again.\n")
            else: 
                again = False
                if operator == '*':
                    print(num1 * num2)
                elif operator == '+':
                    print(num1 + num2)
                elif operator == '-':
                    print(num1 - num2)
                elif operator == "**":
                    print(num1 ** num2)
                elif operator == '/':
                    print(num1 / num2)
    go_again_int = 1
    go_again_int = int(input("\nEnter 1 if you would like to calcualte again and 2 if you would like to quit."))
    if go_again_int == 1:
        whole_prog_again = True
    else:
        whole_prog_again = False

            


    

            





    

    
