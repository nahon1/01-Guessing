import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 66

while not quit:
    random_number = random.randint(6,range)
    count = 1
    number = -1
    while number != random_number:
        number = input("Guess the correct number between 6 and {} ".format(range) + "or pay the price: ")
        if not number.isdigit():
            print("Do you know what a number is?")
        else:
            number = int(number)
            count = count + 1
            print("You can't get it right, can you?")
            if number > random_number:
                print("Your number is TOO HIGH!")
            elif number < random_number:
                print("Your number is TOO LOW!")
    print("You FINALLY guessed it right!!!")
    print("It took you {} tries!".format(count))
    play_again = input("\nTry again to get a better result! (yes or no) ")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True

print("\n\nBye~~~")




