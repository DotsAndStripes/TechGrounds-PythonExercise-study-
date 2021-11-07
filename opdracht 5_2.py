# With if, elif and else, we can create the game of number guessing
# if < 100, a line will be printed out with a suggestion.
# elif > 100, a line will be printed out with another suggestion
# else gives the right value => 100 and will print the last line.
# To start the while loop, we have to give the value 99 to the number (of each other value for NOT being 100!) 
# so the while loop can start. 
# As soon as the input number = 100, the while loop will end and print the last line. The game is finished.

number =99

while number != 100:

    number = int(input("Please enter a number: "))
    if number < 100:
        print("Sorry, your response is too low.")

    elif number > 100:
        print("Sorry, your response is too high.")

    else:
        print("You've found the right number!! Well Done!")