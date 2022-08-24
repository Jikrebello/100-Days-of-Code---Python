print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? R"))
percentage_tip = int(input("What percentage tip would you like to give? 10%, 12% or 15% "))
tip_amount = (percentage_tip / 100) + 1
total_people = int(input("How many people to split the bill? "))
individual_contribution = (total_bill / total_people) * tip_amount
print("Each person should pay: R{:.2f}".format(individual_contribution))
