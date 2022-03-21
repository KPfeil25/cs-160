def which_summation():
    ask_again = True

    while ask_again == True:
        choice = int(input("Do you want to sum up the equation or integrate it? Enter 1 for summation or 2 for integrate.\n"))

        if choice == 1:
            ask_again = False
            return choice

        elif choice == 2:
            choice2 = int(input("Enter 2 to integrate with trapezoids or 3 to integrate with rectangles:\n"))
            if choice2 == 1:
                return choice
            elif choice == 2:
                return choice
            else:
                ask_again = True
        else:
            ask_again = True

def get_numbers(choice):
    if choice == 1:
        num1 = int(input("Enter starting number for the summation:\n"))
        num2 = int(input("Enter ending number for the summation:\n"))
        return num1, num2

    elif choice == 2 or choice == 3:
        num3 = int(input("Enter starting number for the integration:\n"))
        num4 = int(input("Enter ending number for the integration:\n"))
        num5 = int(input("Enter the number of trapezoids/ rectangles you want:\n"))
        return num3, num4, num5

def which_formula():
    go_again = True

    print("Formula 1: 10x^2\n")
    print("Formula 2: 2x^2 - 5\n")
    print("Formula 3: x + 20\n")
    
    choice = int(input("Which formula do you want to use? Enter 1 for formula 1, etc.\n"))
    
    if choice == 1 or choice == 2 or choice == 3:
        go_again = False
        return choice
    else:
        go_again = True

def summation_calculations(formula, num1, num2):
    if formula == 1:
        total = 0
        for i in range (num1, num2):
            total = total + ((10*(i**2)))
    elif formula == 2:
        total = 0
        for i in range (num1, num2):
            total = total + (2*(i**2) - 5)
    elif formula == 3:
        total = 0
        for i in range (num1, num2):
            total = total + (i+20)
    return total

def trapezoid_integration(formula, start, end, num_trapezoids):
    if formula == 1:
        total = 0
        width = ((end - start) / num_trapezoids)
        for i in range (start, end):
            total = total + (0.5*(((10*((i*width)**2)) + (10*(((i+1)*width)**2)))*width))
    elif formula == 2:
        total = 0
        width = ((end - start) / num_trapezoids)
        for i in range (start, end):
            total = total + (0.5*((((2*((i*width)**2))-5) + ((2*(((i+1)*width)**2))-5))*width))
    elif formula == 3:
        total = 0
        width = ((end - start) / num_trapezoids)
        for i in range (start, end):
            total = total + (0.5*((((i*width)+20) + (((i+1)*width)+20))*width))
    return total

def rectangle_integration(formula, start, end, num_trapezoids):
    if formula == 1:
        total = 0
        width = ((end - start) / num_trapezoids)
        for i in range (start, end):
            total = total + ((((10*(i+1)**2)*width) - (((10*(i*width))**2)*width))*width)
    elif formula == 2:
        total = 0
        width = ((end - start) / num_trapezoids)
        for i in range (start, end):
            total = total + (((((2*(i+1)**2)-5)*width) - (((2*(i*width)**2)-5)*width))*width)
    elif formula == 3:
        total = 0
        width = ((end - start) / num_trapezoids)
        for i in range (start, end):
            total = total + (((((i+1)+20)*width) - ((i+20)*width))*width)

def wholeprogram():
    firstchoice = which_summation()
    if firstchoice == 1:
        nums1, nums9 = get_numbers(1)
        formula = which_formula()
        answer = summation_calculations(formula, nums1, nums9)
        print("Your answer is " + str(answer))
    elif firstchoice == 2:
        nums2, nums7, nums8 = get_numbers(2)
        formula = which_formula()
        answer = trapezoid_integration(formula, nums2, nums7, nums8)
        print("Your answer is " + str(answer))
    elif firstchoice == 3:
        nums4, nums5, nums6 = get_numbers(3)
        formula = which_formula()
        answer = rectangle_integration(formula, nums4, nums5, nums6)
        print("Your answer is " + str(answer))

prog_again = True

while prog_again == True: 
    wholeprogram()
    choice = int(input("Enter 1 to run this calculator again or 2 to quit!\n"))
    if choice == 1:
        prog_again = True
    elif choice == 2:
        prog_again = False




