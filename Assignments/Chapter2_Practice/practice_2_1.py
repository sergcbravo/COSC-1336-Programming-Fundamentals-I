# This program calculates the total and average cost of a meal (hamburger, fries, shake).

# Asking user for costs
hamburger_cost = float(input("Enter the cost of the hamburger: "))
fries_cost = float(input("Enter the cost of the fries: "))
shake_cost = float(input("Enter the cost of the shake: "))

# Calculating total and average
total_cost = hamburger_cost + fries_cost + shake_cost
average_cost = total_cost / 3

# Displaying results
print(f"The cost is: ${int(total_cost)}")
print(f"The average cost is: ${int(average_cost)}")
