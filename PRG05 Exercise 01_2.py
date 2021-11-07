# With this command, after receiving some input, can be compared if the name is correct or not. 
# if correct
# elif not correct (else if)

goede_naam = input("Wat is je naam?")
if goede_naam == "Marieke":
    print("Hello, Welcome", goede_naam, "!")
elif goede_naam != "Marieke:":
    print("You are", goede_naam, "not Marieke. Please Leave.")
