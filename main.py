# firstNumber = input("First: ")
# secondNumber = input("Second: ")
# print("Sum:",(int(firstNumber) + int(secondNumber)))


# number1 = float(input("First: "))
# number2 = float(input("Second: "))
# print(f"Sum: {number1 + number2}")

# weight = float(input("Weight: "))
# unit = input("(K)g or (L)bs: ")
# if unit.lower() == 'k':
#     print(f"Weight in lbs: {weight / 0.45359237}")
# elif unit.lower() == 'l':
#     print(f"Weight in Kg: {weight * 0.45359237}")
# else:
#     print("You didn't type in K or L, you fuck.")

#PRICES IN KG
priceOfSilverPerKg = 912.76
priceOfGoldPerKg = 1653.90
#PRICES IN LBS
priceOfSilverPerLbs = priceOfSilverPerKg * .453
priceOfGoldPerLbs = priceOfGoldPerKg * .453

metal = input("Please enter a metal: ")
weight = float(input("Please enter a weight: "))
unit = input("Please enter a weight unit: ")

if metal.lower() == 'silver' or metal.lower() == 'ag':
    if unit.lower() == "k":
        print(f"You have ${priceOfSilverPerKg * weight} worth of silver.")
    if unit.lower() == "l":
        print(f"You have ${priceOfSilverPerLbs * weight} worth of silver")
elif metal.lower() == 'gold' or metal.lower() == 'au':
    if unit.lower() == "k":
        print(f"You have ${priceOfGoldPerKg * weight} worth of gold")
    if unit.lower() == "l":
        print(f"You have ${priceOfGoldPerLbs * weight} worth of gold")

