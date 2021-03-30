#coins
#Coin Converter Lab
print("Please enter the amount of money to convert:")
print()
number_of_dollars = int(input("# of dollars: "))
number_of_cents = int(input("# of cents: "))
total = number_of_cents + 100 * number_of_dollars

#convert
number_of_quarters = total // 25
balance1 = total % 25
number_of_dimes = balance1 // 10
balance2 = balance1 % 10
number_of_nickels = balance2 // 5
balance3 = balance2 % 5
number_of_pennies = balance3

print("The coins are", number_of_quarters, "quarters,", number_of_dimes, 
      "dimes,", number_of_nickels, "nickels and", number_of_pennies, "pennies")