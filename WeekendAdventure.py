name = input("Name: ")
age = int(input("Age: "))
weather = input("Weather (good/bad):")
friends = int (input("How many friends are you bringing? "))
budget_per_person = float(input("Budget per person: "))

total_budget = friends * budget_per_person

print(f"Hi {name}, you are {age} years old. The weather is {weather}. You are bringing {friends} friends, and your total budget is ${total_budget:.2f}.")

if weather == "good" and total_budget >= 100:
    print("You can go to a theme park or a concert!")
elif weather == "good" and total_budget < 100:
    print("Great! You can go hiking or have a picnic!")
else:
    print("Since the weather is bad, you can go to a museum or watch a movie indoors.")
    
