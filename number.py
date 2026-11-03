










def add_guess(guesses):
    """Add a new guess to the list."""
    number = input("ENTER YOUR GUESS: ").strip()
    if number.isdigit() or (number.startswith("-") and number[1:].isdigit()):
        number = int(number)
        if number in guesses:
            print("THIS NUMBER HAS ALREADY BEEN ENTERED!")
        else:
            guesses.append(number)
            print("GUESS ADDED SUCCESSFULLY!")
    else:
        print("PLEASE ENTER A VALID INTEGER!")


def show_guesses(guesses):
    """Display all registered guesses."""
    if len(guesses) == 0:
        print("NO GUESSES AVAILABLE!")
    else:
        print("---------- YOUR GUESSES ----------")
        number = 1
        for guess in guesses:
            print(number, ".", guess)
            number = number + 1


def count_guesses(guesses):
    """Display the total number of guesses."""
    print("TOTAL GUESSES:", len(guesses))


def find_largest(guesses):
    """Find and display the largest guess."""
    if len(guesses) == 0:
        print("NO GUESSES AVAILABLE!")
    else:
        largest = guesses[0]
        for guess in guesses:
            if guess > largest:
                largest = guess
        print("LARGEST GUESS:", largest)


def clear_guesses(guesses):
    """Remove all guesses from the list."""
    if len(guesses) == 0:
        print("THE LIST IS ALREADY EMPTY!")
    else:
        guesses.clear()
        print("ALL GUESSES HAVE BEEN DELETED!")




guesses = []

print("==========================")
print("    NUMBER GUESSING ")
print("==========================")
while True:
    print()
    print("========== MAIN MENU ==========")
    print("1. ADD GUESS")
    print("2. SHOW GUESSES")
    print("3. COUNT GUESSES")
    print("4. FIND LARGEST GUESS")
    print("5. CLEAR GUESSES")
    print("6. EXIT")
    print("===============================")
    choice = input("CHOOSE AN OPTION: ").strip()
    match choice:
        case "1":
            add_guess(guesses)
        case "2":
            show_guesses(guesses)
        case "3":
            count_guesses(guesses)
        case "4":
            find_largest(guesses)
        case "5":
            clear_guesses(guesses)
        case "6":
            print("THANK YOU FOR PLAYING!")
            print("PROGRAM FINISHED!")
            break
        case _:
            print("INVALID OPTION!")
            continue
