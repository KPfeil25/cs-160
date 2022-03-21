def count_letters(name_list):
    letters_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for name in name_list:
        for i in range(len(name)):
            if name[i] in letters_dict:
                letters_dict[name[i]] += 1
    print("Letters and their occurences:\n")
    for letter in letters_dict.keys():
        if letters_dict[letter] != 0:
            print(letter, ': ', letters_dict[letter])

def create_name_list():
    go_again = True
    name_list = []

    while go_again == True:
        choice = int(input("Enter 1 to add a name to the list or 2 to end this part:\n"))
        if choice == 1:
            name = input("Enter the name you want to add:\n")
            name_list.append(name)
            go_again = True
        elif choice == 2:
            go_again = False
        else:
            print("You did not enter 1 or 2!")
            go_again = True
    count_letters(name_list)

def num_lists():
    go_again = True
    num_list1 = []
    num_list2 = []

    while go_again == True:
        list_1_len = int(input("How long do you want list 1 to be?\n"))
        list_2_len = int(input("How long do you want list 2 to be?\n"))
        if list_1_len > 0 and list_2_len > 0:
            go_again = False
            for i in range (0, list_1_len):
                num = int(input("Enter number " + str(i+1) + " out of " + str(list_1_len) + " for string 1\n"))
                num_list1.append(num)
            for i in range (0, list_2_len):
                num = int(input("Enter number " + str(i+1) + " out of " + str(list_2_len) + " for string 2\n"))
                num_list2.append(num)
        else:
            print("Boths lists must be of positive length!")
            go_again = True
    
    list_sums(num_list1, num_list2)
    list_avgs(num_list1, num_list2)
    is_equal_length(num_list1, num_list2)
    are_same_sums(num_list1, num_list2)
    return_common_numbers(num_list1, num_list2)


def is_equal_length(list1, list2):
    if len(list1) == len(list2):
        print("The lists are of equal length!")
    else:
        print("The lists are not of equal length!")

def list_sums(list1, list2):
    sum1 = 0
    sum2 = 0
    for i in range (0, len(list1)):
        sum1 += list1[i]
    for i in range (0, len(list2)):
        sum2 += list2[i]
    print("The sum of list 1 is " + str(sum1))
    print("The sum of list 2 is " + str(sum2))

def list_avgs(list1, list2):
    sum1 = 0
    sum2 = 0
    for i in range (0, len(list1)):
        sum1 += list1[i]
    for i in range (0, len(list2)):
        sum2 += list2[i]
    avg1 = (sum1 / len(list1))
    avg2 = (sum2 / len(list2))
    print("The average of list 1 is " + str(avg1))
    print("The average of list 2 is " + str(avg2))

def are_same_sums(list1, list2):
    sum1 = 0
    sum2 = 0
    for i in range (0, len(list1)):
        sum1 += list1[i]
    for i in range (0, len(list2)):
        sum2 += list2[i]
    if sum1 == sum2:
        print("The sums are the same!")
    else:
        print("The sums are not the same!")

def return_common_numbers(list1, list2):
    common_numbers = []
    if len(list1) > len(list2):
        for i in range (0, len(list2)):
            if list1[i] == list2[i]:
                common_numbers.append(list1[1])
    elif len(list1) < len(list2):
        for i in range (0, len(list1)):
            if list1[i] == list2[i]:
                common_numbers.append(list1[i])
    else:
        for i in range (0, len(list2)):
            if list1[i] == list2[i]:
                common_numbers.append(list1[i])
    print("The common numbers are: " + str(common_numbers))

def main():
    create_name_list()
    num_lists()

main()