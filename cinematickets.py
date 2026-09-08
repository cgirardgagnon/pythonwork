customer = 0
while customer == 0:
    name = input("What is your name?\n")
    age = int(input("How old are you?\n"))
    money = float(input("How much money do you have?\n"))
    popcorn = input("Did you bring popcorn yes/no?\n")

    if age < 18:
        print(f"Nice try, {name}! Go home and watch cartoons! 🍼📺😂")
    elif money < 15 and age >= 100:
        print(f"Sorry, {name}, I doubt you'd hear the movie anyway...")
    elif money < 15 and age > 18:
        print(f"Sorry {name}, ERROR 404: MONEY NOT FOUND! 💸😂")
    elif money > 15 and age >= 18 and popcorn == "yes":
        print(f"“Welcome {name}! Ticket ✅ Popcorn ✅ Life is good! 🍿😎”")
    elif money > 15 and age >= 18 and popcorn == "no":
        print(f"Welcome {name}... but coming to the cinema without popcorn is VERY suspicious. 👀😂")
        
    answer = input("Is there an other customer?\n")

    while answer != "yes" and answer != "no":
        print("Invalid answer! Please enter yes or no.")
        answer = input("Is there an other customer?\n")

    if answer == "no":
        customer = 1

print("Thank you for buying tickets!")
