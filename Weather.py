flag = 0
 
while flag == 0:
 
    weather = input("How is the weather? (good/rainy/snowy): ")
 
    if weather == "good":
        print("Go outside and have fun! ")
 
    elif weather == "rainy":
        print("Take an umbrella! ")
 
    elif weather == "snowy":
        print("Wear a warm jacket! ")
 
    else:
        print("Stay home and relax! ")
 
    answer = input("Do you want to check again? (yes/no): ")
 
    # Keep asking until the user enters yes or no
    while answer != "yes" and answer != "no":
        print("Invalid answer! Please enter yes or no.")
        answer = input("Do you want to check again? (yes/no): ")
 
    if answer == "no":
        flag = 1
 
print("Thank you for using the Weather App!")
