print("Welcome to this adventure game! You will be given 2 options and please enter 1 or 2 to make the choice.")
choice1 = int(input("Do you want to go to Europe or Antarctica? Enter 1 for Europe or 2 for Antarctica\n"))

if choice1 == 1:
    choice2 = int(input("Welcome to Europe! You may now go ski in the alps or bath in the sun in Slovenia. Enter 1 for skiing or 2 for Slovenia!\n"))
    if choice2 == 1:
        print("Skiing was enjoyable but you realized you would rather be in Slovenia because sun is nice. Oh well, next time!")
    elif choice2 == 2:
        print("Choosing the sun in Slovenia was great, and you even ended up going skydiving!")

elif choice1 == 2:
    choice3 = int(input("Welcome to Antarctica! Who the heck goes here. Enter 1 to go on a boat trip or 2 to go on a hike!\n"))
    if choice3 == 1:
        print("Boating was great! Pengiuns were seen and given names. What a great time.")
    elif choice3 == 2:
        choice4 = int(input("Hiking is a good choice! Enter 1 to hike a mountain or 2 to go across a snowfield.\n"))
        if choice4 == 1:
            print("Going up the mountain was great! Sledding down it after was even more fun.")
        elif choice4 == 2:
            print("Hiking across the snowfield was fun, and you saw polar bears! What a great day.")