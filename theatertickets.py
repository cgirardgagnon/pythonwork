flag = 0
 
while flag == 0:
 
    # Get and validate name
    name = input("What is your name? ").strip()
 
    while name == "":
        print("Invalid name. Please enter your name.")
        name = input("What is your name? ").strip()
 
 
    # Get and validate age
    ageInput = input("How old are you? ")
 
    while not ageInput.isdigit():
        print("Invalid age. Please enter a number.")
        ageInput = input("How old are you? ")
 
    age = int(ageInput)
 
    while age <= 0:
        print("Invalid age. Age must be greater than 0.")
        age = int(input("How old are you? "))
 
 
    # Get and validate money
    moneyInput = input("How much money do you have? $")
 
    while not moneyInput.replace(".", "", 1).isdigit():
        print("Invalid amount. Please enter a number.")
        moneyInput = input("How much money do you have? $")
 
    money = float(moneyInput)
 
 
    # Get and validate snacks
    snacks = input("Did you buy snacks? (yes/no): ").lower()
 
    while snacks != "yes" and snacks != "no":
        print("Invalid answer. Please enter yes or no.")
        snacks = input("Did you buy snacks? (yes/no): ").lower()
 
 
    # Regular ticket price
    ticketPrice = 15
 
    # Apply 10% discount
    if snacks == "yes":
        discount = ticketPrice * 0.10
        ticketPrice = ticketPrice - discount
        print("You bought snacks! You get a 10% discount.")
 
 
    # Check if customer can enter
    if age >= 18 and money >= ticketPrice:
        print(f"Welcome {name}! You can buy the movie ticket.")
        print(f"Your ticket price is ${ticketPrice:.2f}.")
 
    else:
        if age < 18:
            print(f"Sorry {name}, you must be at least 18 years old.")
        else:
            print(f"Sorry {name}, you do not have enough money.")
            print(f"You need ${ticketPrice:.2f}.")
 
 
    # Ask if another customer wants to use the app
    answer = input("Do you want to check another customer? (yes/no): ").lower()
 
    while answer != "yes" and answer != "no":
        print("Invalid answer. Please enter yes or no.")
        answer = input("Do you want to check another customer? (yes/no): ").lower()
 
    if answer == "no":
        flag = 1
 
 
print("Cinema closed. Thank you!")
