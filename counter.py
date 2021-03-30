#Write a program that asks the user to enter a number of quarters, dimes, 
# nickels and pennies and then outputs the monetary value of the coins in the 
# format of dollars and remaining cents.Your program should interact with the 
# user exactly as it shows in the following example:
    
print("Please enter the number of coins:")
q = int(input("# of quarters: "))
d = int(input("# of dimes: "))
n = int(input("# of nickels: "))
p = int(input("# of pennies: "))

#calculating
total = 25 * q + 10 * d + 5 * n + 1 * p
number_of_dollars = total // 100
number_of_cents = total % 100

print("The total is", number_of_dollars, "dollars and", number_of_cents, 
      "cents" )