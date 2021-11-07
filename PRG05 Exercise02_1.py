number =99

while number != 100:

    number = int(input("Please enter a number: "))
    if number < 100:
        print("Sorry, your response is too low.")

    elif number > 100:
        print("Sorry, your response is too high.")

    else:
        print("You've found the right number!! Well Done!")
