firstName = input("Please put your first name: ")
travelDestination = input("What is your favorite travel destination? ")
travelDays = input("How many days will you travel? ")
Dailybudget = input("how much money per day will you budget? ")
print(f"Hi {firstName} . "
      f"Your  {travelDays} -day trip to {travelDestination} will cost {int(travelDays) * int(Dailybudget)}.")
