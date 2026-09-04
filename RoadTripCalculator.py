firstName = input("Please put your first name: ")
tripDistance = float(input("how many KM will you travel? "))
fuelConsumption = float(input("How much fuel per 100 km does your car consumes? "))
gasPrice = float(input("What is the price of the gas per liter? "))
numberTravelers = int(input("How many travelers will be in the trip? "))

gasNeeded = (tripDistance / 100) * fuelConsumption
totalCost = gasNeeded * gasPrice
CostPerTraveler = totalCost / numberTravelers
print(f"Hi {firstName} . "
      f"For your "+ str(tripDistance) + " km trip, with a fuel consumption of " + str(fuelConsumption) + " liters per 100 km, and a gas price of " + str(gasPrice) + " per liter, " 
      f"Your trip will cost " + str(int(totalCost)) + " in total, and each traveler will pay " + str(int(CostPerTraveler)) + ".")
