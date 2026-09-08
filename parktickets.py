age = int(input("How old are you? "))
money = int(input("How much money do you have? "))
weather = input("How is the weather? (sunny/rainy/snowy): ")
 
# AND: both conditions must be true
if age >= 12 and money >= 20:
    print("You can buy a ticket! ")
 
    # OR: either condition can be true
    if weather == "rainy" or weather == "snowy":
        print("But the rides are closed because of the weather! ")
    else:
        print("The rides are open! Have fun! ")
 
else:
    print("Sorry! You don't meet the age or money requirement. ")
